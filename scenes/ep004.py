"""Видео №4: «Сила тяжести: почему мы не улетаем с Земли?»
Факт-чек:
- Скорость вращения Земли на экваторе ≈ 1670 км/ч (≈465 м/с) —
  Wikipedia «Earth's rotation», Universe Today.
- g ≈ 9,8 м/с² — NIST/CGPM 1901.
- Центростремительное ускорение на экваторе ≈ 0,034 м/с² (v²/R),
  то есть притяжение в сотни раз сильнее «отбрасывания» вращением.
"""
from __future__ import annotations
from manim import (
    Text, VGroup, Circle, Arrow, Dot,
    FadeIn, FadeOut, Create, GrowArrow,
    UP, DOWN, LEFT, RIGHT, BOLD,
)
import config
from core.scene_base import NarratedScene, FONT

ACC, FG, MUT = config.BRAND_ACCENT, config.BRAND_FG, config.BRAND_MUTED

NARRATION = [
    "Земля крутится — на экваторе со скоростью примерно тысяча шестьсот "
    "семьдесят километров в час. Почему нас не сбрасывает?",
    "Всё дело в силе тяжести. Она притягивает любые тела к центру Земли.",
    "Отпусти что угодно из рук — оно падает вниз, то есть к центру планеты.",
    "Вращение действительно немного «отбрасывает» наружу. Но этот эффект "
    "крошечный.",
    "Притяжение Земли в сотни раз сильнее этого отбрасывания.",
    "Поэтому мы, воздух и океаны надёжно удерживаемся на поверхности.",
    "Сила тяжести зависит от массы: чем массивнее тело, тем сильнее "
    "оно притягивает.",
    "У поверхности Земли тяготение разгоняет падение примерно на "
    "девять и восемь десятых метра в секунду каждую секунду.",
    "У тел со слабым притяжением газам трудно удержаться — атмосфера "
    "постепенно улетучивается в космос.",
    "Итог: нас держит не «прилипание», а притяжение к центру Земли.",
    "А как думаешь: человек весит чуть больше на полюсе или на экваторе? "
    "И почему? Напиши в комментариях и смотри следующий выпуск.",
]


class Episode004(NarratedScene):
    narration = NARRATION
    episode_title = "Почему мы не улетаем с Земли?"

    def _earth(self, r=1.7):
        e = Circle(radius=r, color=ACC, stroke_width=5)
        e.set_fill(ACC, opacity=0.12)
        return e

    def beat_0(self):
        e = self._earth().shift(DOWN * 0.2)
        spin = Arrow(e.get_top() + LEFT * 0.2, e.get_top() + RIGHT * 1.0,
                     color=MUT, buff=0)
        q = Text("≈ 1670 км/ч — и не сбрасывает?", font=FONT, color=FG,
                 weight=BOLD).scale(0.62).to_edge(UP, buff=0.9)
        self.play_for(FadeIn(q), Create(e), frac=0.4)
        self.play_for(GrowArrow(spin), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(q, e, spin)), frac=0.9)

    def beat_1(self):
        e = self._earth(1.4).shift(DOWN * 0.2)
        arrs = VGroup()
        for ang in (0.3, 1.4, 2.6, 3.7, 4.9, 5.7):
            import numpy as np
            d = np.array([np.cos(ang), np.sin(ang), 0.0])
            p = e.get_center() + d * 2.4
            arrs.add(Arrow(p, e.get_center() + d * 1.45, color=ACC, buff=0))
        lab = Text("СИЛА ТЯЖЕСТИ", font=FONT, color=ACC,
                   weight=BOLD).scale(0.55).to_edge(UP, buff=0.9)
        self.play_for(Create(e), FadeIn(lab), frac=0.35)
        self.play_for(*[GrowArrow(a) for a in arrs], frac=0.55)
        self.hold()
        self.play_for(FadeOut(VGroup(e, arrs, lab)), frac=0.9)

    def beat_2(self):
        self.card("Всё падает", "к центру Земли")

    def beat_3(self):
        self.card("Вращение «отбрасывает»", "но совсем чуть-чуть")

    def beat_4(self):
        big = Arrow(UP * 1.6, DOWN * 1.6, color=ACC, buff=0,
                    stroke_width=10).shift(LEFT * 1.5)
        small = Arrow(LEFT * 0.2, RIGHT * 0.35, color="#FF5252",
                      buff=0).shift(RIGHT * 1.8)
        l1 = Text("притяжение", font=FONT, color=ACC).scale(0.5)
        l1.next_to(big, LEFT, 0.2)
        l2 = Text("отбрасывание", font=FONT, color=MUT).scale(0.42)
        l2.next_to(small, DOWN, 0.25)
        self.play_for(GrowArrow(big), FadeIn(l1), frac=0.4)
        self.play_for(GrowArrow(small), FadeIn(l2), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(big, small, l1, l2)), frac=0.9)

    def beat_5(self):
        self.card("Мы, воздух, океаны", "надёжно держимся", color=ACC)

    def beat_6(self):
        self.card("Чем массивнее тело —", "тем сильнее притяжение")

    def beat_7(self):
        self.card("g ≈ 9,8 м/с²", "+9,8 м/с скорости каждую секунду",
                  color=ACC)

    def beat_8(self):
        self.card("Слабое притяжение —", "атмосфера улетучивается")

    def beat_9(self):
        self.card("Нас держит притяжение", "к центру Земли")

    def beat_10(self):
        a = Text("Где вес чуть больше:\nна полюсе или экваторе?",
                 font=FONT, color=ACC, weight=BOLD).scale(0.6)
        a.to_edge(UP, buff=1.3)
        cta = Text("Пиши · Следующий выпуск →", font=FONT,
                   color=MUT).scale(0.5).to_edge(DOWN, buff=1.0)
        self.play_for(FadeIn(a, shift=DOWN * 0.2), frac=0.4)
        self.play_for(FadeIn(cta), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(a, cta)), frac=0.9)
