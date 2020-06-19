from manimlib.imports import *

class SimpleDragForce(Scene):
    def construct(self):
        eq1 = TexMobject(
            "F_d", "=", "-", "b", "v")
        eq1.move_to(2*UP)
        self.play(Write(eq1))

        brace_b = Brace(eq1[-2], DOWN, buff = SMALL_BUFF)
        t_b = brace_b.get_text(
            "$C$", "$\\rho$", "$A$")
        braces = [
            Brace(symbol, DOWN, buff = SMALL_BUFF)
            for symbol in t_b]
        texts = [
            "Drag coefficient",
            "Fluid density",
            "Cross sectional area"]
        ts = [braces[i].get_text(texts[i]) for i in range(len(texts))]

        self.play(
            GrowFromCenter(brace_b),
            FadeIn(t_b))

        self.play(
            GrowFromCenter(braces[0]),
            FadeIn(ts[0]))
        for i in range(2):
            self.play(
                ReplacementTransform(braces[i], braces[i+1]),
                ReplacementTransform(ts[i], ts[i+1]))
        self.play(
            FadeOut(braces[2]),
            FadeOut(ts[2]))
        
        self.play(
            FadeOut(brace_b),
            FadeOut(t_b))

        eq3 = TexMobject("\\sum", "F", "=", "F_d")
        eq3.next_to(eq1, DOWN)
        self.play(Write(eq3))

        eq4 = TexMobject("m", "a", "=", "-", "b", "v")
        eq4.next_to(eq3, DOWN)
        self.play(
            TransformFromCopy(eq3[1], eq4[:2]),
            TransformFromCopy(eq3[2], eq4[2]),
            TransformFromCopy(eq3[3], eq4[3:]))

        eq5 = TexMobject(
            "m", "{dv", "\\over", "dt}", "=", "-", "b", "v")
        eq5.next_to(eq4, DOWN)
        self.play(TransformFromCopy(eq4, eq5))
        self.wait()
        self.play(
            FadeOutAndShift(eq1, UP),
            FadeOutAndShift(eq3, UP),
            FadeOutAndShift(eq4, UP),
            ApplyMethod(eq5.move_to, UP*3))

        eq6 = TexMobject(
            "{1", "\\over", "v}", "dv", "=", 
            "-", "{b", "\\over", "m}", "dt")
        eq6.next_to(eq5, DOWN)
        self.play(TransformFromCopy(eq5[4], eq6[4]))
        self.play(
            TransformFromCopy(eq5[-1], eq6[2]),
            TransformFromCopy(eq5[1], eq6[3]),
            Write(eq6[:2]))   
        self.play(
            TransformFromCopy(eq5[-3], eq6[-5]),
            TransformFromCopy(eq5[-2], eq6[-4]),
            TransformFromCopy(eq5[0], eq6[-2]),
            TransformFromCopy(eq5[3], eq6[-1]),
            Write(eq6[-3]))
    
        eq7 = TexMobject(
            "\\int_{v_0}^{v(t)}", 
            "{1", "\\over", "v}", "dv", 
            "=", 
            "\\int_{0}^{t}", 
            "-", "{b", "\\over", "m}", "dt")
        eq7.next_to(eq6, DOWN)
        self.play(
            TransformFromCopy(eq6[:5], eq7[1:6]),
            TransformFromCopy(eq6[-5:], eq7[-5:]))
        self.play(
            Write(eq7[0]),
            Write(eq7[6]))

        eq8 = TexMobject(
            "ln(", "v", ")", "\Big|_{v_0}^{v(t)}", 
            "=", 
            "{b", "t", "\\over", "m}", "\Big|_0^t")
        eq8.next_to(eq7, DOWN)
        self.play(
            TransformFromCopy(eq7[1:5], eq8[:3]),
            TransformFromCopy(eq7[6], eq8[4]),
            TransformFromCopy(eq7[-4:-1], eq8[-5:-1]))
        self.play(
            Write(eq8[3]),
            Write(eq8[-1]))

        eq9 = TexMobject(
            "ln(", "v(t)", ")", "-",
            "ln(", "v_0", ")", 
            "=", 
            "{b", "t", "\\over", "m}")
        eq9.next_to(eq8, DOWN)
        self.play(
            TransformFromCopy(eq8[:4], eq9[:7]),
            TransformFromCopy(eq8[4], eq9[7]),
            TransformFromCopy(eq8[-5:], eq9[-4:]))
        self.wait()

        self.play(
            FadeOutAndShift(eq5, UP),
            FadeOutAndShift(eq6, UP),
            FadeOutAndShift(eq7, UP),
            FadeOutAndShift(eq8, UP),
            ApplyMethod(eq9.move_to, UP*3))

        ##################
        # eq10 = TexMobject(
        #     "{1", "\\over", "v(t)}", "=",
        #     "{b", "t", "\\over", "m}", "+",
        #     "{1", "\\over", "v_0}")
        # eq10.next_to(eq9, DOWN)
        # self.play(
        #     TransformFromCopy(eq9[:3], eq10[:3]),
        #     TransformFromCopy(eq9[7], eq10[3]),
        #     TransformFromCopy(eq9[-4:], eq10[4:8]),
        #     TransformFromCopy(eq9[3:7], eq10[-4:]))

        # eq11 = TexMobject(
        #     "v(t)", "=", "{1 \\over",
        #     "{b", "t", "\\over", "m}", "+",
        #     "{1", "\\over", "v_0}", "}")
        # eq11.next_to(eq10, DOWN)
        # self.play(
        #     TransformFromCopy(eq10[:4], eq11[:2]),
        #     TransformFromCopy(eq10[4:], eq11[3:]),
        #     Write(eq11[2]))

        # eq12 = TexMobject(
        #     "v(t)", "=", "{1 \\over",
        #     "{b", "v_0", "t", "+", "m", "\\over",
        #     "m", "v_0}", "}")
        # eq12.next_to(eq11, DOWN)
        # self.play(TransformFromCopy(eq11, eq12))

        # eq13 = TexMobject(
        #     "v(t)", "=", 
        #     "{", "m", "v_0", "\\over", 
        #     "b", "v_0", "t", "+", "m", "}")
        # eq13.next_to(eq12, DOWN)
        # self.play(
        #     TransformFromCopy(eq12[:2], eq13[:2]),
        #     TransformFromCopy(eq12[-3:], eq13[2:5]),
        #     TransformFromCopy(eq12[3:8], eq13[6:]),
        #     Write(eq13[5]))

class DragForce(Scene):
    def construct(self):
        eq1 = TexMobject(
            "F_d", "=", "-", "\\frac{1}{2}", "C", "\\rho", "A", "v^2")
        eq1.move_to(2*UP)
        self.play(Write(eq1))

        braces = [
            Brace(symbol, DOWN, buff = SMALL_BUFF)
            for symbol in eq1[-4:]]
        texts = [
            "Drag coefficient",
            "Fluid density",
            "Cross sectional area",
            "Velocity squared"]
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

        eq2 = TexMobject("F_d", "=", "-", "b", "v^2")
        eq2.move_to(eq1)
        self.play(Transform(eq1, eq2))
        brace_b = Brace(eq2[-2], DOWN, buff = SMALL_BUFF)
        t_b = brace_b.get_text("$\\frac{1}{2}C\\rho A$")
        self.play(
            GrowFromCenter(brace_b),
            FadeIn(t_b))
        self.play(
            FadeOut(brace_b),
            FadeOut(t_b))

        eq3 = TexMobject("\\sum", "F", "=", "F_d")
        eq3.next_to(eq1, DOWN)
        self.play(Write(eq3))

        eq4 = TexMobject("m", "a", "=", "-", "b", "v^2")
        eq4.next_to(eq3, DOWN)
        self.play(
            TransformFromCopy(eq3[1], eq4[:2]),
            TransformFromCopy(eq3[2], eq4[2]),
            TransformFromCopy(eq3[3], eq4[3:]))

        eq5 = TexMobject(
            "m", "{dv", "\\over", "dt}", "=", "-", "b", "v^2")
        eq5.next_to(eq4, DOWN)
        self.play(TransformFromCopy(eq4, eq5))
        self.wait()
        self.play(
            FadeOutAndShift(eq1, UP),
            FadeOutAndShift(eq3, UP),
            FadeOutAndShift(eq4, UP),
            ApplyMethod(eq5.move_to, UP*3))

        eq6 = TexMobject(
            "-", "{1", "\\over", "v^2}", "dv", "=", 
            "{b", "\\over", "m}", "dt")
        eq6.next_to(eq5, DOWN)
        self.play(TransformFromCopy(eq5[4], eq6[5]))
        self.play(
            TransformFromCopy(eq5[-1], eq6[3]),
            TransformFromCopy(eq5[-3], eq6[0]),
            TransformFromCopy(eq5[1], eq6[4]),
            Write(eq6[1:3]))   
        self.play(
            TransformFromCopy(eq5[6], eq6[6]),
            TransformFromCopy(eq5[0], eq6[-2]),
            TransformFromCopy(eq5[3], eq6[-1]),
            Write(eq6[-3]))
    
        eq7 = TexMobject(
            "\\int_{v_0}^{v(t)}", 
            "-", "{1", "\\over", "v^2}", "dv", 
            "=", 
            "\\int_{0}^{t}", 
            "{b", "\\over", "m}", "dt")
        eq7.next_to(eq6, DOWN)
        self.play(
            TransformFromCopy(eq6[:6], eq7[1:7]),
            TransformFromCopy(eq6[-4:], eq7[-4:]))
        self.play(
            Write(eq7[0]),
            Write(eq7[7]))

        eq8 = TexMobject(
            "{1", "\\over", "v}", "\Big|_{v_0}^{v(t)}", 
            "=", 
            "{b", "t", "\\over", "m}", "\Big|_0^t")
        eq8.next_to(eq7, DOWN)
        self.play(
            TransformFromCopy(eq7[1:5], eq8[:3]),
            TransformFromCopy(eq7[6], eq8[4]),
            TransformFromCopy(eq7[-4:-1], eq8[-5:-1]))
        self.play(
            Write(eq8[3]),
            Write(eq8[-1]))

        eq9 = TexMobject(
            "{1", "\\over", "v(t)}", "-",
            "{1", "\\over", "v_0}", 
            "=", 
            "{b", "t", "\\over", "m}")
        eq9.next_to(eq8, DOWN)
        self.play(
            TransformFromCopy(eq8[:4], eq9[:7]),
            TransformFromCopy(eq8[4], eq9[7]),
            TransformFromCopy(eq8[-5:], eq9[-4:]))
        self.wait()
        
        self.play(
            FadeOutAndShift(eq5, UP),
            FadeOutAndShift(eq6, UP),
            FadeOutAndShift(eq7, UP),
            FadeOutAndShift(eq8, UP),
            ApplyMethod(eq9.move_to, UP*3))

        # Solving for v(t)
        eq10 = TexMobject(
            "{1", "\\over", "v(t)}", "=",
            "{b", "t", "\\over", "m}", "+",
            "{1", "\\over", "v_0}")
        eq10.next_to(eq9, DOWN)
        self.play(
            TransformFromCopy(eq9[:3], eq10[:3]),
            TransformFromCopy(eq9[7], eq10[3]),
            TransformFromCopy(eq9[-4:], eq10[4:8]),
            TransformFromCopy(eq9[3:7], eq10[-4:]))

        eq11 = TexMobject(
            "v(t)", "=", "{1 \\over",
            "{b", "t", "\\over", "m}", "+",
            "{1", "\\over", "v_0}", "}")
        eq11.next_to(eq10, DOWN)
        self.play(
            TransformFromCopy(eq10[:4], eq11[:2]),
            TransformFromCopy(eq10[4:], eq11[3:]),
            Write(eq11[2]))

        eq12 = TexMobject(
            "v(t)", "=", "{1 \\over",
            "{b", "v_0", "t", "+", "m", "\\over",
            "m", "v_0}", "}")
        eq12.next_to(eq11, DOWN)
        self.play(TransformFromCopy(eq11, eq12))

        eq13 = TexMobject(
            "v(t)", "=", 
            "{", "m", "v_0", "\\over", 
            "b", "v_0", "t", "+", "m", "}")
        eq13.next_to(eq12, DOWN)
        self.play(
            TransformFromCopy(eq12[:2], eq13[:2]),
            TransformFromCopy(eq12[-3:], eq13[2:5]),
            TransformFromCopy(eq12[3:8], eq13[6:]),
            Write(eq13[5]))