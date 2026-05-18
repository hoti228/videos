"""ffmpeg без установки в систему: берём бинарь из пакета imageio-ffmpeg
и кладём копию как .bin\\ffmpeg.exe, чтобы и Manim, и наша склейка видели
один и тот же ffmpeg (на D:, C: не трогаем)."""
from __future__ import annotations
import shutil
from pathlib import Path
import config


def ensure_ffmpeg() -> str:
    """Гарантирует наличие d:\\ggpolole\\physics_channel\\.bin\\ffmpeg.exe.
    Возвращает абсолютный путь к нему (str)."""
    target = config.BIN / "ffmpeg.exe"
    if target.exists():
        return str(target)
    import imageio_ffmpeg
    src = Path(imageio_ffmpeg.get_ffmpeg_exe())
    config.BIN.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, target)
    return str(target)


def bin_dir() -> str:
    """Каталог с ffmpeg.exe — добавляем в PATH для дочерних процессов (Manim)."""
    ensure_ffmpeg()
    return str(config.BIN)
