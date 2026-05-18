"""Видео №8: «Почему лёд скользкий?»  (разоблачение мифа)
Факт-чек:
- Старое объяснение «лёд тает под давлением конька» — в основном НЕВЕРНО:
  давление снижает t плавления лишь на доли градуса; лёд скользкий и
  в сильный мороз. Источники: Physics Today «Why Is Ice Slippery?»,
  Quanta Magazine (2025), Penn Today, Science News Explores.
- Реальная причина: на поверхности льда всегда есть тончайший
  «квазижидкий» (полужидкий) слой — премелтинг; трение/скольжение
  его дополнительно усиливают.
Числа намеренно не приводятся (только качественно: «на доли градуса»).
"""
from __future__ import annotations
from manim import (
    Text, VGroup, Rectangle, Line,
    FadeIn, FadeOut, Create,
    UP, DOWN, LEFT, RIGHT, BOLD,
)
import config
from core.scene_base import NarratedScene, FONT

ACC, FG, MUT = config.BRAND_ACCENT, config.BRAND_FG, config.BRAND_MUTED

NARRATION = [
    "Почему лёд скользкий, а камень — нет? Привычный школьный ответ "
    "оказался неверным.",
    "Старое объяснение: конёк давит на лёд, лёд тает под давлением, "
    "и ты едешь по тонкой плёнке воды.",
    "Но это в основном миф. Давление снижает температуру плавления "
    "лишь на доли градуса.",
    "Лёд остаётся скользким и в сильный мороз, когда никакого "
    "плавления от давления быть не может.",
    "Настоящая причина: у поверхности льда всегда есть тончайший "
    "полужидкий слой.",
    "Молекулы на самой поверхности расположены менее упорядоченно — "
    "этот слой ведёт себя как вязкая жидкость.",
    "Он существует сам по себе, без всякого давления, даже при "
    "температуре ниже нуля.",
    "А скольжение и трение слегка нагревают поверхность и делают "
    "этот слой ещё заметнее.",
    "Поэтому коньки, лыжи и обычная подошва легко скользят по этой "
    "невидимой плёнке.",
    "Это хороший пример, как наука уточняет «очевидные» школьные "
    "объяснения. Проверяй факты.",
    "Итог: лёд скользкий не из-за давления, а из-за собственного "
    "жидкоподобного слоя на поверхности.",
    "А как думаешь: почему мокрый лёд около нуля ещё скользче, чем "
    "сухой в мороз? Напиши в комментариях и смотри следующий выпуск.",
]


class Episode008(NarratedScene):
    narration = NARRATION
    episode_title = "Почему лёд скользкий (не из-за давления)"

    def _ice(self):
        block = Rectangle(width=6.0, height=1.4, color="#7FB3D5",
                          fill_opacity=0.35).set_fill("#7FB3D5")
        block.shift(DOWN * 1.0)
        return block

    def beat_0(self):
        self.card("Почему лёд скользкий?", "привычный ответ — неверный",
                  color=ACC)

    def beat_1(self):
        ice = self._ice()
        skate = Line(ice.get_top() + LEFT * 0.8, ice.get_top() + RIGHT * 0.8,
                     color=FG, stroke_width=8)
        lab = Text("давит → тает?", font=FONT, color=MUT).scale(0.5)
        lab.next_to(ice, UP, 0.3)
        self.play_for(Create(ice), FadeIn(skate), FadeIn(lab), frac=0.45)
        self.hold()
        self.play_for(FadeOut(VGroup(ice, skate, lab)), frac=0.9)

    def beat_2(self):
        self.card("МИФ", "давление снижает t плавления\nлишь на доли градуса",
                  color="#FF5252")

    def beat_3(self):
        self.card("Лёд скользкий", "и в сильный мороз")

    def beat_4(self):
        ice = self._ice()
        layer = Rectangle(width=6.0, height=0.18, color=ACC,
                          fill_opacity=1).set_fill(ACC)
        layer.move_to(ice.get_top() + DOWN * 0.09)
        lab = Text("полужидкий слой — всегда", font=FONT, color=ACC,
                   weight=BOLD).scale(0.5).next_to(ice, UP, 0.3)
        self.play_for(Create(ice), frac=0.3)
        self.play_for(FadeIn(layer), FadeIn(lab), frac=0.55)
        self.hold()
        self.play_for(FadeOut(VGroup(ice, layer, lab)), frac=0.9)

    def beat_5(self):
        self.card("Поверхность льда", "молекулы менее упорядочены")

    def beat_6(self):
        self.card("Слой есть сам по себе", "без давления, ниже нуля",
                  color=ACC)

    def beat_7(self):
        self.card("Трение нагревает", "и усиливает этот слой")

    def beat_8(self):
        self.card("Коньки и лыжи", "скользят по невидимой плёнке")

    def beat_9(self):
        self.card("Проверяй факты", "наука уточняет «очевидное»",
                  color=ACC)

    def beat_10(self):
        self.card("Дело не в давлении —", "а в жидком слое на поверхности")

    def beat_11(self):
        a = Text("Почему мокрый лёд\nещё скользче?", font=FONT,
                 color=ACC, weight=BOLD).scale(0.62).to_edge(UP, buff=1.3)
        cta = Text("Пиши · Следующий выпуск →", font=FONT,
                   color=MUT).scale(0.5).to_edge(DOWN, buff=1.0)
        self.play_for(FadeIn(a, shift=DOWN * 0.2), frac=0.4)
        self.play_for(FadeIn(cta), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(a, cta)), frac=0.9)
