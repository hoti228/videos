"""Видео №1: «Почему всё падает одинаково быстро?»

Факты сверены (см. content/scripts/001_*.md):
- g у Земли ≈ 9,8 м/с² (станд. 9,80665, NIST/CGPM 1901)
- Аполлон-15, 2 августа 1971, командир Дэвид Скотт (NASA, Wikipedia)
- молоток ≈1,32 кг (алюм.), соколиное перо ≈0,03 кг, высота ≈1,6 м (NASA)
- притяжение Луны ≈1,62 м/с² ≈ 1/6 земного (NASA, Wikipedia)
- «Галилей и Пизанская башня» — историческая легенда (Wikipedia, Physics World)
Числа в озвучке намеренно округлены и поданы со словами «около/примерно».
"""
from __future__ import annotations

from manim import (
    Text, VGroup, Circle, Square, Rectangle, Line, Arrow, Dot,
    FadeIn, FadeOut, Create, GrowArrow, Indicate,
    UP, DOWN, LEFT, RIGHT, ORIGIN, BOLD,
)
import config
from core.scene_base import NarratedScene, FONT

ACC = config.BRAND_ACCENT
FG = config.BRAND_FG
MUT = config.BRAND_MUTED

NARRATION = [
    # 0 — хук
    "Что упадёт быстрее: тяжёлый молоток или лёгкое пёрышко? "
    "Ответ удивляет почти каждого.",
    # 1 — наивное ожидание
    "Кажется очевидным: чем тяжелее предмет, тем быстрее он падает. "
    "Брось камень и лист бумаги — камень внизу первым. "
    "Но физика говорит: дело не в весе.",
    # 2 — роль воздуха
    "Листу бумаги мешает воздух. Скомкай тот же лист в плотный шарик — "
    "и он упадёт почти как камень. Изменился не вес, а сопротивление воздуха.",
    # 3 — Галилей
    "Более четырёхсот лет назад Галилео Галилей понял главное: "
    "если убрать воздух, все тела падают одинаково — не важно, какая масса.",
    # 4 — легенда о башне (честно)
    "Есть красивая история, будто Галилей бросал шары с Пизанской башни. "
    "Историки считают это лишь легендой. Но сама идея оказалась верной.",
    # 5 — почему так (компенсация)
    "Почему? Землю тяжёлый предмет притягивает сильнее. "
    "Но тяжёлый предмет и труднее разогнать — у него больше инертность. "
    "Эти два эффекта точно уравновешивают друг друга.",
    # 6 — вакуум
    "Поэтому в пустоте, где воздуха нет, перо и молоток разгоняются "
    "совершенно одинаково и падают вместе.",
    # 7 — g
    "У поверхности Земли скорость свободного падения растёт примерно "
    "на девять и восемь десятых метра в секунду каждую секунду. "
    "Это ускорение свободного падения, его обозначают буквой g.",
    # 8 — Аполлон-15
    "И это не просто слова из учебника. Второго августа тысяча девятьсот "
    "семьдесят первого года это проверили на Луне, в миссии Аполлон-15.",
    # 9 — Скотт, молоток и перо
    "Командир Дэвид Скотт держал в одной руке геологический молоток массой "
    "около одного и трёх десятых килограмма, а в другой — лёгкое соколиное перо.",
    # 10 — одновременно
    "Он отпустил их одновременно примерно с высоты полутора метров. "
    "И тяжёлый молоток, и лёгкое перо коснулись лунного грунта "
    "в один и тот же миг.",
    # 11 — Луна слабее, вывод
    "Притяжение на Луне примерно в шесть раз слабее земного, поэтому "
    "падали они медленно и плавно — но строго вместе. Галилей оказался прав.",
    # 12 — аутро, вовлечение (без продаж)
    "Итог: кто упадёт быстрее, решает не вес, а воздух. "
    "А как думаешь: что коснётся земли первым в вакууме — кирпич или ты сам? "
    "Напиши в комментариях и смотри следующий выпуск.",
]


def _ground(y=-3.0):
    return Line(LEFT * 7 + UP * y, RIGHT * 7 + UP * y, color=MUT, stroke_width=6)


def _hammer(scale=1.0):
    head = Rectangle(width=0.9, height=0.45, color=MUT, fill_opacity=1).set_fill(MUT)
    handle = Rectangle(width=0.16, height=1.0, color="#7A5230", fill_opacity=1).set_fill("#7A5230")
    handle.next_to(head, DOWN, buff=0)
    return VGroup(head, handle).scale(scale)


def _feather(scale=1.0):
    quill = Line(UP * 0.5, DOWN * 0.5, color=FG, stroke_width=3)
    vane = Circle(radius=0.32, color=ACC, fill_opacity=0.6).set_fill(ACC)
    vane.move_to(quill.get_center())
    return VGroup(vane, quill).scale(scale)


class Episode001(NarratedScene):
    narration = NARRATION
    episode_title = "Почему всё падает одинаково быстро?"

    # 0
    def beat_0(self):
        q = Text("Что упадёт быстрее?", font=FONT, color=FG, weight=BOLD).scale(0.95)
        q.to_edge(UP, buff=1.0)
        h = _hammer(0.9).next_to(q, DOWN, buff=1.0).shift(LEFT * 2.2)
        f = _feather(0.9).next_to(q, DOWN, buff=1.0).shift(RIGHT * 2.2)
        self.play_for(FadeIn(q, shift=DOWN * 0.3), frac=0.4)
        self.play_for(FadeIn(h), FadeIn(f), frac=0.5)
        self.play_for(Indicate(h, color=ACC), Indicate(f, color=ACC), frac=0.7)
        self.hold()
        self.play_for(FadeOut(VGroup(q, h, f)), frac=0.9)

    # 1
    def beat_1(self):
        g = _ground()
        stone = Circle(radius=0.35, color=MUT, fill_opacity=1).set_fill(MUT)
        stone.move_to(UP * 2.6 + LEFT * 2.2)
        paper = Rectangle(width=0.9, height=1.1, color=FG, fill_opacity=0.9).set_fill(FG)
        paper.move_to(UP * 2.6 + RIGHT * 2.2)
        ls = Text("камень", font=FONT, color=MUT).scale(0.4).next_to(stone, UP, 0.2)
        lp = Text("лист бумаги", font=FONT, color=MUT).scale(0.4).next_to(paper, UP, 0.2)
        self.play_for(Create(g), FadeIn(VGroup(stone, paper, ls, lp)), frac=0.35)
        self.play_for(
            stone.animate.move_to(LEFT * 2.2 + DOWN * 2.6),
            paper.animate.move_to(RIGHT * 2.2 + DOWN * 1.2),
            frac=0.55, rate_func=lambda t: t * t,
        )
        self.hold()
        self.play_for(FadeOut(VGroup(g, stone, paper, ls, lp)), frac=0.9)

    # 2
    def beat_2(self):
        g = _ground()
        paper = Rectangle(width=0.9, height=1.1, color=FG, fill_opacity=0.9).set_fill(FG)
        paper.move_to(UP * 2.6 + LEFT * 2.2)
        stone = Circle(radius=0.35, color=MUT, fill_opacity=1).set_fill(MUT)
        stone.move_to(UP * 2.6 + RIGHT * 2.2)
        ball = Circle(radius=0.33, color=FG, fill_opacity=0.9).set_fill(FG)
        ball.move_to(paper.get_center())
        self.play_for(Create(g), FadeIn(VGroup(paper, stone)), frac=0.3)
        self.play_for(FadeOut(paper), FadeIn(ball), frac=0.3)  # смяли в шарик
        self.play_for(
            ball.animate.move_to(LEFT * 2.2 + DOWN * 2.6),
            stone.animate.move_to(RIGHT * 2.2 + DOWN * 2.6),
            frac=0.7, rate_func=lambda t: t * t,
        )
        self.hold()
        self.play_for(FadeOut(VGroup(g, ball, stone)), frac=0.9)

    # 3
    def beat_3(self):
        port = Circle(radius=1.0, color=ACC, stroke_width=6)
        nm = Text("Галилео\nГалилей", font=FONT, color=FG, weight=BOLD).scale(0.45)
        nm.move_to(port.get_center())
        grp = VGroup(port, nm).shift(LEFT * 3.2)
        idea = Text("убрать воздух →\nвсе падают одинаково", font=FONT,
                    color=ACC, weight=BOLD).scale(0.6).shift(RIGHT * 2.2)
        self.play_for(Create(port), FadeIn(nm), frac=0.4)
        self.play_for(FadeIn(idea, shift=RIGHT * 0.3), frac=0.55)
        self.hold()
        self.play_for(FadeOut(VGroup(grp, idea)), frac=0.9)

    # 4
    def beat_4(self):
        tower = Rectangle(width=0.9, height=4.0, color=MUT, fill_opacity=0.7).set_fill(MUT)
        tower.rotate(-0.12).shift(LEFT * 3.0 + DOWN * 0.3)
        stamp = Text("ЛЕГЕНДА", font=FONT, color="#FF5252", weight=BOLD).scale(0.9)
        stamp.rotate(-0.2).shift(RIGHT * 1.6 + UP * 0.6)
        note = Text("идея верна, история — миф", font=FONT, color=MUT).scale(0.5)
        note.next_to(stamp, DOWN, buff=0.5)
        self.play_for(Create(tower), frac=0.4)
        self.play_for(FadeIn(stamp, scale=1.3), frac=0.4)
        self.play_for(FadeIn(note), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(tower, stamp, note)), frac=0.9)

    # 5
    def beat_5(self):
        heavy = Square(side_length=1.1, color=MUT, fill_opacity=1).set_fill(MUT)
        heavy.shift(LEFT * 3.0)
        light = Square(side_length=0.6, color=FG, fill_opacity=1).set_fill(FG)
        light.shift(RIGHT * 3.0)
        ah = Arrow(heavy.get_bottom(), heavy.get_bottom() + DOWN * 1.6, color=ACC, buff=0)
        al = Arrow(light.get_bottom(), light.get_bottom() + DOWN * 0.8, color=ACC, buff=0)
        th = Text("сильнее тянет,\nно тяжелее разогнать", font=FONT, color=MUT).scale(0.4)
        th.next_to(heavy, UP, 0.3)
        eq = Text("ускорение одинаковое", font=FONT, color=ACC, weight=BOLD).scale(0.6)
        eq.to_edge(DOWN, buff=0.8)
        self.play_for(FadeIn(heavy), FadeIn(light), frac=0.3)
        self.play_for(GrowArrow(ah), GrowArrow(al), FadeIn(th), frac=0.45)
        self.play_for(FadeIn(eq, shift=UP * 0.2), frac=0.6)
        self.hold()
        self.play_for(FadeOut(VGroup(heavy, light, ah, al, th, eq)), frac=0.9)

    # 6
    def beat_6(self):
        tube = Rectangle(width=2.4, height=5.0, color=ACC, stroke_width=5)
        tube.shift(DOWN * 0.2)
        lab = Text("ВАКУУМ", font=FONT, color=ACC, weight=BOLD).scale(0.6)
        lab.next_to(tube, UP, 0.25)
        h = _hammer(0.7).move_to(tube.get_top() + DOWN * 0.8 + LEFT * 0.55)
        f = _feather(0.7).move_to(tube.get_top() + DOWN * 0.8 + RIGHT * 0.55)
        self.play_for(Create(tube), FadeIn(lab), frac=0.3)
        self.play_for(FadeIn(h), FadeIn(f), frac=0.25)
        self.play_for(
            h.animate.move_to(tube.get_bottom() + UP * 0.5 + LEFT * 0.55),
            f.animate.move_to(tube.get_bottom() + UP * 0.5 + RIGHT * 0.55),
            frac=0.7, rate_func=lambda t: t * t,
        )
        self.hold()
        self.play_for(FadeOut(VGroup(tube, lab, h, f)), frac=0.9)

    # 7
    def beat_7(self):
        axis = Line(DOWN * 2.6, UP * 2.6, color=MUT).shift(LEFT * 4.0)
        cap = Text("скорость растёт", font=FONT, color=MUT).scale(0.45)
        cap.next_to(axis, UP, 0.2)
        d = Dot(axis.get_bottom(), color=ACC, radius=0.12)
        big = Text("g ≈ 9,8 м/с²", font=FONT, color=ACC, weight=BOLD).scale(1.0)
        big.shift(RIGHT * 1.5)
        self.play_for(Create(axis), FadeIn(cap), FadeIn(d), frac=0.35)
        self.play_for(d.animate.move_to(axis.get_top()), frac=0.4,
                      rate_func=lambda t: t * t)
        self.play_for(FadeIn(big, scale=1.2), frac=0.55)
        self.hold()
        self.play_for(FadeOut(VGroup(axis, cap, d, big)), frac=0.9)

    # 8
    def beat_8(self):
        moon = Circle(radius=2.3, color=MUT, fill_opacity=0.25).set_fill(MUT)
        moon.shift(DOWN * 0.2)
        t1 = Text("Аполлон-15", font=FONT, color=FG, weight=BOLD).scale(0.8)
        t2 = Text("2 августа 1971 · Луна", font=FONT, color=ACC).scale(0.5)
        t1.to_edge(UP, buff=1.1)
        t2.next_to(t1, DOWN, 0.25)
        self.play_for(FadeIn(moon, scale=1.2), frac=0.4)
        self.play_for(FadeIn(t1, shift=DOWN * 0.2), FadeIn(t2), frac=0.55)
        self.hold()
        self.play_for(FadeOut(VGroup(moon, t1, t2)), frac=0.9)

    # 9
    def beat_9(self):
        body = VGroup(
            Circle(radius=0.45, color=FG, fill_opacity=1).set_fill(FG),
            Rectangle(width=0.9, height=1.3, color=FG, fill_opacity=1).set_fill(FG),
        )
        body[1].next_to(body[0], DOWN, buff=0)
        body.shift(DOWN * 0.3)
        h = _hammer(0.6).next_to(body, LEFT, buff=0.4).shift(UP * 0.2)
        f = _feather(0.6).next_to(body, RIGHT, buff=0.4).shift(UP * 0.2)
        lh = Text("молоток ≈ 1,3 кг", font=FONT, color=MUT).scale(0.42)
        lf = Text("соколиное перо", font=FONT, color=MUT).scale(0.42)
        lh.next_to(h, DOWN, 0.3)
        lf.next_to(f, DOWN, 0.3)
        self.play_for(FadeIn(body), frac=0.3)
        self.play_for(FadeIn(h), FadeIn(f), FadeIn(lh), FadeIn(lf), frac=0.6)
        self.hold()
        self.play_for(FadeOut(VGroup(body, h, f, lh, lf)), frac=0.9)

    # 10
    def beat_10(self):
        g = _ground(-2.8)
        sub = Text("Луна", font=FONT, color=MUT).scale(0.4).next_to(g, DOWN, 0.15)
        h = _hammer(0.6).move_to(UP * 2.4 + LEFT * 1.6)
        f = _feather(0.6).move_to(UP * 2.4 + RIGHT * 1.6)
        self.play_for(Create(g), FadeIn(sub), FadeIn(h), FadeIn(f), frac=0.3)
        self.play_for(
            h.animate.move_to(LEFT * 1.6 + DOWN * 2.4),
            f.animate.move_to(RIGHT * 1.6 + DOWN * 2.4),
            frac=0.55, rate_func=lambda t: t * t,
        )
        bang = Text("одновременно!", font=FONT, color=ACC, weight=BOLD).scale(0.8)
        bang.move_to(UP * 1.2)
        self.play_for(FadeIn(bang, scale=1.3), frac=0.8)
        self.hold()
        self.play_for(FadeOut(VGroup(g, sub, h, f, bang)), frac=0.9)

    # 11
    def beat_11(self):
        le = Text("Земля: g ≈ 9,8 м/с²", font=FONT, color=FG).scale(0.6)
        lm = Text("Луна: g ≈ 1,6 м/с²  (≈ в 6 раз слабее)", font=FONT,
                  color=ACC, weight=BOLD).scale(0.6)
        le.shift(UP * 0.7)
        lm.next_to(le, DOWN, 0.5)
        win = Text("Галилей оказался прав", font=FONT, color=FG, weight=BOLD).scale(0.7)
        win.to_edge(DOWN, buff=0.9)
        self.play_for(FadeIn(le), frac=0.3)
        self.play_for(FadeIn(lm, shift=DOWN * 0.2), frac=0.4)
        self.play_for(FadeIn(win, scale=1.15), frac=0.6)
        self.hold()
        self.play_for(FadeOut(VGroup(le, lm, win)), frac=0.9)

    # 12
    def beat_12(self):
        a = Text("Решает не вес — решает воздух.", font=FONT, color=FG,
                 weight=BOLD).scale(0.72)
        a.to_edge(UP, buff=1.3)
        q = Text("В вакууме: кирпич или ты сам?", font=FONT, color=ACC,
                 weight=BOLD).scale(0.6).next_to(a, DOWN, 0.6)
        cta = Text("Пиши в комментариях · Следующий выпуск →", font=FONT,
                   color=MUT).scale(0.5).to_edge(DOWN, buff=1.0)
        self.play_for(FadeIn(a, shift=DOWN * 0.2), frac=0.35)
        self.play_for(FadeIn(q), frac=0.35)
        self.play_for(FadeIn(cta), frac=0.5)
        self.hold()
        self.play_for(FadeOut(VGroup(a, q, cta)), frac=0.95)
