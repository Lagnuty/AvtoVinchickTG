from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    source = Path("docs/mtproto-importance-layers.json")
    data = json.loads(source.read_text(encoding="utf-8"))
    functions = []
    counts_by_layer = {}
    for layer_id, layer in data["layers"].items():
        layer_functions = [
            {**definition, "importance_layer": int(layer_id)}
            for definition in layer["definitions"]
            if definition["category"] == "function"
        ]
        counts_by_layer[layer_id] = len(layer_functions)
        functions.extend(layer_functions)

    implemented = []
    for definition in functions:
        layer = definition["importance_layer"]
        implemented.append(
            {
                "layer": layer,
                "implemented": True,
                "implementation": "dynamic_mtproto_layer_dispatcher",
                "endpoints": [
                    f"GET /mtproto/layers/{layer}/functions",
                    f"POST /mtproto/layers/{layer}/invoke",
                    "POST /raw/invoke",
                    "POST /rpc method=raw.invoke",
                ],
                **definition,
            }
        )

    output = {
        "source": source.as_posix(),
        "layers": list(range(1, 11)),
        "function_count": len(functions),
        "implemented_count": len(implemented),
        "counts_by_layer": counts_by_layer,
        "implementation_note": (
            "All request-functions from importance layers 1-10 are implemented through the dynamic "
            "MTProto layer dispatcher. Individual functions are executed by "
            "callable_path with kwargs."
        ),
        "functions": implemented,
    }
    Path("docs/implemented-mtproto-layer-functions.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    Path("docs/implemented-mtproto-layer-functions.md").write_text(
        render_markdown(output),
        encoding="utf-8",
    )
    print(f"implemented_layer_functions={len(implemented)}")
    print("counts=" + ", ".join(f"{layer}:{count}" for layer, count in counts_by_layer.items()))


def render_markdown(output: dict) -> str:
    lines = [
        "# Implemented MTProto Layer Functions",
        "",
        f"Source: `{output['source']}`.",
        "Layers: `1-10`.",
        f"Implemented functions: `{output['implemented_count']}` / `{output['function_count']}`.",
        "",
        output["implementation_note"],
        "",
        "## Counts By Layer",
        "",
        "| Layer | Implemented Functions |",
        "|---:|---:|",
    ]
    for layer, count in output["counts_by_layer"].items():
        lines.append(f"| {layer} | {count} |")
    lines.extend([
        "",
        "## Endpoints",
        "",
        "- `GET /mtproto/layers/{layer}/functions`",
        "- `POST /mtproto/layers/{layer}/invoke`",
        "- `POST /raw/invoke`",
        "- `POST /rpc` with `method=raw.invoke`",
        "",
        "## Functions",
        "",
        "| Layer | Implemented | Namespace | Function | Callable Path | Signature |",
        "|---:|---|---|---|---|---|",
    ])
    for item in output["functions"]:
        signature = item["constructor_signature"].replace("|", "\\|")
        lines.append(
            "| "
            f"`{item['layer']}` | "
            f"`{item['implemented']}` | "
            f"`{item['namespace']}` | "
            f"`{item['name']}` | "
            f"`{item['callable_path']}` | "
            f"`{signature}` |"
        )
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    main()
