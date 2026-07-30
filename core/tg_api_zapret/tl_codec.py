from __future__ import annotations

import base64
from datetime import date, datetime, timezone
import importlib
import inspect
from typing import Any, get_args, get_origin

from fastapi import HTTPException
from telethon import utils
from telethon.tl import types


BYTES_MARKER = "bytes"
DATETIME_MARKER = "datetime"
ENTITY_MARKERS = {"entity", "peer", "input_entity", "input_peer"}


def resolve_tl_request(path: str):
    module_name, _, class_name = path.rpartition(".")
    if not module_name or not class_name:
        raise HTTPException(
            status_code=400,
            detail="Use request path like users.GetFullUserRequest",
        )
    try:
        module = importlib.import_module(f"telethon.tl.functions.{module_name}")
        return getattr(module, class_name)
    except (ImportError, AttributeError) as exc:
        raise HTTPException(status_code=400, detail=f"Unknown TL request: {path}") from exc


def resolve_tl_constructor(name: str):
    if "." in name:
        return resolve_tl_request(name)
    try:
        return getattr(types, name)
    except AttributeError as exc:
        raise HTTPException(status_code=400, detail=f"Unknown TL constructor: {name}") from exc


async def build_tl_request(path: str, fields: dict[str, Any], client: Any):
    request_cls = resolve_tl_request(path)
    kwargs = await decode_kwargs(fields, request_cls, client)
    return request_cls(**kwargs)


async def build_tl_object(name: str, fields: dict[str, Any], client: Any | None = None) -> Any:
    constructor = resolve_tl_constructor(name)
    kwargs = await decode_kwargs(fields, constructor, client)
    return constructor(**kwargs)


async def decode_kwargs(fields: dict[str, Any], constructor: Any, client: Any | None = None) -> dict[str, Any]:
    signature = inspect.signature(constructor.__init__)
    kwargs: dict[str, Any] = {}
    for field_name, value in fields.items():
        if field_name == "_":
            continue
        parameter = signature.parameters.get(field_name)
        annotation = parameter.annotation if parameter else inspect.Parameter.empty
        kwargs[field_name] = await decode_tl_value(
            value,
            client=client,
            field_name=field_name,
            annotation=annotation,
        )
    return kwargs


async def decode_tl_value(
    value: Any,
    *,
    client: Any | None = None,
    field_name: str | None = None,
    annotation: Any = inspect.Parameter.empty,
) -> Any:
    if value is None or isinstance(value, str | int | float | bool):
        return await resolve_entity_if_needed(
            value,
            client=client,
            field_name=field_name,
            annotation=annotation,
        )
    if isinstance(value, list):
        item_annotation = list_item_annotation(annotation)
        return [
            await decode_tl_value(
                item,
                client=client,
                field_name=field_name,
                annotation=item_annotation,
            )
            for item in value
        ]
    if isinstance(value, dict):
        marker = value.get("_")
        if marker == BYTES_MARKER:
            return decode_bytes(value)
        if marker == DATETIME_MARKER:
            return decode_datetime(value)
        if marker in ENTITY_MARKERS:
            return await resolve_entity(
                value.get("value") or value.get("id") or value.get("username"),
                client=client,
                annotation=annotation,
            )
        if marker:
            constructor = resolve_tl_constructor(str(marker))
            kwargs = await decode_kwargs(value, constructor, client)
            return constructor(**kwargs)
        return {
            str(key): await decode_tl_value(item, client=client, field_name=str(key))
            for key, item in value.items()
        }
    return value


async def resolve_entity_if_needed(
    value: Any,
    *,
    client: Any | None,
    field_name: str | None,
    annotation: Any,
) -> Any:
    if client is None or value is None or not is_entity_field(field_name, annotation):
        return value
    if not isinstance(value, str | int):
        return value
    return await resolve_entity(value, client=client, annotation=annotation)


async def resolve_entity(value: Any, *, client: Any | None, annotation: Any = None) -> Any:
    if client is None:
        raise HTTPException(status_code=400, detail="Entity resolver requires an authorized client")
    if value is None:
        raise HTTPException(status_code=400, detail="Entity value is required")

    annotation_text = annotation_to_text(annotation)
    if "TypeInputUser" in annotation_text:
        entity = await client.get_entity(value)
        return utils.get_input_user(entity)
    if "TypeInputChannel" in annotation_text:
        entity = await client.get_entity(value)
        return utils.get_input_channel(entity)
    if "TypeInputPeer" in annotation_text or not annotation_text:
        return await client.get_input_entity(value)
    return await client.get_input_entity(value)


def is_entity_field(field_name: str | None, annotation: Any) -> bool:
    annotation_text = annotation_to_text(annotation)
    if "InputPeer" in annotation_text or "InputUser" in annotation_text or "InputChannel" in annotation_text:
        return True
    if not field_name:
        return False
    normalized = field_name.lower()
    return normalized in {
        "entity",
        "peer",
        "to_peer",
        "from_peer",
        "input_peer",
        "user",
        "users",
        "user_id",
        "participant",
        "channel",
        "channels",
        "chat",
        "chats",
        "peers",
    }


def list_item_annotation(annotation: Any) -> Any:
    origin = get_origin(annotation)
    if origin in {list, tuple}:
        args = get_args(annotation)
        if args:
            return args[0]
    annotation_text = annotation_to_text(annotation)
    if "InputPeer" in annotation_text or "InputUser" in annotation_text or "InputChannel" in annotation_text:
        return annotation
    return inspect.Parameter.empty


def annotation_to_text(annotation: Any) -> str:
    if annotation is inspect.Parameter.empty or annotation is None:
        return ""
    return str(annotation)


def decode_bytes(value: dict[str, Any]) -> bytes:
    if "base64" in value:
        return base64.b64decode(str(value["base64"]))
    if "hex" in value:
        return bytes.fromhex(str(value["hex"]))
    if "utf8" in value:
        return str(value["utf8"]).encode("utf-8")
    raise HTTPException(status_code=400, detail="bytes object requires base64, hex, or utf8")


def decode_datetime(value: dict[str, Any]) -> datetime:
    if "timestamp" in value:
        return datetime.fromtimestamp(float(value["timestamp"]), tz=timezone.utc)
    iso = str(value.get("iso") or value.get("value") or "")
    if not iso:
        raise HTTPException(status_code=400, detail="datetime object requires iso or timestamp")
    return datetime.fromisoformat(iso.replace("Z", "+00:00"))


def serialize_tl(value: Any) -> Any:
    if value is None or isinstance(value, str | int | float | bool):
        return value
    if isinstance(value, bytes | bytearray):
        return {"_": BYTES_MARKER, "base64": base64.b64encode(bytes(value)).decode("ascii")}
    if isinstance(value, datetime):
        return {"_": DATETIME_MARKER, "iso": value.isoformat(), "timestamp": value.timestamp()}
    if isinstance(value, date):
        return {"_": "date", "iso": value.isoformat()}
    if isinstance(value, list | tuple | set):
        return [serialize_tl(item) for item in value]
    if isinstance(value, dict):
        return {str(key): serialize_tl(item) for key, item in value.items()}
    if hasattr(value, "to_dict"):
        data = value.to_dict()
        if isinstance(data, dict):
            data.setdefault("_", type(value).__name__)
        return serialize_tl(data)
    return {"_": type(value).__name__, "value": str(value)}
