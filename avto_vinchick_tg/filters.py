from __future__ import annotations

from dataclasses import dataclass, field
import re
from typing import Any


@dataclass(frozen=True)
class FilterSettings:
    banned_text: list[str] = field(default_factory=list)
    required_text: list[str] = field(default_factory=list)
    banned_regex: list[str] = field(default_factory=list)
    required_regex: list[str] = field(default_factory=list)
    min_words: int = 0
    max_words: int = 0
    min_chars: int = 0
    max_chars: int = 0
    min_age: int = 0
    max_age: int = 0
    reject_without_age: bool = False
    require_photo: bool = False
    reject_links: bool = False
    reject_mentions: bool = False

    @classmethod
    def from_dict(cls, data: dict[str, Any] | None) -> "FilterSettings":
        data = data or {}
        return cls(
            banned_text=split_lines(data.get("banned_text")),
            required_text=split_lines(data.get("required_text")),
            banned_regex=split_lines(data.get("banned_regex")),
            required_regex=split_lines(data.get("required_regex")),
            min_words=as_int(data.get("min_words")),
            max_words=as_int(data.get("max_words")),
            min_chars=as_int(data.get("min_chars")),
            max_chars=as_int(data.get("max_chars")),
            min_age=as_int(data.get("min_age")),
            max_age=as_int(data.get("max_age")),
            reject_without_age=bool(data.get("reject_without_age")),
            require_photo=bool(data.get("require_photo")),
            reject_links=bool(data.get("reject_links")),
            reject_mentions=bool(data.get("reject_mentions")),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "banned_text": "\n".join(self.banned_text),
            "required_text": "\n".join(self.required_text),
            "banned_regex": "\n".join(self.banned_regex),
            "required_regex": "\n".join(self.required_regex),
            "min_words": self.min_words,
            "max_words": self.max_words,
            "min_chars": self.min_chars,
            "max_chars": self.max_chars,
            "min_age": self.min_age,
            "max_age": self.max_age,
            "reject_without_age": self.reject_without_age,
            "require_photo": self.require_photo,
            "reject_links": self.reject_links,
            "reject_mentions": self.reject_mentions,
        }


@dataclass(frozen=True)
class FilterResult:
    accepted: bool
    reasons: list[str] = field(default_factory=list)
    age: int | None = None
    word_count: int = 0
    char_count: int = 0


def evaluate_profile(text: str, settings: FilterSettings, *, has_media: bool = False) -> FilterResult:
    normalized = text.casefold()
    words = re.findall(r"\w+", text, flags=re.UNICODE)
    reasons: list[str] = []
    age = extract_age(text)

    if settings.require_photo and not has_media:
        reasons.append("нет фото/медиа")
    if settings.reject_without_age and age is None:
        reasons.append("возраст не найден")
    if age is not None and settings.min_age and age < settings.min_age:
        reasons.append(f"возраст {age} меньше {settings.min_age}")
    if age is not None and settings.max_age and age > settings.max_age:
        reasons.append(f"возраст {age} больше {settings.max_age}")
    if settings.min_words and len(words) < settings.min_words:
        reasons.append(f"слов {len(words)} меньше {settings.min_words}")
    if settings.max_words and len(words) > settings.max_words:
        reasons.append(f"слов {len(words)} больше {settings.max_words}")
    if settings.min_chars and len(text) < settings.min_chars:
        reasons.append(f"символов {len(text)} меньше {settings.min_chars}")
    if settings.max_chars and len(text) > settings.max_chars:
        reasons.append(f"символов {len(text)} больше {settings.max_chars}")
    if settings.reject_links and re.search(r"(https?://|t\.me/|www\.)", normalized):
        reasons.append("есть ссылка")
    if settings.reject_mentions and re.search(r"(?<!\w)@\w{3,}", text):
        reasons.append("есть @mention")

    for needle in settings.banned_text:
        if needle.casefold() in normalized:
            reasons.append(f"запрещенный текст: {needle}")
    for needle in settings.required_text:
        if needle.casefold() not in normalized:
            reasons.append(f"нет обязательного текста: {needle}")
    for pattern in settings.banned_regex:
        if regex_search(pattern, text):
            reasons.append(f"запрещенный regex: {pattern}")
    for pattern in settings.required_regex:
        if not regex_search(pattern, text):
            reasons.append(f"нет обязательного regex: {pattern}")

    return FilterResult(
        accepted=not reasons,
        reasons=reasons,
        age=age,
        word_count=len(words),
        char_count=len(text),
    )


def extract_age(text: str) -> int | None:
    patterns = [
        r"(?<!\d)(1[4-9]|[2-6]\d)(?!\d)\s*(?:год|года|лет|yo|y\.o\.)",
        r"(?:age|возраст)\D{0,8}(1[4-9]|[2-6]\d)(?!\d)",
        r"(?<!\d)(1[4-9]|[2-6]\d)(?!\d)",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE | re.UNICODE)
        if match:
            return int(match.group(1))
    return None


def regex_search(pattern: str, text: str) -> bool:
    try:
        return re.search(pattern, text, flags=re.IGNORECASE | re.UNICODE) is not None
    except re.error:
        return False


def split_lines(value: Any) -> list[str]:
    if isinstance(value, list):
        items = value
    else:
        items = str(value or "").splitlines()
    return [str(item).strip() for item in items if str(item).strip()]


def as_int(value: Any) -> int:
    try:
        return max(0, int(value or 0))
    except (TypeError, ValueError):
        return 0
