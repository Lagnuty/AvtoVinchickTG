from __future__ import annotations

import json
from pathlib import Path
from typing import Any


LAYERS: dict[int, dict[str, str]] = {
    1: {
        "title": "Core client basics",
        "description": "Authorization, current user, dialogs, peers, messages, updates.",
    },
    2: {
        "title": "Common messaging and media",
        "description": "Sending, reading, searching, forwarding, uploading, media objects.",
    },
    3: {
        "title": "Account, profile, contacts, privacy",
        "description": "Profile settings, contacts, sessions, privacy, usernames, notifications.",
    },
    4: {
        "title": "Groups, channels, administration",
        "description": "Channels, megagroups, permissions, invites, migrations, boosts.",
    },
    5: {
        "title": "Bots, inline mode, web apps, business",
        "description": "Bot API-adjacent MTProto functions, inline results, web views, business links.",
    },
    6: {
        "title": "Calls, stories, reactions, stickers, premium",
        "description": "User-facing extras that are common but not required for a minimal client.",
    },
    7: {
        "title": "Payments and monetization",
        "description": "Payments, invoices, stars, subscriptions, gifts, revenue-related objects.",
    },
    8: {
        "title": "Discovery, stats, help, localization, organization",
        "description": "Help/config, statistics, folders, chatlists, langpacks, search/discovery support.",
    },
    9: {
        "title": "Security, passport, low-level protocol support",
        "description": "Secure values, password SRP, salts, CDN, encrypted credentials, protocol details.",
    },
    10: {
        "title": "Rare, niche, experimental, internal",
        "description": "Features most integrations never touch: AI compose, SMS jobs, Fragment, niche TL types.",
    },
}


EXACT_FUNCTION_LAYERS = {
    "auth.SendCodeRequest": 1,
    "auth.SignInRequest": 1,
    "auth.LogOutRequest": 1,
    "auth.ExportAuthorizationRequest": 1,
    "auth.ImportAuthorizationRequest": 1,
    "users.GetUsersRequest": 1,
    "users.GetFullUserRequest": 1,
    "messages.GetDialogsRequest": 1,
    "messages.GetHistoryRequest": 1,
    "messages.GetMessagesRequest": 1,
    "messages.SendMessageRequest": 1,
    "messages.ReadHistoryRequest": 1,
    "updates.GetStateRequest": 1,
    "updates.GetDifferenceRequest": 1,
}

FUNCTION_NAMESPACE_LAYERS = {
    "auth": 1,
    "updates": 1,
    "users": 1,
    "messages": 2,
    "upload": 2,
    "photos": 3,
    "contacts": 3,
    "account": 3,
    "channels": 4,
    "bots": 5,
    "phone": 6,
    "stories": 6,
    "stickers": 6,
    "premium": 6,
    "payments": 7,
    "help": 8,
    "stats": 8,
    "folders": 8,
    "chatlists": 8,
    "langpack": 8,
    "aicompose": 10,
    "smsjobs": 10,
    "fragment": 10,
}

TYPE_KEYWORD_LAYERS: list[tuple[int, tuple[str, ...]]] = [
    (
        1,
        (
            "User",
            "Chat",
            "Channel",
            "Peer",
            "InputPeer",
            "Message",
            "Dialog",
            "Update",
            "Updates",
            "Authorization",
        ),
    ),
    (
        2,
        (
            "Media",
            "Photo",
            "Document",
            "File",
            "InputFile",
            "InputMedia",
            "WebPage",
            "Draft",
            "MessageEntity",
            "Reply",
            "Forward",
            "Poll",
            "Geo",
            "Venue",
        ),
    ),
    (
        3,
        (
            "Contact",
            "Privacy",
            "Notify",
            "Theme",
            "WallPaper",
            "Username",
            "EmojiStatus",
            "AutoSave",
            "Account",
            "Session",
        ),
    ),
    (
        4,
        (
            "Admin",
            "Banned",
            "Participant",
            "Invite",
            "ExportedChatInvite",
            "ChatAdmin",
            "ChatBanned",
            "ChannelAdmin",
            "ChannelParticipant",
            "Boost",
            "Forum",
        ),
    ),
    (
        5,
        (
            "Bot",
            "Inline",
            "Keyboard",
            "WebView",
            "WebApp",
            "Business",
            "MenuButton",
            "BotCommand",
        ),
    ),
    (
        6,
        (
            "Call",
            "PhoneCall",
            "Story",
            "Stories",
            "Reaction",
            "Sticker",
            "Premium",
            "Emoji",
            "AttachMenu",
            "SavedReaction",
        ),
    ),
    (
        7,
        (
            "Payment",
            "Invoice",
            "Shipping",
            "Stars",
            "Star",
            "Gift",
            "Giveaway",
            "Revenue",
            "Subscription",
            "Paid",
        ),
    ),
    (
        8,
        (
            "Help",
            "Config",
            "Stats",
            "LangPack",
            "Folder",
            "Chatlist",
            "Search",
            "TopPeer",
            "PopularContact",
        ),
    ),
    (
        9,
        (
            "Secure",
            "Password",
            "Passport",
            "Encrypted",
            "Cdn",
            "Dh",
            "Salt",
            "Key",
            "InputCheckPassword",
            "ResPQ",
            "P_Q",
        ),
    ),
    (
        10,
        (
            "Ai",
            "Sms",
            "Fragment",
            "Todo",
            "AccessPoint",
            "RequirementToContact",
            "ThemeSettings",
        ),
    ),
]


def main() -> None:
    source_path = Path("docs/mtproto-definitions.json")
    data = json.loads(source_path.read_text(encoding="utf-8"))

    layered: dict[int, list[dict[str, Any]]] = {layer: [] for layer in LAYERS}
    for definition in data["definitions"]:
        layer = classify(definition)
        layered[layer].append(definition)

    for definitions in layered.values():
        definitions.sort(key=lambda item: (item["category"], item["namespace"], item["name"]))

    counts = {str(layer): len(definitions) for layer, definitions in layered.items()}
    output = {
        "source": source_path.as_posix(),
        "telethon_version": data["telethon_version"],
        "definition_count": data["definition_count"],
        "layer_count": 10,
        "counts": counts,
        "layers": {
            str(layer): {
                **LAYERS[layer],
                "count": len(definitions),
                "definitions": definitions,
            }
            for layer, definitions in layered.items()
        },
        "notes": [
            "Importance is heuristic, not an official Telegram classification.",
            "The goal is API implementation priority: common client features first, rare/internal features last.",
        ],
    }

    Path("docs/mtproto-importance-layers.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    Path("docs/mtproto-importance-layers.md").write_text(render_markdown(output), encoding="utf-8")

    print(f"definitions={data['definition_count']}")
    print("counts=" + ", ".join(f"{layer}:{count}" for layer, count in counts.items()))


def classify(definition: dict[str, Any]) -> int:
    if definition["category"] == "function":
        exact_key = f"{definition['namespace']}.{definition['name']}"
        if exact_key in EXACT_FUNCTION_LAYERS:
            return EXACT_FUNCTION_LAYERS[exact_key]
        name_layer = classify_by_name(definition["name"])
        namespace_layer = FUNCTION_NAMESPACE_LAYERS.get(definition["namespace"], 10)
        return min(name_layer, namespace_layer) if name_layer else namespace_layer

    name_layer = classify_by_name(definition["name"])
    return name_layer or 10


def classify_by_name(name: str) -> int | None:
    for layer, keywords in TYPE_KEYWORD_LAYERS:
        if any(keyword in name for keyword in keywords):
            return layer
    return None


def render_markdown(output: dict[str, Any]) -> str:
    lines = [
        "# MTProto Importance Layers",
        "",
        f"Source: `{output['source']}`.",
        f"Telethon version: `{output['telethon_version']}`.",
        f"Total definitions: `{output['definition_count']}`.",
        "",
        "Importance is heuristic, not an official Telegram classification.",
        "The goal is implementation priority for this API project.",
        "",
        "## Summary",
        "",
        "| Layer | Title | Count |",
        "|---:|---|---:|",
    ]
    for layer, info in output["layers"].items():
        lines.append(f"| {layer} | {info['title']} | {info['count']} |")

    lines.extend(["", "## Layers", ""])
    for layer, info in output["layers"].items():
        lines.extend(
            [
                f"### Layer {layer}: {info['title']}",
                "",
                info["description"],
                "",
                f"Count: `{info['count']}`.",
                "",
                "| Category | Namespace | Name | Callable Path |",
                "|---|---|---|---|",
            ]
        )
        for item in info["definitions"]:
            lines.append(
                "| "
                f"`{item['category']}` | "
                f"`{item['namespace']}` | "
                f"`{item['name']}` | "
                f"`{item['callable_path']}` |"
            )
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
