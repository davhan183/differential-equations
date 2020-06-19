from manimlib.imports import *

class EulersMethod(Scene):
    def show_braces(self, eq):
        braces = [
            Brace(eq[index], DOWN, buff = SMALL_BUFF)
            for index in [4,5,7,8]]
        texts = [
            "Spring constant",
            "Spring position ",
            "Damping term",
            "Velocity"]
        ts = [braces[i].get_text(texts[i]) for i in range(len(texts))]
        self.play(
            GrowFromCenter(braces[0]),
            FadeIn(ts[0]))
        for i in range(3):
            self.play(
                ReplacementTransform(braces[i], braces[i+1]),
                ReplacementTransform(ts[i], ts[i+1]))
        self.play(
            FadeOut(braces[3]),
            FadeOut(ts[3]))
    def construct(self):
        eq1 = TexMobject("\\sum", "F", "=", "m", "a")
        eq1.move_to(2*UP)
        self.play(Write(eq1))

        eq2 = TexMobject(
            "\\sum", "F", "=", "F_s", "+", "F_d")
            # "\\sum", "F", "=", "m", "a", "=", "F_s", "+", "F_d")
        eq2.move_to(eq1)
        self.play(ReplacementTransform(eq1, eq2))

        eq3 = TexMobject("m", "a", "=", "-", "k", "x", "-", "b", "v")
        eq3.next_to(eq2, DOWN)
        self.play(
            TransformFromCopy(eq1[1], eq3[:2]),
            TransformFromCopy(eq2[2], eq3[2]),
            # TransformFromCopy(eq1[3:5], eq3[:2]),
            # TransformFromCopy(eq2[5], eq3[2]),
            TransformFromCopy(eq2[-3], eq3[-6:-3]),
            TransformFromCopy(eq2[-1], eq3[-3:]))

        self.show_braces(eq3)

        eq4 = TexMobject(
            "m", "{dv", "\\over", "dt}", "=", 
            "-", "k", "x", "-", "b", "v")
        eq4.next_to(eq3, DOWN)
        self.play(
            TransformFromCopy(eq3[:3], eq4[:5]),
            TransformFromCopy(eq3[3:], eq4[5:]))

        eq5 = TexMobject(
            "m", "{d^2x", "\\over", "dt^2}", "=", 
            "-", "k", "x", "-", "b", "{dx", "\\over", "dt}")
        # eq5.move_to(eq4)
        eq5.next_to(eq4, DOWN)
        self.play(
            # ReplacementTransform(eq4[:4], eq5[:4]),
            # ReplacementTransform(eq4[-1], eq5[-3:]))
            TransformFromCopy(eq4[:5], eq5[:5]),
            TransformFromCopy(eq4[5:-1], eq5[5:-3]),
            TransformFromCopy(eq4[-1], eq5[-3:]))

        self.wait()
        self.play(
            FadeOutAndShift(eq1, UP),
            FadeOutAndShift(eq2, UP),
            FadeOutAndShift(eq3, UP),
            FadeOutAndShift(eq5, UP),
            ApplyMethod(eq4.move_to, UP*3))
            # ApplyMethod(eq4.move_to, UP*1 + LEFT*3),
            # ApplyMethod(eq5.move_to, UP*1 + RIGHT*3))

        eq4_1 = TexMobject(
            "{dv", "\\over", "dt}", "=", 
            "-", "{1", "\\over", "m}", 
            "(", "k", "x", "+", "b", "v", ")")
        eq4_1.next_to(eq4, DOWN)
        # eq5_1 = TexMobject(
        #     "{d^2x", "\\over", "dt^2}", "=", 
        #     "-", "{1", "\\over", "m}", 
        #     "(", "k", "x", "+", "b", "{dx", "\\over", "dt}", ")")
        # eq5_1.next_to(eq5, DOWN)
        self.play(
            TransformFromCopy(eq4[1:6], eq4_1[:5]),
            TransformFromCopy(eq4[0], eq4_1[7]),
            TransformFromCopy(eq4[-5:], eq4_1[-6:-1]),

            Write(eq4_1[5:7]),
            Write(eq4_1[8]),
            Write(eq4_1[-1]) )#,

        #     TransformFromCopy(eq5[1:6], eq5_1[:5]),
        #     TransformFromCopy(eq5[0], eq5_1[7]),
        #     TransformFromCopy(eq5[-7:], eq5_1[-8:-1]),

        #     Write(eq5_1[5:7]),
        #     Write(eq5_1[8]),
        #     Write(eq5_1[-1]))
