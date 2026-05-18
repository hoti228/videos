"""Видео №10: «Хитрая задача на среднюю скорость, где ошибаются почти все»
Факт-чек (чистая арифметика, проверяемо):
- путь в одну сторону 120 км; туда 60 км/ч → 2 ч; обратно 40 км/ч → 3 ч;
- весь путь 240 км, всё время 5 ч; средняя = 240/5 = 48 км/ч (не 50).
- Ответ не зависит от выбранного расстояния (среднее гармоническое
  2·60·40/(60+40) = 48 км/ч).
"""
from __future__ import annotations
from manim import (
    Text, VGroup,
    FadeIn, FadeOut,
    UP, DOWN, LEFT, RIGHT, BOLD,
)
import config
from core.scene_base import NarratedScene, FONT

ACC, FG, MUT = config.BRAND_ACCENT, config.BRAND_FG, config.BRAND_MUTED

NARRATION = [
    "Туда — шестьдесят километров в час, обратно — сорок. Средняя "
    "скорость пятьдесят? На этом ошибаются почти все.",
    "Кажется логичным: шестьдесят плюс сорок, делить на два — "
    "пятьдесят. Но это неверно.",
    "Средняя скорость — это весь путь, делённый на всё время. "
    "Не среднее из чисел!",
    "Посчитаем. Пусть в одну сторону сто двадцать километров — "
    "так удобнее.",
    "Туда со скоростью шестьдесят — это два часа в пути.",
    "Обратно со скоростью сорок — это уже три часа.",
    "Весь путь — двести сорок километров. Всё время — пять часов.",
    "Средняя скорость: двести сорок делить на пять — сорок восемь "
    "километров в час. Не пятьдесят!",
    "Почему меньше? На медленный участок уходит больше времени, "
    "поэтому он «весит» сильнее.",
    "Правило: среднюю скорость всегда считают через путь и время, "
    "а не усреднением скоростей.",
    "Итог: всегда «весь путь делить на всё время». Правильный "
    "ответ — сорок восемь.",
    "А если туда и обратно ехать с одной и той же скоростью — будет "
    "ли средняя ей равна? Напиши в комментариях и смотри следующий "
    "выпуск.",
]


class Episode010(NarratedScene):
    narration = NARRATION
    episode_title = "Задача про среднюю скорость"

    def beat_0(self):
        self.card("60 туда, 40 обратно", "средняя = 50?", color=ACC)

    def beat_1(self):
        wrong = Text("(60 + 40) / 2 = 50", font=FONT, color="#FF5252",
                     weight=BOLD).scale(0.8)
        x = Text("так — неверно", font=FONT, color="#FF5252").scale(0.55)
        x.next_to(wrong, DOWN, 0.4)
        self.play_for(FadeIn(VGroup(wrong, x), shift=UP * 0.2), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(wrong, x)), frac=0.9)

    def beat_2(self):
        self.card("Средняя скорость =", "весь путь / всё время",
                  color=ACC)

    def beat_3(self):
        self.card("Пусть 120 км", "в одну сторону")

    def beat_4(self):
        self.card("Туда: 60 км/ч", "120 / 60 = 2 часа")

    def beat_5(self):
        self.card("Обратно: 40 км/ч", "120 / 40 = 3 часа")

    def beat_6(self):
        self.card("Всего: 240 км", "за 5 часов")

    def beat_7(self):
        r = Text("240 / 5 = 48 км/ч", font=FONT, color=ACC,
                 weight=BOLD).scale(0.95)
        x = Text("а не 50!", font=FONT, color="#FF5252",
                 weight=BOLD).scale(0.6).next_to(r, DOWN, 0.4)
        self.play_for(FadeIn(r, scale=1.15), frac=0.45)
        self.play_for(FadeIn(x), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(r, x)), frac=0.9)

    def beat_8(self):
        self.card("Медленный участок", "длится дольше — «весит» больше")

    def beat_9(self):
        self.card("Правило", "через путь и время, не усреднять скорости")

    def beat_10(self):
        self.card("Ответ: 48 км/ч", "весь путь / всё время", color=ACC)

    def beat_11(self):
        a = Text("Одна скорость туда-обратно:\nсредняя ей равна?",
                 font=FONT, color=ACC, weight=BOLD).scale(0.56)
        a.to_edge(UP, buff=1.3)
        cta = Text("Пиши · Следующий выпуск →", font=FONT,
                   color=MUT).scale(0.5).to_edge(DOWN, buff=1.0)
        self.play_for(FadeIn(a, shift=DOWN * 0.2), frac=0.4)
        self.play_for(FadeIn(cta), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(a, cta)), frac=0.9)
