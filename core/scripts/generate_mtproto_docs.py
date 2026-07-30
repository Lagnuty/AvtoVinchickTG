from __future__ import annotations

import importlib
import inspect
import json
import pkgutil
from pathlib import Path

import telethon
import telethon.tl.functions as functions
import telethon.tl.types as types


def main() -> None:
    output_dir = Path("docs")
    output_dir.mkdir(exist_ok=True)

    function_items = collect_functions()
    type_items = collect_types()
    definitions = sorted(
        [*function_items, *type_items],
        key=lambda item: (item["category"], item["namespace"], item["name"]),
    )

    data = {
        "source": "Telethon generated TL schema",
        "telethon_version": telethon.__version__,
        "definition_count": len(definitions),
        "function_count": len(function_items),
        "type_constructor_count": len(type_items),
        "categories": {
            "function": len(function_items),
            "type_constructor": len(type_items),
        },
        "definitions": definitions,
    }
    (output_dir / "mtproto-definitions.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (output_dir / "mtproto-definitions.md").write_text(
        render_markdown(data),
        encoding="utf-8",
    )

    function_data = {
        "source": data["source"],
        "telethon_version": telethon.__version__,
        "function_count": len(function_items),
        "namespaces": count_by_namespace(function_items),
        "functions": function_items,
    }
    (output_dir / "mtproto-functions.json").write_text(
        json.dumps(function_data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (output_dir / "mtproto-functions.md").write_text(
        render_functions_markdown(function_data),
        encoding="utf-8",
    )

    print(f"definitions={len(definitions)}")
    print(f"functions={len(function_items)}")
    print(f"type_constructors={len(type_items)}")


def collect_functions() -> list[dict[str, str]]:
    items = []
    for module_info in pkgutil.iter_modules(functions.__path__):
        namespace = module_info.name
        module = importlib.import_module(f"telethon.tl.functions.{namespace}")
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if not name.endswith("Request") or obj.__module__ != module.__name__:
                continue
            signature = str(inspect.signature(obj.__init__))
            items.append(
                {
                    "category": "function",
                    "namespace": namespace,
                    "name": name,
                    "callable_path": f"{namespace}.{name}",
                    "import_path": f"telethon.tl.functions.{namespace}.{name}",
                    "constructor_signature": signature,
                }
            )
    return sorted(items, key=lambda item: (item["namespace"], item["name"]))


def collect_types() -> list[dict[str, str | int]]:
    items = []
    for name, obj in inspect.getmembers(types, inspect.isclass):
        if obj.__module__ != types.__name__ or not hasattr(obj, "CONSTRUCTOR_ID"):
            continue
        signature = str(inspect.signature(obj.__init__))
        items.append(
            {
                "category": "type_constructor",
                "namespace": "types",
                "name": name,
                "callable_path": name,
                "import_path": f"telethon.tl.types.{name}",
                "constructor_id": getattr(obj, "CONSTRUCTOR_ID"),
                "subclass_of_id": getattr(obj, "SUBCLASS_OF_ID"),
                "constructor_signature": signature,
            }
        )
    return sorted(items, key=lambda item: item["name"])


def render_markdown(data: dict) -> str:
    lines = [
        "# MTProto API Definitions",
        "",
        f"Source: Telethon generated TL schema, version `{data['telethon_version']}`.",
        "",
        f"Total definitions: `{data['definition_count']}`.",
        f"Functions: `{data['function_count']}`.",
        f"Type constructors: `{data['type_constructor_count']}`.",
        "",
        "This file lists both callable MTProto request functions and TL type constructors.",
        "",
        "## Full List",
        "",
    ]
    grouped: dict[str, list[dict]] = {}
    for item in data["definitions"]:
        grouped.setdefault(item["category"], []).append(item)
    for category, items in grouped.items():
        lines.extend([f"### `{category}`", ""])
        lines.append("| Namespace | Name | Callable Path | Constructor Signature |")
        lines.append("|---|---|---|---|")
        for item in items:
            lines.append(
                "| "
                f"`{item['namespace']}` | "
                f"`{item['name']}` | "
                f"`{item['callable_path']}` | "
                f"`{escape_markdown_table(item['constructor_signature'])}` |"
            )
        lines.append("")
    return "\n".join(lines)


def render_functions_markdown(data: dict) -> str:
    lines = [
        "# MTProto API Functions",
        "",
        f"Source: Telethon generated TL schema, version `{data['telethon_version']}`.",
        "",
        f"Total functions: `{data['function_count']}`.",
        "",
        "Use `callable_path` values with `/raw/invoke`, for example:",
        "",
        "```json",
        '{"request":"users.GetFullUserRequest","kwargs":{"id":"me"}}',
        "```",
        "",
        "## Namespaces",
        "",
    ]
    for namespace, count in data["namespaces"].items():
        lines.append(f"- `{namespace}`: {count} functions")
    lines.extend(["", "## Full List", ""])

    grouped: dict[str, list[dict]] = {}
    for item in data["functions"]:
        grouped.setdefault(item["namespace"], []).append(item)
    for namespace, items in grouped.items():
        lines.extend([f"### `{namespace}`", ""])
        lines.append("| Function | Callable Path | Constructor Signature |")
        lines.append("|---|---|---|")
        for item in items:
            lines.append(
                "| "
                f"`{item['name']}` | "
                f"`{item['callable_path']}` | "
                f"`{escape_markdown_table(item['constructor_signature'])}` |"
            )
        lines.append("")
    return "\n".join(lines)


def count_by_namespace(items: list[dict[str, str]]) -> dict[str, int]:
    result: dict[str, int] = {}
    for item in items:
        result[item["namespace"]] = result.get(item["namespace"], 0) + 1
    return dict(sorted(result.items()))


def escape_markdown_table(value: str) -> str:
    return value.replace("|", "\\|")


if __name__ == "__main__":
    main()

