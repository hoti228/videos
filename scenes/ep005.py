"""Видео №5: «Чем масса отличается от веса?»
Факт-чек: вес = m·g; g_Земли ≈ 9,8 м/с² (NIST); g_Луны ≈ 1/6 земного
(NASA/Wikipedia). 1 кг → ≈ 9,8 Н.
"""
from __future__ import annotations
from manim import (
    Text, VGroup, Square, Arrow,
    FadeIn, FadeOut, GrowArrow,
    UP, DOWN, LEFT, RIGHT, BOLD,
)
import config
from core.scene_base import NarratedScene, FONT

ACC, FG, MUT = config.BRAND_ACCENT, config.BRAND_FG, config.BRAND_MUTED

NARRATION = [
    "«Сколько ты весишь?» — вопрос с подвохом. Масса и вес — это разные "
    "вещи.",
    "Масса — это количество вещества в теле. Она не меняется нигде: "
    "ни на Земле, ни на Луне, ни в космосе.",
    "Вес — это сила, с которой тело давит на опору или растягивает "
    "подвес из-за притяжения.",
    "Массу измеряют в килограммах. Вес — это сила, поэтому в ньютонах.",
    "Связь простая: вес равен массе, умноженной на g. У Земли "
    "g примерно девять и восемь десятых.",
    "Значит, тело массой один килограмм давит на опору с силой "
    "примерно девять и восемь десятых ньютона.",
    "На Луне притяжение в шесть раз слабее: масса та же, а вес — "
    "в шесть раз меньше.",
    "В свободном падении или на орбите вес может стать нулевым — это "
    "невесомость. А масса при этом никуда не девается.",
    "Поэтому «похудеть», слетав на Луну, не выйдет: уменьшится вес, "
    "а не масса.",
    "Итог: масса — сколько в теле вещества; вес — с какой силой его "
    "тянет вниз.",
    "А как думаешь: в лифте, который резко поехал вниз, твой вес "
    "больше или меньше? Напиши в комментариях и смотри следующий выпуск.",
]


class Episode005(NarratedScene):
    narration = NARRATION
    episode_title = "Масса и вес — это разное"

    def beat_0(self):
        self.card("Масса ≠ Вес", "вопрос с подвохом", color=ACC)

    def beat_1(self):
        self.card("МАССА", "сколько вещества — не меняется нигде")

    def beat_2(self):
        self.card("ВЕС", "сила давления на опору", color=ACC)

    def beat_3(self):
        left = Text("масса\n→ килограммы", font=FONT, color=FG,
                    weight=BOLD).scale(0.6).shift(LEFT * 3.0)
        right = Text("вес\n→ ньютоны", font=FONT, color=ACC,
                     weight=BOLD).scale(0.6).shift(RIGHT * 3.0)
        self.play_for(FadeIn(left), frac=0.4)
        self.play_for(FadeIn(right), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(left, right)), frac=0.9)

    def beat_4(self):
        self.card("Вес = масса × g", "у Земли g ≈ 9,8", color=ACC)

    def beat_5(self):
        box = Square(side_length=1.2, color=FG, fill_opacity=1).set_fill(FG)
        box.shift(UP * 0.4)
        lbl = Text("1 кг", font=FONT, color=config.BRAND_BG,
                   weight=BOLD).scale(0.5).move_to(box.get_center())
        arr = Arrow(box.get_bottom(), box.get_bottom() + DOWN * 1.6,
                    color=ACC, buff=0)
        f = Text("≈ 9,8 Н", font=FONT, color=ACC,
                 weight=BOLD).scale(0.6).next_to(arr, RIGHT, 0.3)
        self.play_for(FadeIn(box), FadeIn(lbl), frac=0.35)
        self.play_for(GrowArrow(arr), FadeIn(f), frac=0.55)
        self.hold()
        self.play_for(FadeOut(VGroup(box, lbl, arr, f)), frac=0.9)

    def beat_6(self):
        self.card("На Луне", "масса та же, вес в 6 раз меньше", color=ACC)

    def beat_7(self):
        self.card("Невесомость", "вес = 0, а масса остаётся")

    def beat_8(self):
        self.card("Полёт на Луну", "уменьшит вес, а не массу")

    def beat_9(self):
        self.card("Масса — сколько вещества", "Вес — с какой силой тянет")

    def beat_10(self):
        a = Text("Лифт резко вниз:\nвес больше или меньше?",
                 font=FONT, color=ACC, weight=BOLD).scale(0.62)
        a.to_edge(UP, buff=1.3)
        cta = Text("Пиши · Следующий выпуск →", font=FONT,
                   color=MUT).scale(0.5).to_edge(DOWN, buff=1.0)
        self.play_for(FadeIn(a, shift=DOWN * 0.2), frac=0.4)
        self.play_for(FadeIn(cta), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(a, cta)), frac=0.9)
