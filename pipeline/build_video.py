"""Оркестратор сборки ролика:
  1) Silero: каждая фраза -> wav, замер длительности
  2) склейка озвучки в narration.wav (+ паузы), timing.json для Manim
  3) Manim рендерит сцену, подгоняя биты ровно под длину аудио
  4) ffmpeg: видео + озвучка -> финальный mp4
  5) .srt из текста и таймингов, обложка, metadata.json (SEO)

Запуск:  d:\ggpolole\.venv\Scripts\python.exe -m pipeline.build_video 001
"""
from __future__ import annotations
import importlib
import json
import os
import subprocess
import sys
from pathlib import Path

import config  # ПЕРВЫМ: кэши -> D:
import numpy as np
import soundfile as sf
from core import tts_silero
from core.ffmpeg_util import ensure_ffmpeg, bin_dir

EPISODES = {
    "001": ("scenes.ep001", "Episode001", "pochemu-vse-padaet-odinakovo"),
}


def _fmt_ts(t: float) -> str:
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = int(t % 60)
    ms = int(round((t - int(t)) * 1000))
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def _write_srt(lines, starts, ends, path: Path):
    out = []
    for i, (txt, a, b) in enumerate(zip(lines, starts, ends), 1):
        out.append(f"{i}\n{_fmt_ts(a)} --> {_fmt_ts(b)}\n{txt.strip()}\n")
    path.write_text("\n".join(out), encoding="utf-8")


def build(episode: str = "001"):
    mod_name, cls_name, slug = EPISODES[episode]
    mod = importlib.import_module(mod_name)
    narration: list[str] = list(getattr(mod, "NARRATION"))

    epdir = config.OUT / episode
    adir = epdir / "audio"
    adir.mkdir(parents=True, exist_ok=True)

    # --- 1) TTS по фразам ---
    sr = config.TTS_SR
    gap = np.zeros(int(sr * config.TTS_GAP), dtype=np.float32)
    durations, narr_dur, track = [], [], []
    for i, txt in enumerate(narration):
        w = adir / f"{i:03d}.wav"
        d = tts_silero.synthesize(txt, str(w))
        data, _ = sf.read(str(w), dtype="float32")
        narr_dur.append(d)
        durations.append(round(d + config.TTS_GAP, 3))  # бит = речь + пауза
        track.append(data)
        track.append(gap)
        print(f"[build] бит {i:02d}: {d:.2f}s  «{txt[:48]}...»")

    narration_wav = epdir / "narration.wav"
    sf.write(str(narration_wav), np.concatenate(track), sr, subtype="PCM_16")
    (epdir / "timing.json").write_text(json.dumps(durations), encoding="utf-8")

    # --- 2) субтитры (речь без пауз) ---
    starts, ends, t = [], [], 0.0
    for i in range(len(narration)):
        starts.append(t)
        ends.append(t + narr_dur[i])
        t += durations[i]
    _write_srt(narration, starts, ends, epdir / f"{episode}.srt")

    # --- 3) Manim ---
    ensure_ffmpeg()
    env = os.environ.copy()
    env["EPISODE_TIMING"] = str(epdir / "timing.json")
    env["PYTHONPATH"] = str(config.ROOT)
    env["PATH"] = bin_dir() + os.pathsep + env.get("PATH", "")
    scene_file = str(Path(mod.__file__))
    cmd = [
        sys.executable, "-m", "manim", "render",
        "--resolution", f"{config.VIDEO_W},{config.VIDEO_H}",
        "--fps", str(config.FPS), "-v", "WARNING",
        "--media_dir", str(config.MANIM_MEDIA),
        "--output_file", episode,
        scene_file, cls_name,
    ]
    print("[build] рендер Manim:", " ".join(cmd))
    subprocess.run(cmd, check=True, env=env, cwd=str(config.ROOT))

    vids = sorted(
        config.MANIM_MEDIA.glob(f"videos/**/{episode}.mp4"),
        key=lambda p: p.stat().st_mtime,
    )
    if not vids:
        vids = sorted(config.MANIM_MEDIA.glob("videos/**/*.mp4"),
                      key=lambda p: p.stat().st_mtime)
    if not vids:
        raise RuntimeError("Manim не выдал mp4")
    silent_video = vids[-1]

    # --- 4) видео + озвучка ---
    ff = ensure_ffmpeg()
    final = epdir / f"{episode}_{slug}.mp4"
    subprocess.run([
        ff, "-y", "-i", str(silent_video), "-i", str(narration_wav),
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-shortest", str(final),
    ], check=True)

    # --- 5) обложка + SEO ---
    from pipeline.make_thumbnail import make_thumbnail
    from pipeline.seo import generate_metadata
    thumb = make_thumbnail(episode)
    meta = generate_metadata(episode, sum(durations))

    print("\n=== ГОТОВО ===")
    print(f"видео:    {final}")
    print(f"обложка:  {thumb}")
    print(f"субтитры: {epdir / (episode + '.srt')}")
    print(f"метаданные: {meta}")
    print(f"длительность: {sum(durations):.1f} c")
    return final


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "001")
