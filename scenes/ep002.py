"""Видео №2: «Что такое инерция и почему вас бросает вперёд при торможении?»
Факты: 1-й закон Ньютона (школьная физика, Пёрышкин 7 кл) — числа не нужны.
"""
from __future__ import annotations
from manim import (
    Text, VGroup, Rectangle, Circle, Arrow, Line,
    FadeIn, FadeOut, Create, GrowArrow,
    UP, DOWN, LEFT, RIGHT, BOLD,
)
import config
from core.scene_base import NarratedScene, FONT

ACC, FG, MUT = config.BRAND_ACCENT, config.BRAND_FG, config.BRAND_MUTED

NARRATION = [
    "В автобусе резко нажали на тормоз — и тебя бросило вперёд. "
    "Почему так происходит?",
    "Это инерция: любое тело стремится сохранять свою скорость.",
    "Первый закон Ньютона: если силы на тело уравновешены, оно покоится "
    "или движётся равномерно и прямолинейно.",
    "Ты ехал вместе с автобусом. Автобус затормозил, а ты по инерции "
    "продолжаешь двигаться вперёд с прежней скоростью.",
    "Когда автобус резко трогается — наоборот: тело «отстаёт», и тебя "
    "вжимает в спинку кресла.",
    "Опыт: карточка на стакане, на ней монетка. Резко щёлкни карту — "
    "монетка не улетит с ней, а упадёт в стакан. Это инерция покоя.",
    "Чем больше масса тела, тем больше его инертность — тем труднее "
    "изменить его скорость.",
    "Поэтому гружёный грузовик тормозит дольше, чем пустой.",
    "Именно из-за инерции нужен ремень безопасности: при ударе тело "
    "продолжает лететь вперёд.",
    "Итог: инерция — свойство сохранять скорость. Изменить её может "
    "только сила.",
    "А как думаешь: почему в метро тебя качает, когда поезд трогается "
    "и когда тормозит? Напиши в комментариях и смотри следующий выпуск.",
]


def _bus(scale=1.0):
    body = Rectangle(width=3.0, height=1.3, color=ACC, stroke_width=5)
    w1 = Circle(radius=0.25, color=MUT, fill_opacity=1).set_fill(MUT)
    w2 = Circle(radius=0.25, color=MUT, fill_opacity=1).set_fill(MUT)
    w1.next_to(body, DOWN, buff=0).shift(LEFT * 0.9 + UP * 0.12)
    w2.next_to(body, DOWN, buff=0).shift(RIGHT * 0.9 + UP * 0.12)
    return VGroup(body, w1, w2).scale(scale)


class Episode002(NarratedScene):
    narration = NARRATION
    episode_title = "Что такое инерция?"

    def beat_0(self):
        bus = _bus(1.0).shift(DOWN * 0.4)
        p = Circle(radius=0.28, color=FG, fill_opacity=1).set_fill(FG)
        p.move_to(bus[0].get_center())
        arr = Arrow(p.get_center(), p.get_center() + RIGHT * 1.6,
                    color="#FF5252", buff=0)
        q = Text("Почему бросает вперёд?", font=FONT, color=FG,
                 weight=BOLD).scale(0.7).to_edge(UP, buff=1.0)
        self.play_for(FadeIn(q), Create(bus), FadeIn(p), frac=0.4)
        self.play_for(GrowArrow(arr), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(q, bus, p, arr)), frac=0.9)

    def beat_1(self):
        self.card("ИНЕРЦИЯ", "тело сохраняет свою скорость", color=ACC)

    def beat_2(self):
        self.card("1-й закон Ньютона",
                  "нет силы → покой или равномерное движение")

    def beat_3(self):
        bus = _bus(1.0).shift(DOWN * 0.3)
        p = Circle(radius=0.26, color=FG, fill_opacity=1).set_fill(FG)
        p.move_to(bus[0].get_center())
        st = Text("СТОП", font=FONT, color="#FF5252", weight=BOLD).scale(0.5)
        st.next_to(bus, UP, 0.3)
        arr = Arrow(p.get_center(), p.get_center() + RIGHT * 1.4,
                    color=ACC, buff=0)
        self.play_for(Create(bus), FadeIn(p), frac=0.3)
        self.play_for(FadeIn(st), GrowArrow(arr), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(bus, p, st, arr)), frac=0.9)

    def beat_4(self):
        self.card("Резкий старт", "тело «отстаёт» — вжимает в кресло")

    def beat_5(self):
        glass = Rectangle(width=1.0, height=1.3, color=MUT, stroke_width=5)
        glass.shift(DOWN * 0.6)
        card = Rectangle(width=1.8, height=0.06, color=FG,
                         fill_opacity=1).set_fill(FG)
        card.next_to(glass, UP, buff=0.02)
        coin = Circle(radius=0.16, color=ACC, fill_opacity=1).set_fill(ACC)
        coin.next_to(card, UP, buff=0.0)
        arr = Arrow(card.get_center(), card.get_center() + RIGHT * 1.8,
                    color="#FF5252", buff=0)
        cap = Text("монетка падает в стакан", font=FONT,
                   color=MUT).scale(0.45).to_edge(DOWN, buff=0.7)
        self.play_for(Create(glass), FadeIn(card), FadeIn(coin), frac=0.35)
        self.play_for(GrowArrow(arr), FadeIn(cap), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(glass, card, coin, arr, cap)), frac=0.9)

    def beat_6(self):
        self.card("Больше масса —", "больше инертность")

    def beat_7(self):
        self.card("Гружёный грузовик", "тормозит дольше пустого")

    def beat_8(self):
        self.card("Ремень безопасности",
                  "при ударе тело летит вперёд по инерции", color=ACC)

    def beat_9(self):
        self.card("Скорость меняет", "только сила")

    def beat_10(self):
        a = Text("Метро: почему качает\nпри старте и торможении?",
                 font=FONT, color=ACC, weight=BOLD).scale(0.6)
        a.to_edge(UP, buff=1.3)
        cta = Text("Пиши в комментариях · Следующий выпуск →",
                   font=FONT, color=MUT).scale(0.5).to_edge(DOWN, buff=1.0)
        self.play_for(FadeIn(a, shift=DOWN * 0.2), frac=0.4)
        self.play_for(FadeIn(cta), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(a, cta)), frac=0.9)
