"""Видео №9: «Что такое скорость и как её измеряют?»
Факт-чек:
- v = путь / время; 1 м/с = 3,6 км/ч (точно).
- Скорость звука в воздухе ≈ 343 м/с при 20 °C (Wikipedia «Speed of
  sound», Physics LibreTexts) — в озвучке «примерно 340 м/с».
- Скорость света ≈ 300 000 км/с (точно 299 792 458 м/с) — мировая
  константа; в озвучке «около 300 000 км/с».
- Пешеход ≈ 5 км/ч — типичная оценка (со словом «примерно»).
"""
from __future__ import annotations
from manim import (
    Text, VGroup, Line, Dot,
    FadeIn, FadeOut, Create,
    UP, DOWN, LEFT, RIGHT, BOLD,
)
import config
from core.scene_base import NarratedScene, FONT

ACC, FG, MUT = config.BRAND_ACCENT, config.BRAND_FG, config.BRAND_MUTED

NARRATION = [
    "Что такое скорость на самом деле — и как её измерить?",
    "Скорость показывает, какое расстояние тело проходит за единицу "
    "времени.",
    "Формула простая: скорость равна пути, делённому на время.",
    "Прошёл десять метров за две секунды — значит, скорость пять "
    "метров в секунду.",
    "Измеряют скорость в метрах в секунду или в километрах в час.",
    "Чтобы из метров в секунду получить километры в час, умножь "
    "на три и шесть десятых.",
    "Для сравнения: пешеход идёт примерно пять километров в час, "
    "машина в городе — около шестидесяти.",
    "Звук в воздухе летит примерно триста сорок метров в секунду.",
    "А свет — около трёхсот тысяч километров в секунду. Быстрее во "
    "Вселенной ничего не бывает.",
    "Скорость бывает средняя — за всю поездку, и мгновенная — та, "
    "что прямо сейчас показывает спидометр.",
    "Итог: скорость — это путь, делённый на время; единицы и перевод "
    "решают половину задач.",
    "А как думаешь: спидометр показывает мгновенную скорость или "
    "среднюю? Напиши в комментариях и смотри следующий выпуск.",
]


class Episode009(NarratedScene):
    narration = NARRATION
    episode_title = "Что такое скорость?"

    def beat_0(self):
        self.card("СКОРОСТЬ", "что это и как измерить", color=ACC)

    def beat_1(self):
        self.card("Расстояние", "за единицу времени")

    def beat_2(self):
        self.card("v = путь / время", "главная формула", color=ACC)

    def beat_3(self):
        track = Line(LEFT * 4 + DOWN * 0.5, RIGHT * 4 + DOWN * 0.5,
                     color=MUT, stroke_width=5)
        d = Dot(track.get_left(), color=ACC, radius=0.16)
        cap = Text("10 м за 2 с → 5 м/с", font=FONT, color=FG,
                   weight=BOLD).scale(0.6).to_edge(UP, buff=1.1)
        self.play_for(Create(track), FadeIn(d), FadeIn(cap), frac=0.3)
        self.play_for(d.animate.move_to(track.get_right()), frac=0.45)
        self.hold()
        self.play_for(FadeOut(VGroup(track, d, cap)), frac=0.9)

    def beat_4(self):
        self.card("Единицы", "м/с  или  км/ч")

    def beat_5(self):
        self.card("м/с → км/ч", "умножь на 3,6", color=ACC)

    def beat_6(self):
        self.card("Пешеход ≈ 5 км/ч", "машина в городе ≈ 60 км/ч")

    def beat_7(self):
        self.card("Звук", "≈ 340 м/с в воздухе", color=ACC)

    def beat_8(self):
        self.card("Свет ≈ 300 000 км/с", "быстрее ничего не бывает",
                  color=ACC)

    def beat_9(self):
        left = Text("средняя\n(за всю поездку)", font=FONT, color=FG,
                    weight=BOLD).scale(0.55).shift(LEFT * 3.2)
        right = Text("мгновенная\n(спидометр сейчас)", font=FONT,
                     color=ACC, weight=BOLD).scale(0.55).shift(RIGHT * 3.2)
        self.play_for(FadeIn(left), frac=0.4)
        self.play_for(FadeIn(right), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(left, right)), frac=0.9)

    def beat_10(self):
        self.card("Скорость = путь / время", "единицы решают ползадачи")

    def beat_11(self):
        a = Text("Спидометр: мгновенная\nили средняя?", font=FONT,
                 color=ACC, weight=BOLD).scale(0.62).to_edge(UP, buff=1.3)
        cta = Text("Пиши · Следующий выпуск →", font=FONT,
                   color=MUT).scale(0.5).to_edge(DOWN, buff=1.0)
        self.play_for(FadeIn(a, shift=DOWN * 0.2), frac=0.4)
        self.play_for(FadeIn(cta), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(a, cta)), frac=0.9)
