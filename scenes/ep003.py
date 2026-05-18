"""Видео №3: «Почему в едущем автобусе подброшенная монетка падает в руку?»
Факты: относительность движения + инерция (школьная физика). Чисел нет.
"""
from __future__ import annotations
from manim import (
    Text, VGroup, Rectangle, Circle, Arrow, Dot,
    FadeIn, FadeOut, Create, GrowArrow,
    UP, DOWN, LEFT, RIGHT, BOLD,
)
import config
from core.scene_base import NarratedScene, FONT

ACC, FG, MUT = config.BRAND_ACCENT, config.BRAND_FG, config.BRAND_MUTED

NARRATION = [
    "Подбрось монетку в едущем автобусе. Она упадёт назад, ведь автобус "
    "уехал вперёд? Проверим.",
    "На самом деле монетка спокойно падает тебе обратно в руку.",
    "Пока монетка летела вверх, кажется, автобус должен «уехать» из-под неё.",
    "Но монетка вместе с тобой и автобусом уже двигалась вперёд с той же "
    "скоростью.",
    "В воздухе она по инерции сохраняет эту скорость — летит вперёд "
    "ровно как автобус.",
    "Поэтому относительно автобуса она просто поднимается и опускается — "
    "точно в руку.",
    "Это относительность движения: «движется или нет» зависит от того, "
    "откуда смотреть.",
    "Для тебя в автобусе монетка летит вверх и вниз. Для человека на "
    "остановке — по дуге вперёд.",
    "Тот же принцип: в самолёте ты спокойно ходишь по салону, хотя "
    "летишь сотни километров в час.",
    "Важно: так работает при ровном движении. Если автобус резко "
    "затормозит, монетка улетит вперёд.",
    "Итог: ты, монетка и автобус — одна движущаяся система.",
    "А где ты прямо сейчас не замечаешь огромную скорость, потому что "
    "движешься вместе со всем? Подсказка — под ногами. Пиши в комментариях.",
]


class Episode003(NarratedScene):
    narration = NARRATION
    episode_title = "Монетка в едущем автобусе"

    def _bus(self):
        body = Rectangle(width=4.0, height=1.8, color=ACC, stroke_width=5)
        w1 = Circle(radius=0.3, color=MUT, fill_opacity=1).set_fill(MUT)
        w2 = Circle(radius=0.3, color=MUT, fill_opacity=1).set_fill(MUT)
        w1.next_to(body, DOWN, 0).shift(LEFT * 1.2 + UP * 0.15)
        w2.next_to(body, DOWN, 0).shift(RIGHT * 1.2 + UP * 0.15)
        return VGroup(body, w1, w2)

    def beat_0(self):
        bus = self._bus().shift(DOWN * 0.3)
        coin = Circle(radius=0.16, color=FG, fill_opacity=1).set_fill(FG)
        coin.move_to(bus[0].get_center())
        mv = Arrow(bus.get_right(), bus.get_right() + RIGHT * 1.2,
                   color=MUT, buff=0.1)
        q = Text("Куда упадёт монетка?", font=FONT, color=FG,
                 weight=BOLD).scale(0.7).to_edge(UP, buff=1.0)
        self.play_for(FadeIn(q), Create(bus), FadeIn(coin), frac=0.4)
        self.play_for(GrowArrow(mv), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(q, bus, coin, mv)), frac=0.9)

    def beat_1(self):
        self.card("В руку!", "а не назад", color=ACC)

    def beat_2(self):
        self.card("Кажется:", "автобус «уедет» из-под монетки")

    def beat_3(self):
        self.card("Но монетка уже", "летит вперёд вместе с автобусом")

    def beat_4(self):
        self.card("Инерция", "монетка сохраняет скорость автобуса",
                  color=ACC)

    def beat_5(self):
        bus = self._bus().shift(DOWN * 0.3)
        hand = Dot(bus[0].get_center() + DOWN * 0.3, color=FG, radius=0.1)
        path = VGroup(
            Dot(bus[0].get_center() + DOWN * 0.3, color=ACC, radius=0.06),
            Dot(bus[0].get_center() + UP * 0.6, color=ACC, radius=0.06),
            Dot(bus[0].get_center() + DOWN * 0.3, color=ACC, radius=0.06),
        )
        cap = Text("вверх и вниз — в руку", font=FONT,
                   color=MUT).scale(0.45).to_edge(DOWN, buff=0.7)
        self.play_for(Create(bus), FadeIn(hand), frac=0.35)
        self.play_for(FadeIn(path), FadeIn(cap), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(bus, hand, path, cap)), frac=0.9)

    def beat_6(self):
        self.card("Относительность движения",
                  "всё зависит, откуда смотреть")

    def beat_7(self):
        left = Text("В автобусе:\nвверх-вниз", font=FONT, color=FG,
                    weight=BOLD).scale(0.55).shift(LEFT * 3.2)
        right = Text("С остановки:\nпо дуге вперёд", font=FONT, color=ACC,
                     weight=BOLD).scale(0.55).shift(RIGHT * 3.2)
        self.play_for(FadeIn(left), frac=0.4)
        self.play_for(FadeIn(right), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(left, right)), frac=0.9)

    def beat_8(self):
        self.card("В самолёте", "ходишь как по земле")

    def beat_9(self):
        self.card("Резкое торможение —", "монетка улетит вперёд",
                  color="#FF5252")

    def beat_10(self):
        self.card("Ты + монетка + автобус", "одна движущаяся система")

    def beat_11(self):
        a = Text("Где ты не чувствуешь\nогромную скорость?",
                 font=FONT, color=ACC, weight=BOLD).scale(0.62)
        a.to_edge(UP, buff=1.2)
        h = Text("подсказка: под ногами — Земля", font=FONT,
                 color=MUT).scale(0.5).next_to(a, DOWN, 0.5)
        cta = Text("Пиши · Следующий выпуск →", font=FONT,
                   color=MUT).scale(0.5).to_edge(DOWN, buff=1.0)
        self.play_for(FadeIn(a, shift=DOWN * 0.2), frac=0.4)
        self.play_for(FadeIn(h), FadeIn(cta), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(a, h, cta)), frac=0.9)
