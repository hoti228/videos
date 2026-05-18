"""Доступ к плану из content/topics.yaml (100 тем, 8 серий)."""
from __future__ import annotations
import functools

import yaml
import config

_TOPICS_FILE = config.CONTENT / "topics.yaml"


@functools.lru_cache(maxsize=1)
def _load() -> dict:
    data = yaml.safe_load(_TOPICS_FILE.read_text(encoding="utf-8"))
    return {str(t["id"]).zfill(3): t for t in data["videos"]}


def get_topic(episode: str) -> dict:
    return _load().get(str(episode).zfill(3), {})


def all_topics() -> list[dict]:
    return list(_load().values())


def series_of(episode: str) -> str:
    return get_topic(episode).get("series", "")
