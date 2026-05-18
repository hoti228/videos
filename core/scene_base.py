"""Базовая Manim-сцена с синхронизацией под озвучку.

Идея: оркестратор сначала генерирует TTS по фразам и пишет JSON с
длительностями (env EPISODE_TIMING). Сцена читает их и подгоняет каждый
"бит" ровно под длину его аудио -> голос и картинка идут синхронно.
"""
from __future__ import annotations
import json
import os
from pathlib import Path

from manim import (
    Scene, Text, VGroup, FadeIn, FadeOut, ORIGIN, UP, DOWN, DR, BOLD,
)
import config

FONT = "Arial"  # на Windows есть кириллица; Manim/Pango ищет по имени семьи


class NarratedScene(Scene):
    narration: list[str] = []
    episode_title: str = ""

    def setup(self):
        self.camera.background_color = config.BRAND_BG
        tp = os.environ.get("EPISODE_TIMING")
        if tp and Path(tp).exists():
            self._dur = json.loads(Path(tp).read_text(encoding="utf-8"))
        else:  # превью без озвучки — по 4 c на бит
            self._dur = [4.0] * len(self.narration)
        self._bi = 0
        self._spent = 0.0

    def construct(self):
        self._brand_corner()
        for i in range(len(self.narration)):
            self._bi = i
            self._spent = 0.0
            getattr(self, f"beat_{i}")()
            self._end_beat()
            self._reset_stage()  # чистим сцену перед след. битом (жёсткая склейка)

    def _reset_stage(self):
        for m in list(self.mobjects):
            if m is not getattr(self, "_tag", None):
                self.remove(m)

    # ---- бюджет времени бита ----
    @property
    def budget(self) -> float:
        return float(self._dur[self._bi]) if self._bi < len(self._dur) else 4.0

    def left(self) -> float:
        return max(0.0, self.budget - self._spent)

    def play_for(self, *anims, seconds=None, frac=0.7, **kw):
        """Проигрывает анимации, не вылезая за остаток бюджета бита."""
        lft = self.left()
        if lft <= 0.05:
            for a in anims:
                m = getattr(a, "mobject", None)
                if m is not None:
                    self.add(m)
            return
        rt = seconds if seconds is not None else lft * frac
        rt = max(0.3, min(rt, lft))
        self.play(*anims, run_time=rt, **kw)
        self._spent += rt

    def hold(self, seconds=None):
        t = seconds if seconds is not None else self.left()
        if t and t > 0.01:
            self.wait(t)
            self._spent += t

    def _end_beat(self):
        r = self.budget - self._spent
        if r > 0.02:
            self.wait(r)  # добиваем бит ровно до длины его аудио

    # ---- бренд ----
    def _brand_corner(self):
        tag = Text(config.CHANNEL_NAME, font=FONT, color=config.BRAND_MUTED,
                   weight=BOLD).scale(0.28).to_corner(DR, buff=0.25)
        self.add(tag)
        self._tag = tag

    def title_card(self, text, sub=None, frac=0.45):
        t = Text(text, font=FONT, color=config.BRAND_FG, weight=BOLD).scale(0.72)
        grp = VGroup(t).move_to(ORIGIN)
        if sub:
            s = Text(sub, font=FONT, color=config.BRAND_ACCENT).scale(0.42)
            s.next_to(t, DOWN, buff=0.35)
            grp.add(s)
        self.play_for(FadeIn(grp, shift=UP * 0.3), frac=frac)
        self.hold()
        self.play_for(FadeOut(grp), frac=0.95)

    def card(self, big, small=None, big_scale=0.8, color=None, frac=0.4):
        """Универсальный кадр: крупное слово/мысль + подпись. Авто-уместить."""
        t = Text(big, font=FONT, color=(color or config.BRAND_FG),
                 weight=BOLD).scale(big_scale)
        grp = VGroup(t)
        if small:
            s = Text(small, font=FONT, color=config.BRAND_MUTED).scale(0.5)
            s.next_to(t, DOWN, buff=0.45)
            grp.add(s)
        grp.move_to(ORIGIN)
        if grp.width > 12.5:
            grp.scale(12.5 / grp.width)
        self.play_for(FadeIn(grp, shift=UP * 0.25), frac=frac)
        self.hold()
        self.play_for(FadeOut(grp), frac=0.92)
