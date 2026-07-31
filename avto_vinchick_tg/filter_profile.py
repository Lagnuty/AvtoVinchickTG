from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any

from avto_vinchick_tg.filters import FilterSettings
from avto_vinchick_tg.taste_model import TasteSettings


PROFILE_FORMAT = "avto_vinchick_tg.filters"
PROFILE_VERSION = 1


@dataclass(frozen=True)
class FilterProfile:
    filters: FilterSettings
    taste: TasteSettings

    def to_dict(self) -> dict[str, Any]:
        return {
            "format": PROFILE_FORMAT,
            "version": PROFILE_VERSION,
            "filters": self.filters.to_dict(),
            "taste": self.taste.to_dict(),
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "FilterProfile":
        if not isinstance(data, dict):
            raise ValueError("JSON profile must be an object")
        if data.get("format") not in {None, PROFILE_FORMAT}:
            raise ValueError("Это не профиль фильтров AvtoVinchickTG")
        return cls(
            filters=FilterSettings.from_dict(data.get("filters")),
            taste=TasteSettings.from_dict(data.get("taste")),
        )


def save_filter_profile(path: Path, profile: FilterProfile) -> None:
    path.write_text(json.dumps(profile.to_dict(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_filter_profile(path: Path) -> FilterProfile:
    return FilterProfile.from_dict(json.loads(path.read_text(encoding="utf-8")))
