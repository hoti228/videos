"""Обложка (1280x720) на Pillow. Высокий контраст, крупный текст, единый
стиль — это главный рычаг CTR (кликабельности) у нового канала.
"""
from __future__ import annotations
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
import config
from pipeline.topics import get_topic

W, H = 1280, 720
_FONTS = [
    r"C:\Windows\Fonts\arialbd.ttf",
    r"C:\Windows\Fonts\Arial.ttf",
]


def _font(size: int):
    for f in _FONTS:
        if Path(f).exists():
            return ImageFont.truetype(f, size)
    return ImageFont.load_default()


def _wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def make_thumbnail(episode: str) -> Path:
    topic = get_topic(episode)
    title = topic.get("thumb", topic.get("title", "ФИЗИКА")).upper()

    img = Image.new("RGB", (W, H), config.BRAND_BG)
    d = ImageDraw.Draw(img)

    # акцентная полоса слева
    d.rectangle([0, 0, 24, H], fill=config.BRAND_ACCENT)
    # «молоток» и «перо» — простые силуэты-намёки справа
    d.rectangle([980, 250, 1180, 310], fill=config.BRAND_MUTED)        # боёк
    d.rectangle([1065, 310, 1095, 470], fill="#7A5230")               # ручка
    d.ellipse([1110, 360, 1210, 460], outline=config.BRAND_ACCENT, width=10)

    big = _font(110)
    lines = _wrap(d, title, big, 900)
    y = (H - len(lines) * 124) // 2 - 20
    for ln in lines:
        d.text((70, y), ln, font=big, fill=config.BRAND_FG,
                stroke_width=6, stroke_fill="#000000")
        y += 124

    small = _font(40)
    d.text((70, H - 80), config.CHANNEL_NAME.upper(), font=small,
           fill=config.BRAND_ACCENT)

    out = config.OUT / episode / f"{episode}_thumbnail.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, "PNG")
    return out


if __name__ == "__main__":
    import sys
    print(make_thumbnail(sys.argv[1] if len(sys.argv) > 1 else "001"))
