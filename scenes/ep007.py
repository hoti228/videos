"""Видео №7: «Трение: почему без него нельзя ходить?»
Факты: качественная физика трения (Пёрышкин 7 кл). Числа не используются.
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
    "Представь мир без трения. Звучит удобно? На самом деле ты не "
    "смог бы сделать ни шага.",
    "Когда идёшь, твоя нога толкает землю назад. А трение в ответ "
    "толкает тебя вперёд.",
    "Без трения нога просто проскальзывала бы — как на очень "
    "скользком льду.",
    "Трение — это сила, которая мешает поверхностям скользить друг "
    "по другу.",
    "Оно останавливает автомобиль, держит гвоздь в стене и узел "
    "на верёвке.",
    "Но у трения есть обратная сторона: оно нагревает детали и "
    "изнашивает их.",
    "Поэтому в механизмах применяют смазку и подшипники — чтобы "
    "трение уменьшить.",
    "А вот убрать его полностью нельзя: без трения не затормозить и "
    "ничего не удержать.",
    "Чем сильнее прижаты поверхности, тем больше трение. А вот "
    "площадь почти не влияет.",
    "Итог: трение и мешает, и помогает. Ходьба, торможение, захват — "
    "всё благодаря ему.",
    "А как думаешь: зачем зимой на лёд и дороги сыплют песок? "
    "Напиши в комментариях и смотри следующий выпуск.",
]


class Episode007(NarratedScene):
    narration = NARRATION
    episode_title = "Зачем нужно трение?"

    def beat_0(self):
        self.card("Мир без трения?", "ни шагу не сделать", color=ACC)

    def beat_1(self):
        ground = Line(LEFT * 5 + DOWN * 1.5, RIGHT * 5 + DOWN * 1.5,
                      color=MUT, stroke_width=6)
        foot = Rectangle(width=0.9, height=0.35, color=FG,
                         fill_opacity=1).set_fill(FG)
        foot.move_to(DOWN * 1.25)
        a_back = Arrow(foot.get_center(), foot.get_center() + LEFT * 1.4,
                       color=MUT, buff=0)
        a_fwd = Arrow(foot.get_center() + UP * 0.5,
                      foot.get_center() + UP * 0.5 + RIGHT * 1.4,
                      color=ACC, buff=0)
        l1 = Text("нога толкает назад", font=FONT, color=MUT).scale(0.4)
        l1.next_to(a_back, DOWN, 0.2)
        l2 = Text("трение толкает вперёд", font=FONT, color=ACC).scale(0.42)
        l2.next_to(a_fwd, UP, 0.2)
        self.play_for(Create(ground), FadeIn(foot), frac=0.3)
        self.play_for(GrowArrow(a_back), FadeIn(l1), frac=0.4)
        self.play_for(GrowArrow(a_fwd), FadeIn(l2), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(ground, foot, a_back, a_fwd, l1, l2)),
                      frac=0.9)

    def beat_2(self):
        self.card("Без трения", "нога проскальзывает — как по льду")

    def beat_3(self):
        self.card("ТРЕНИЕ", "мешает поверхностям скользить", color=ACC)

    def beat_4(self):
        self.card("Трение держит", "тормоза · гвоздь · узел")

    def beat_5(self):
        self.card("Минус трения", "нагрев и износ", color="#FF5252")

    def beat_6(self):
        self.card("Смазка и подшипники", "уменьшают трение")

    def beat_7(self):
        self.card("Совсем убрать нельзя", "не затормозить, не удержать")

    def beat_8(self):
        self.card("Сильнее прижал —", "больше трение (площадь не важна)")

    def beat_9(self):
        self.card("Трение и мешает,", "и помогает", color=ACC)

    def beat_10(self):
        a = Text("Зачем зимой сыплют\nпесок на лёд?", font=FONT,
                 color=ACC, weight=BOLD).scale(0.62).to_edge(UP, buff=1.3)
        cta = Text("Пиши · Следующий выпуск →", font=FONT,
                   color=MUT).scale(0.5).to_edge(DOWN, buff=1.0)
        self.play_for(FadeIn(a, shift=DOWN * 0.2), frac=0.4)
        self.play_for(FadeIn(cta), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(a, cta)), frac=0.9)
