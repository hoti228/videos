"""Видео №6: «Почему на Луне ты весишь в 6 раз меньше?»
Факт-чек: g_Луны ≈ 1,62 м/с² ≈ 1/6 земного (NASA NSSDC / Wikipedia
«Gravitation of the Moon»); g_Земли ≈ 9,8 (NIST).
Пример: 60 кг → ≈ 588 Н на Земле, ≈ 97 Н на Луне (числа выведены из
проверенных g; в озвучке округлены со словом «около»).
"""
from __future__ import annotations
from manim import (
    Text, VGroup, Circle, Arrow,
    FadeIn, FadeOut, Create, GrowArrow,
    UP, DOWN, LEFT, RIGHT, BOLD,
)
import config
from core.scene_base import NarratedScene, FONT

ACC, FG, MUT = config.BRAND_ACCENT, config.BRAND_FG, config.BRAND_MUTED

NARRATION = [
    "На Луне астронавты передвигаются гигантскими прыжками. Почему так "
    "легко?",
    "Притяжение Луны примерно в шесть раз слабее земного: около одной и "
    "шести десятых против девяти и восьми десятых метра в секунду "
    "за секунду.",
    "Масса тела не меняется. А вот вес — сила притяжения — на Луне "
    "в шесть раз меньше.",
    "Человек массой шестьдесят килограммов на Земле весит около "
    "пятисот девяноста ньютонов.",
    "На Луне тот же человек весит примерно сто ньютонов — будто по "
    "земным меркам в нём около десяти килограммов.",
    "Поэтому обычный шаг на Луне превращается в прыжок на пару метров.",
    "Почему притяжение слабее? Луна меньше и легче Земли.",
    "Сила тяжести зависит от массы небесного тела и расстояния до "
    "его центра.",
    "Но запомни из первого выпуска: при падении к поверхности молоток "
    "и перо там всё равно падают одинаково.",
    "Итог: на Луне меньше становишься не ты, а сила, которая тянет "
    "тебя вниз.",
    "Прикинь: во сколько раз выше ты подпрыгнул бы на Луне, чем на "
    "Земле? Напиши ответ в комментариях и смотри следующий выпуск.",
]


class Episode006(NarratedScene):
    narration = NARRATION
    episode_title = "Почему на Луне весишь в 6 раз меньше?"

    def beat_0(self):
        moon = Circle(radius=1.2, color=MUT, fill_opacity=0.25).set_fill(MUT)
        moon.shift(DOWN * 1.1)
        q = Text("Прыжки как у супергероя", font=FONT, color=FG,
                 weight=BOLD).scale(0.7).to_edge(UP, buff=1.0)
        self.play_for(FadeIn(q), FadeIn(moon, scale=1.2), frac=0.45)
        self.hold()
        self.play_for(FadeOut(VGroup(q, moon)), frac=0.9)

    def beat_1(self):
        self.card("Притяжение Луны", "≈ в 6 раз слабее (1,6 vs 9,8 м/с²)",
                  color=ACC)

    def beat_2(self):
        self.card("Масса та же —", "вес в 6 раз меньше")

    def beat_3(self):
        box = Text("60 кг", font=FONT, color=FG, weight=BOLD).scale(0.7)
        box.shift(UP * 1.2)
        arr = Arrow(box.get_bottom(), box.get_bottom() + DOWN * 2.0,
                    color=ACC, buff=0.1, stroke_width=10)
        f = Text("≈ 590 Н на Земле", font=FONT, color=ACC,
                 weight=BOLD).scale(0.6).next_to(arr, RIGHT, 0.3)
        self.play_for(FadeIn(box), frac=0.3)
        self.play_for(GrowArrow(arr), FadeIn(f), frac=0.55)
        self.hold()
        self.play_for(FadeOut(VGroup(box, arr, f)), frac=0.9)

    def beat_4(self):
        box = Text("60 кг", font=FONT, color=FG, weight=BOLD).scale(0.7)
        box.shift(UP * 1.2)
        arr = Arrow(box.get_bottom(), box.get_bottom() + DOWN * 0.7,
                    color=ACC, buff=0.1, stroke_width=10)
        f = Text("≈ 100 Н на Луне\n(как ~10 кг по-земному)", font=FONT,
                 color=ACC, weight=BOLD).scale(0.52).next_to(arr, RIGHT, 0.3)
        self.play_for(FadeIn(box), frac=0.3)
        self.play_for(GrowArrow(arr), FadeIn(f), frac=0.55)
        self.hold()
        self.play_for(FadeOut(VGroup(box, arr, f)), frac=0.9)

    def beat_5(self):
        self.card("Шаг → прыжок", "на пару метров", color=ACC)

    def beat_6(self):
        self.card("Луна меньше и легче", "поэтому притяжение слабее")

    def beat_7(self):
        self.card("Сила тяжести зависит от", "массы тела и расстояния")

    def beat_8(self):
        self.card("Но падают всё равно", "одинаково (выпуск №1)")

    def beat_9(self):
        self.card("Меньше не ты —", "меньше сила, тянущая вниз", color=ACC)

    def beat_10(self):
        a = Text("Во сколько раз выше\nпрыжок на Луне?",
                 font=FONT, color=ACC, weight=BOLD).scale(0.62)
        a.to_edge(UP, buff=1.3)
        cta = Text("Пиши · Следующий выпуск →", font=FONT,
                   color=MUT).scale(0.5).to_edge(DOWN, buff=1.0)
        self.play_for(FadeIn(a, shift=DOWN * 0.2), frac=0.4)
        self.play_for(FadeIn(cta), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(a, cta)), frac=0.9)
