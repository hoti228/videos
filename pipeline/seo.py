"""metadata.json под алгоритмы YouTube: заголовки-варианты + структурное
описание (хук в 1-й строке, польза, проверка фактов, вопрос для
комментариев, подписка, плейлист, хэштеги). Цель — вовлечение, без продаж.
"""
from __future__ import annotations
import json
import re

import config
from pipeline.topics import get_topic

SERIES_PLAYLIST = {
    "A": "Движение и силы — физика 7–8 класс",
    "B": "Давление, жидкости и газы — физика 7–8 класс",
    "C": "Тепло и температура — физика 7–8 класс",
    "D": "Электричество — физика 7–8 класс",
    "E": "Магнетизм — физика 7–8 класс",
    "F": "Свет и оптика — физика 7–8 класс",
    "G": "Звук и волны — физика 7–8 класс",
    "H": "Энергия и механизмы — физика 7–8 класс",
}

# Короткий релевантный список — мусорные теги вредят ранжированию.
BASE_TAGS = ["физика", "физика для детей", "физика 7 класс",
             "физика 8 класс", "наука простым языком", "образование"]
HASHTAGS = "#физика #наука #школа #7класс #8класс #образование"


def _clip(s: str, n: int) -> str:
    s = s.strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def _title_variants(title: str, alt: list[str]) -> list[str]:
    core = title.rstrip("?！!.").strip()
    cand = [title] + list(alt) + [
        f"{core} — простыми словами",
        f"{title} | Физика за 5 минут",
        f"{core}? Физика 7–8 класс за 5 минут",
    ]
    out, seen = [], set()
    for c in cand:
        c = _clip(c, 90)
        k = c.lower()
        if c and k not in seen:
            seen.add(k)
            out.append(c)
    return out[:4]


def generate_metadata(episode: str, duration_sec: float):
    t = get_topic(episode)
    title = t.get("title", "Физика просто")
    hook = t.get("hook", title)
    learn = t.get("learn", [])
    tags = list(t.get("tags", [])) + BASE_TAGS
    tags = list(dict.fromkeys(t.strip() for t in tags if t.strip()))[:15]
    series = t.get("series", "A")
    comment_q = t.get("comment_q", "А как думаешь — каким будет ответ? "
                      "Напиши в комментариях 👇")
    mins = max(2, round(duration_sec / 60))

    d = []
    d.append(_clip(hook, 150))                      # 1-я строка — ключевая
    d.append(f"Физика для 7–8 класса за ~{mins} мин: коротко, наглядно "
             f"и с проверенными фактами.")
    d.append("")
    if learn:
        d.append("🔎 В этом выпуске:")
        d += [f" • {x}" for x in learn]
        d.append("")
    d.append("✅ Все числа и факты перепроверены по первоисточникам "
             "(NASA, NIST, научные публикации).")
    d.append("")
    d.append(f"💬 {comment_q}")
    d.append("🔔 Подпишись — новые выпуски по физике регулярно. "
             "Это лучшее видео, чтобы начать понимать физику с нуля.")
    d.append("")
    d.append(f"▶ Серия: {SERIES_PLAYLIST.get(series, '')}")
    d.append("")
    d.append(HASHTAGS)

    meta = {
        "episode": episode,
        "title": _clip(title, 90),
        "title_variants": _title_variants(title, t.get("alt_titles", [])),
        "description": "\n".join(d),
        "tags": tags,
        "category": "Education",
        "language": "ru",
        "default_audio_language": "ru",
        "playlist": SERIES_PLAYLIST.get(series, ""),
        "made_for_kids": False,
        "thumbnail_text": t.get("thumb", title),
        "pinned_comment": comment_q,
        "duration_sec": round(duration_sec, 1),
        "publish_notes": [
            "Заголовок: протестировать 2–3 варианта из title_variants по CTR.",
            "Загрузить .srt как субтитры (ru) — плюс к SEO и досмотру.",
            "Добавить в плейлист серии (поле playlist).",
            "Конечная заставка: следующий выпуск серии + кнопка подписки.",
            "Закрепить pinned_comment первым комментарием.",
            "Первые 1–2 часа отвечать на комментарии — важный сигнал.",
        ],
    }
    out = config.OUT / episode / "metadata.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(meta, ensure_ascii=False, indent=2),
                    encoding="utf-8")
    return out


if __name__ == "__main__":
    import sys
    print(generate_metadata(sys.argv[1] if len(sys.argv) > 1 else "001", 130))
