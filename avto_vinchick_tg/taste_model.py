from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math
import re
import sys
import zipfile
from pathlib import Path
from typing import Any

from avto_vinchick_tg.dv_bot import classify_dv_message, DvMessageKind
from avto_vinchick_tg.filters import extract_age


FEATURE_BUCKETS = 4096


@dataclass(frozen=True)
class TasteSettings:
    enabled: bool = False
    min_score: int = 55
    min_samples: int = 8

    @classmethod
    def from_dict(cls, data: dict[str, Any] | None) -> "TasteSettings":
        data = data or {}
        return cls(
            enabled=bool(data.get("enabled", False)),
            min_score=max(0, min(100, as_int(data.get("min_score"), 55))),
            min_samples=max(1, as_int(data.get("min_samples"), 8)),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "enabled": self.enabled,
            "min_score": self.min_score,
            "min_samples": self.min_samples,
        }


@dataclass(frozen=True)
class TastePrediction:
    score: int
    trained: bool
    positive_samples: int
    negative_samples: int

    @property
    def total_samples(self) -> int:
        return self.positive_samples + self.negative_samples


@dataclass(frozen=True)
class ImportResult:
    imported: int
    positive: int
    negative: int
    skipped: int


class TasteModel:
    def __init__(self, path: Path | None = None) -> None:
        if path is None:
            path = default_model_path()
        self.path = path
        self.pos: dict[str, float] = {}
        self.neg: dict[str, float] = {}
        self.pos_total = 0.0
        self.neg_total = 0.0
        self.positive_samples = 0
        self.negative_samples = 0
        self.load()

    @property
    def total_samples(self) -> int:
        return self.positive_samples + self.negative_samples

    def predict(self, text: str, *, min_samples: int = 8) -> TastePrediction:
        if self.total_samples < min_samples:
            return TastePrediction(50, False, self.positive_samples, self.negative_samples)
        features = text_features(text)
        vocab = FEATURE_BUCKETS + 16
        pos_log = math.log((self.positive_samples + 1) / (self.total_samples + 2))
        neg_log = math.log((self.negative_samples + 1) / (self.total_samples + 2))
        for feature, count in features.items():
            pos_log += count * math.log((self.pos.get(feature, 0.0) + 1.0) / (self.pos_total + vocab))
            neg_log += count * math.log((self.neg.get(feature, 0.0) + 1.0) / (self.neg_total + vocab))
        diff = max(-40.0, min(40.0, pos_log - neg_log))
        probability = 1.0 / (1.0 + math.exp(-diff))
        return TastePrediction(round(probability * 100), True, self.positive_samples, self.negative_samples)

    def learn(self, text: str, command: str) -> bool:
        command = command.strip()
        if command not in {"1", "2", "4"}:
            return False
        positive = command in {"1", "2"}
        weight = 2.0 if command == "2" else 1.0
        target = self.pos if positive else self.neg
        for feature, count in text_features(text).items():
            target[feature] = target.get(feature, 0.0) + count * weight
            if positive:
                self.pos_total += count * weight
            else:
                self.neg_total += count * weight
        if positive:
            self.positive_samples += 1
        else:
            self.negative_samples += 1
        self.save()
        return True

    def import_export(self, path: Path) -> ImportResult:
        messages = load_export_messages(path)
        imported = positive = negative = skipped = 0
        pending_profile: str | None = None
        for message in messages:
            text = message_text(message)
            if not text:
                continue
            if classify_dv_message(text) == DvMessageKind.PROFILE:
                pending_profile = text
                continue
            command = text.strip()
            if command in {"1", "2", "3", "4"} and pending_profile:
                learn_command = "4" if command == "3" else command
                self.learn(pending_profile, learn_command)
                imported += 1
                if command in {"1", "2"}:
                    positive += 1
                else:
                    negative += 1
                pending_profile = None
            elif pending_profile and classify_dv_message(text) in {DvMessageKind.PROFILE, DvMessageKind.AD}:
                skipped += 1
                pending_profile = text if classify_dv_message(text) == DvMessageKind.PROFILE else None
        return ImportResult(imported, positive, negative, skipped)

    def load(self) -> None:
        if not self.path.exists():
            return
        data = json.loads(self.path.read_text(encoding="utf-8"))
        self.pos = {str(k): float(v) for k, v in (data.get("pos") or {}).items()}
        self.neg = {str(k): float(v) for k, v in (data.get("neg") or {}).items()}
        self.pos_total = float(data.get("pos_total") or 0.0)
        self.neg_total = float(data.get("neg_total") or 0.0)
        self.positive_samples = int(data.get("positive_samples") or 0)
        self.negative_samples = int(data.get("negative_samples") or 0)

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "version": 1,
            "positive_samples": self.positive_samples,
            "negative_samples": self.negative_samples,
            "pos_total": self.pos_total,
            "neg_total": self.neg_total,
            "pos": self.pos,
            "neg": self.neg,
        }
        self.path.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")


def load_export_messages(path: Path) -> list[dict[str, Any]]:
    if path.is_dir():
        return read_result_json(path / "result.json")
    if path.suffix.casefold() == ".zip":
        with zipfile.ZipFile(path) as archive:
            name = next((item for item in archive.namelist() if item.endswith("result.json")), "")
            if not name:
                raise ValueError("В zip не найден result.json")
            return json.loads(archive.read(name).decode("utf-8")).get("messages") or []
    return read_result_json(path)


def read_result_json(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("messages") or []


def message_text(message: dict[str, Any]) -> str:
    value = message.get("text") or ""
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, list):
        parts = []
        for item in value:
            if isinstance(item, str):
                parts.append(item)
            elif isinstance(item, dict):
                parts.append(str(item.get("text") or ""))
        return "".join(parts).strip()
    return ""


def text_features(text: str) -> dict[str, float]:
    lowered = text.casefold()
    tokens = re.findall(r"[a-zа-яё0-9]{2,}", lowered, flags=re.IGNORECASE)
    features: dict[str, float] = {}
    for token in tokens:
        add_feature(features, "w:" + token, 1.0)
    for first, second in zip(tokens, tokens[1:]):
        add_feature(features, f"b:{first}_{second}", 0.75)
    age = extract_age(text)
    if age is not None:
        add_feature(features, f"age:{age // 5 * 5}", 1.5)
    add_feature(features, f"len:{min(len(tokens) // 10, 20)}", 1.0)
    return features


def add_feature(features: dict[str, float], value: str, weight: float) -> None:
    digest = hashlib.blake2b(value.encode("utf-8"), digest_size=4).digest()
    bucket = int.from_bytes(digest, "little") % FEATURE_BUCKETS
    key = str(bucket)
    features[key] = features.get(key, 0.0) + weight


def as_int(value: Any, default: int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def default_model_path() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent / "data" / "taste_model.json"
    return Path(__file__).resolve().parent.parent / ".data" / "taste_model.json"
