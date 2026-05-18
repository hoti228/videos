"""Собирает out/_CATALOG.md — готовые заголовки, описания, теги и пути
к файлам для ручной загрузки на YouTube (по всем готовым видео).
Запуск: python -m pipeline.catalog
"""
from __future__ import annotations
import json

import config


def build() -> str:
    rows = []
    for md in sorted(config.OUT.glob("*/metadata.json")):
        m = json.loads(md.read_text(encoding="utf-8"))
        d = md.parent
        ep = m.get("episode", d.name)
        mp4 = next(iter(sorted(d.glob(f"{ep}_*.mp4"))), None)
        rows.append((ep, m, d, mp4))

    out = ["# Каталог видео — для загрузки на YouTube",
           "",
           f"Готово роликов: {len(rows)}. "
           "Скопируй заголовок и описание при заливке; добавь .srt как "
           "субтитры, поставь обложку, закрепи комментарий.", ""]
    for ep, m, d, mp4 in rows:
        out += [
            f"## №{ep} — {m['title']}",
            "",
            f"- Видео: `{mp4 if mp4 else d}`",
            f"- Обложка: `{d / (ep + '_thumbnail.png')}`",
            f"- Субтитры: `{d / (ep + '.srt')}`",
            f"- Плейлист: {m.get('playlist','')}",
            "",
            "**Заголовок (варианты для A/B):**",
        ]
        out += [f"{i+1}. {t}" for i, t in enumerate(m.get("title_variants", []))]
        out += [
            "",
            "**Описание:**",
            "```",
            m.get("description", ""),
            "```",
            f"**Закреплённый комментарий:** {m.get('pinned_comment','')}",
            "",
            f"**Теги:** {', '.join(m.get('tags', []))}",
            "",
            "---",
            "",
        ]
    text = "\n".join(out)
    p = config.OUT / "_CATALOG.md"
    p.write_text(text, encoding="utf-8")
    return str(p)


if __name__ == "__main__":
    print(build())
