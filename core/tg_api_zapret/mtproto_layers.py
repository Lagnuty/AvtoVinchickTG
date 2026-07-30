from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any


@lru_cache(maxsize=1)
def load_importance_layers() -> dict[str, Any]:
    path = Path(__file__).resolve().parent.parent / "docs" / "mtproto-importance-layers.json"
    return json.loads(path.read_text(encoding="utf-8"))


def get_layer_functions(layer: int) -> list[dict[str, Any]]:
    layers = load_importance_layers()["layers"]
    layer_data = layers.get(str(layer))
    if layer_data is None:
        raise ValueError(f"Unknown MTProto importance layer: {layer}")
    return [
        definition
        for definition in layer_data["definitions"]
        if definition["category"] == "function"
    ]


def get_layer_function_paths(layer: int) -> set[str]:
    return {definition["callable_path"] for definition in get_layer_functions(layer)}


def require_layer_function(layer: int, callable_path: str) -> None:
    if callable_path not in get_layer_function_paths(layer):
        raise ValueError(f"{callable_path} is not implemented in MTProto layer {layer}")

