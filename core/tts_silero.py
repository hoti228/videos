"""Silero TTS: текст -> wav. Офлайн, бесплатно, GPU (GTX 1050 Ti) с
автоматическим откатом на CPU, если CUDA-ядро недоступно для Pascal.

Импортируем config ПЕРВЫМ — он ставит TORCH_HOME на D: до импорта torch.
"""
from __future__ import annotations
import re
import config  # noqa: F401  (должен быть до torch — задаёт TORCH_HOME на D:)
import numpy as np
import soundfile as sf
import torch

_model = None
_device = "cpu"


def _pick_device() -> str:
    if not torch.cuda.is_available():
        return "cpu"
    try:
        # GTX 1050 Ti = Pascal sm_61: проверяем, что ядро реально работает
        t = torch.zeros(8, device="cuda")
        _ = (t + 1).sum().item()
        torch.cuda.synchronize()
        return "cuda"
    except Exception as e:  # noqa: BLE001
        print(f"[tts] CUDA недоступна для вычислений ({e}); работаем на CPU")
        return "cpu"


def _load() -> None:
    global _model, _device
    if _model is not None:
        return
    _device = _pick_device()
    print(f"[tts] устройство: {_device}")
    model, _ = torch.hub.load(
        repo_or_dir="snakers4/silero-models",
        model="silero_tts",
        language=config.TTS_LANG,
        speaker=config.TTS_MODEL,
        trust_repo=True,
    )
    model.to(torch.device(_device))
    _model = model


_SENT_SPLIT = re.compile(r"(?<=[.!?…])\s+")


def synthesize(text: str, out_path: str) -> float:
    """Озвучивает text, пишет 16-бит PCM WAV в out_path.
    Возвращает длительность в секундах."""
    _load()
    text = " ".join(text.split()).strip()
    # Silero v4 ограничивает длину запроса — режем длинные биты по предложениям
    chunks, buf = [], ""
    for s in _SENT_SPLIT.split(text):
        if len(buf) + len(s) > 800 and buf:
            chunks.append(buf.strip())
            buf = s
        else:
            buf = (buf + " " + s).strip()
    if buf:
        chunks.append(buf)

    pieces = []
    for ch in chunks:
        try:
            audio = _model.apply_tts(
                text=ch, speaker=config.TTS_SPEAKER,
                sample_rate=config.TTS_SR, put_accent=True, put_yo=True,
            )
        except Exception as e:  # noqa: BLE001 — на CPU не падаем из-за GPU
            print(f"[tts] откат на CPU из-за: {e}")
            _model.to(torch.device("cpu"))
            audio = _model.apply_tts(
                text=ch, speaker=config.TTS_SPEAKER,
                sample_rate=config.TTS_SR, put_accent=True, put_yo=True,
            )
        pieces.append(audio.detach().cpu().numpy().astype(np.float32))
        pieces.append(np.zeros(int(config.TTS_SR * 0.18), dtype=np.float32))

    wav = np.concatenate(pieces) if pieces else np.zeros(1, dtype=np.float32)
    peak = float(np.max(np.abs(wav))) or 1.0
    wav = (wav / peak) * 0.95  # нормализация громкости
    sf.write(out_path, wav, config.TTS_SR, subtype="PCM_16")
    return len(wav) / config.TTS_SR


if __name__ == "__main__":
    import sys
    d = synthesize(
        "Проверка голоса Силеро. Физика — это интересно!",
        sys.argv[1] if len(sys.argv) > 1 else "tts_test.wav",
    )
    print(f"OK: {d:.2f} c, устройство {_device}")
