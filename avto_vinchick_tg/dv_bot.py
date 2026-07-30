from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import re


class DvMessageKind(str, Enum):
    PROFILE = "profile"
    AD = "ad"
    LIKE_NOTICE = "like_notice"
    MATCH_NOTICE = "match_notice"
    MENU = "menu"
    FOUND_PROMPT = "found_prompt"
    WAITING = "waiting"
    OWN_PROFILE = "own_profile"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class DvActionSettings:
    auto_skip_rejected: bool = True
    accepted_action: str = "notify"
    auto_open_found: bool = True
    ignore_ads: bool = True
    forward_likes: bool = True
    auto_decline_like_prompts: bool = False

    @classmethod
    def from_dict(cls, data: dict | None) -> "DvActionSettings":
        data = data or {}
        return cls(
            auto_skip_rejected=bool(data.get("auto_skip_rejected", True)),
            accepted_action=str(data.get("accepted_action") or "notify"),
            auto_open_found=bool(data.get("auto_open_found", True)),
            ignore_ads=bool(data.get("ignore_ads", True)),
            forward_likes=bool(data.get("forward_likes", True)),
            auto_decline_like_prompts=bool(data.get("auto_decline_like_prompts", False)),
        )

    def to_dict(self) -> dict:
        return {
            "auto_skip_rejected": self.auto_skip_rejected,
            "accepted_action": self.accepted_action,
            "auto_open_found": self.auto_open_found,
            "ignore_ads": self.ignore_ads,
            "forward_likes": self.forward_likes,
            "auto_decline_like_prompts": self.auto_decline_like_prompts,
        }


def classify_dv_message(text: str) -> DvMessageKind:
    compact = normalize_text(text)
    lower = compact.casefold()

    if not compact:
        return DvMessageKind.UNKNOWN
    if "так выглядит твоя анкета" in lower:
        return DvMessageKind.OWN_PROFILE
    if "подождем пока кто-то увидит твою анкету" in lower:
        return DvMessageKind.WAITING
    if re.search(r"наш[её]л\s+\d+.*показать\?", lower):
        return DvMessageKind.FOUND_PROMPT
    if "1. смотреть анкеты" in lower and "моя анкета" in lower:
        return DvMessageKind.MENU
    if any(marker in lower for marker in ["premium", "активируй premium", "продлить premium", "⭐"]):
        return DvMessageKind.AD
    if any(
        marker in lower
        for marker in [
            "несколько девушек",
            "хотят познакомиться",
            "хочет познакомиться",
            "хотят пообщаться",
            "кому-то понравилась",
        ]
    ):
        return DvMessageKind.LIKE_NOTICE
    if any(marker in lower for marker in ["взаимная симпатия", "вы понравились друг другу", "есть симпатия"]):
        return DvMessageKind.MATCH_NOTICE
    if looks_like_profile(compact):
        return DvMessageKind.PROFILE
    return DvMessageKind.UNKNOWN


def command_for_accepted(action: str) -> str | None:
    if action == "like":
        return "1"
    if action == "like_message":
        return "2"
    if action == "skip":
        return "3"
    return None


def normalize_text(text: str) -> str:
    return " ".join((text or "").split())


def looks_like_profile(text: str) -> bool:
    if len(text) < 8:
        return False
    if " – " not in text and " - " not in text:
        return False
    return re.search(r"(?<!\d)(1[4-9]|[2-6]\d)(?!\d)", text) is not None
