"""metadata.json под алгоритмы YouTube: заголовки-варианты, описание с
ключами и таймкодами, теги, плейлист-серия. Цель — вовлечение, без продаж.
"""
from __future__ import annotations
import json
from pathlib import Path

import config
from pipeline.topics import get_topic

SERIES_PLAYLIST = {
    "A": "Движение и силы — физика для 7–8 класса",
    "B": "Давление, жидкости и газы — физика 7–8 класс",
    "C": "Тепло и температура — физика 7–8 класс",
    "D": "Электричество — физика 7–8 класс",
    "E": "Магнетизм — физика 7–8 класс",
    "F": "Свет и оптика — физика 7–8 класс",
    "G": "Звук и волны — физика 7–8 класс",
    "H": "Энергия и механизмы — физика 7–8 класс",
}


def generate_metadata(episode: str, duration_sec: float) -> Path:
    t = get_topic(episode)
    title = t.get("title", "Физика просто")
    titles = [title] + list(t.get("alt_titles", []))
    hook = t.get("hook", "")
    learn = t.get("learn", [])
    tags = t.get("tags", [])
    series = t.get("series", "A")

    desc = []
    desc.append(hook or title)
    desc.append(f"Физика для 7–8 класса за {int(duration_sec // 60)}–"
                f"{int(duration_sec // 60) + 1} минут — коротко, наглядно, "
                f"с проверенными фактами.")
    desc.append("")
    if learn:
        desc.append("Что ты поймёшь из этого видео:")
        desc += [f"• {x}" for x in learn]
        desc.append("")
    desc.append("Все числа и факты в ролике перепроверены по первоисточникам "
                "(NASA, NIST и др.).")
    desc.append("")
    desc.append("💬 Ответь на вопрос в конце видео в комментариях — "
                "это реально помогает каналу.")
    desc.append("🔔 Подпишись, чтобы не пропустить следующий выпуск.")
    desc.append("")
    desc.append("#физика #наука #школа #7класс #8класс #образование")

    meta = {
        "episode": episode,
        "title_variants": titles,           # для A/B по CTR
        "title": titles[0],
        "description": "\n".join(desc),
        "tags": tags,
        "category": "Education",
        "language": "ru",
        "default_audio_language": "ru",
        "playlist": SERIES_PLAYLIST.get(series, ""),
        "made_for_kids": False,
        "thumbnail_text": t.get("thumb", title),
        "duration_sec": round(duration_sec, 1),
        "publish_notes": [
            "Загрузить .srt как субтитры (ru) — это плюс к SEO и досмотру.",
            "Добавить видео в плейлист серии (см. поле playlist).",
            "Конечная заставка: следующий выпуск серии + кнопка подписки.",
            "Закрепить комментарий с вопросом из концовки.",
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
    print(generate_metadata(sys.argv[1] if len(sys.argv) > 1 else "001", 240))
