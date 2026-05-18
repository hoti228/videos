"""Центральная конфигурация канала.

ВАЖНО: импортируйте `config` ПЕРВЫМ (до torch/manim) — он перенаправляет все
кэши и временные файлы на диск D:, потому что на C: свободно ~2 ГБ.
"""
from __future__ import annotations
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent            # d:\ggpolole\physics_channel
DRIVE_ROOT = ROOT.parent                          # d:\ggpolole
CACHE = DRIVE_ROOT / ".cache"
TMP = DRIVE_ROOT / ".tmp"
MANIM_MEDIA = DRIVE_ROOT / ".manim_media"

# --- всё тяжёлое строго на D: (C: переполнен) ---
os.environ.setdefault("TORCH_HOME", str(CACHE / "torch"))
os.environ.setdefault("HF_HOME", str(CACHE / "hf"))
os.environ.setdefault("TMP", str(TMP))
os.environ.setdefault("TEMP", str(TMP))
for _p in (CACHE / "torch", CACHE / "hf", TMP, MANIM_MEDIA):
    _p.mkdir(parents=True, exist_ok=True)

# --- структура проекта ---
CONTENT = ROOT / "content"
SCRIPTS = CONTENT / "scripts"
OUT = ROOT / "out"
BIN = ROOT / ".bin"
for _p in (CONTENT, SCRIPTS, OUT, BIN):
    _p.mkdir(parents=True, exist_ok=True)

# --- видео ---
VIDEO_W, VIDEO_H, FPS = 1920, 1080, 30

# --- озвучка (Silero, офлайн, GPU c fallback на CPU) ---
TTS_LANG = "ru"
TTS_MODEL = "v4_ru"          # последняя русская модель Silero
TTS_SPEAKER = "baya"         # тёплый чёткий женский голос (подходит для обучения)
TTS_SR = 48000               # 48 кГц
TTS_GAP = 0.35               # пауза между фразами, сек

# --- бренд (единый стиль = выше CTR и узнаваемость) ---
BRAND_BG = "#0B1E3A"         # глубокий синий
BRAND_ACCENT = "#FFC400"     # жёлтый акцент
BRAND_FG = "#FFFFFF"
BRAND_MUTED = "#9FB3C8"
CHANNEL_NAME = "Физика за 5 минут"
