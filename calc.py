from tkinter import messagebox
from tkinter import *
from math import sin as sinus, cos as cosinus, tan as tanges, pi as π, log as logaritm, e, factorial, radians
import matplotlib.pyplot as plt
import numpy as np


class fact(int):
    def __rpow__(self, other):
        return factorial(other)


Fa = fact()

mem = ""
base = 10

sins = {0: 0, 30: 0.5, 90: 1, 150: 0.5, 180: 0, 210: -0.5, 270: -1, 330: -0.5}
coss = {0: 1, 60: 0.5, 90: 0, 120: -0.5, 180: -1, 240: -0.5, 270: 0, 300: 0.5}
tans = {
    0: 0,
    45: 1,
    90: "Not defined",
    135: -1,
    180: 0,
    225: -1,
    270: "Not defined",
    315: -1
}
cots = {
    0: "Not defined",
    45: 1,
    90: 0,
    135: -1,
    180: "Not defined",
    225: -1,
    270: 0,
    315: -1
}


def sin(x):
    if x % 360 in sins.keys():
        return sins[x % 360]
    else:
        return sinus(radians(x))


def cos(x):
    if x % 360 in coss.keys():
        return coss[x % 360]
    else:
        return cosinus(radians(x))


def tan(x):
    if x % 180 in tans.keys():
        return tans[x % 180]
    else:
        return tanges(radians(x))


def cot(x):
    if x % 180 in cots.keys():
        return cots[x % 180]
    else:
        return 1 / tanges(radians(x))


def log(b, a):
    return logaritm(a, b)


def GCD(a, b):
    if (b == 0):
        return a
    else:
        return GCD(b, a % b)


def LCM(a, b):
    return int(a * b / GCD(a, b))


def R(a, b):
    return f"{divmod(a,b)[0]}, R = {divmod(a,b)[1]}"


def nAr(n, r):
    return int(factorial(n) / factorial(n - r))


def nCr(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n - r)))


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = []
        self.lbl = Label(
            text="".join(self.formula),
            font=("Times New Roman", 25, "bold"),
            bg="#ececec",
            foreground="#000")
        self.lbl.place(x=11, y=50)

        btns = [
            "C", "DEL", "MS", "MR", "M+", "MC", "nCr", "1", "2", "3", "*", "/",
            "!", "nAr", "4", "5", "6", "+", "-", "%", ":R", "7", "8", "9", "(",
            ",", ")", "π", "x", "0", "X^2", "x^(-1)", "X^0.5", "x^y", "e",
            "sinx", "cosx", "tanx", "cotx", "log", "GCD", "LCM",
            "Solve quadeq", "Graph", "DEC", "BIN", "HEX", "OCT", "="
        ]

        x = 0
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            if bt.isdigit():
                Button(
                    text=bt,
                    bg="#f4f4f4",
                    borderwidth=0,
                    font=("Times New Roman", 15),
                    command=com).place(
                        x=x, y=y, width=115, height=79)
            else:
                Button(
                    text=bt,
                    bg="#fbfbfb",
                    borderwidth=0,
                    font=("Times New Roman", 15),
                    command=com).place(
                        x=x, y=y, width=115, height=79)
            x += 118
            if x > 750:
                x = 0
                y += 81

    def logicalc(self, operation):
        global mem
        global base
        if operation == "C":
            self.formula = []
        elif operation == "DEL":
            self.formula = self.formula[0:-1]

        elif operation == "MS":
            mem = float(eval("".join(self.formula)))
            self.formula = []
        elif operation == "MR":
            self.formula.append(str(mem))
        elif operation == "M+":
            mem += float(eval("".join(self.formula)))
            self.formula = []
        elif operation == "MC":
            mem = ""
        elif operation == "X^2":
            base = 10
            self.formula.append("**2")
        elif operation == "=":
            a = "".join(self.formula)
            if "%" in a:
                a = a.replace("%", "/100")
            if "!" in a:
                a = a.replace("!", "**Fa")

            try:
                self.formula = [str(eval(a))]
            except:
                self.formula = ["ERROR"]
        elif operation == "x^y":
            base = 10
            self.formula.append("**")
        elif operation == "x^(-1)":
            base = 10
            self.formula.append("**(-1)")
        elif operation == "log":
            base = 10
        elif operation in "0123456789":
            self.formula.append(operation)
        elif operation == "X^0.5":
            base = 10
            self.formula.append("**0.5")
        elif operation == "!":
            base = 10
            self.formula.append("!")
        elif operation == "Graph":
            base = 10
            try:
                self.graphi()
            except:
                self.formula = [
                    "I can only graph polynomials and exponentials"
                ]
        elif operation == "Solve quadeq":
            base = 10
            self.quadraticsolve()
        elif operation == "sinx":
            base = 10
            self.formula.append("sin(")
        elif operation == "cosx":
            base = 10
            self.formula.append("cos(")
        elif operation == "tanx":
            base = 10
            self.formula.append("tan(")
        elif operation == "cotx":
            base = 10
            self.formula.append("cot(")
        elif operation == "GCD":
            base = 10
            self.formula.append("GCD(")
        elif operation == "LCM":
            base = 10
            self.formula.append("LCM(")
        elif operation == ":R":
            base = 10
            self.formula.append("R(")
        elif operation == "nCr":
            base = 10
            self.formula.append("nCr(")
        elif operation == "nAr":
            base = 10
            self.formula.append("nAr(")
        elif operation == "BIN":
            if self.formula:
                if base == 10:
                    self.formula = [bin(int("".join(self.formula)))[2:]]
                elif base == 8:
                    a = int("".join(self.formula), 8)
                    self.formula = [bin(int(a))[2:]]
                elif base == 16:
                    a = int("".join(self.formula), 16)
                    self.formula = [bin(int(a))[2:]]
            base = 2

        elif operation == "HEX":
            if self.formula:
                if base == 10:
                    self.formula = [hex(int("".join(self.formula)))[2:]]
                elif base == 8:
                    a = int("".join(self.formula), 8)
                    self.formula = [hex(int(a))[2:]]
                elif base == 2:
                    a = int("".join(self.formula), 2)
                    self.formula = [hex(int(a))[2:]]
            base = 16
        elif operation == "DEC":
            if self.formula:
                self.formula = [str(int("".join(self.formula), base))]
            base = 10
        elif operation == "OCT":
            if self.formula:
                if base == 10:
                    self.formula = [oct(int("".join(self.formula)))[2:]]
                elif base == 2:
                    a = int("".join(self.formula), 2)
                    self.formula = [oct(int(a))[2:]]
                elif base == 16:
                    a = int("".join(self.formula), 16)
                    self.formula = [oct(int(a))[2:]]
            base = 8
        else:
            base = 10
            self.formula.append(operation)
        self.update()

    def update(self):
        self.lbl.configure(text="".join(self.formula))

    def graphi(self):
        inp = Tk()
        inp["bg"] = "#fff"
        inp.geometry("130x100+200+200")
        inp.title("")
        inp.resizable(False, False)
        Label(inp, text="Enter Range", bg="#fff").grid(row=1, column=1)
        self.r1 = Entry(inp)
        self.r2 = Entry(inp)
        self.r1.grid(row=2, column=1)
        self.r2.grid(row=3, column=1)
        Button(inp, text='Graph', command=self.graph).grid(row=4, column=1)

    def graph(self):
        fig = plt.figure()
        try:
            x = np.linspace(float(self.r1.get()), float(self.r2.get()))
            y = lambda x: eval("".join(self.formula))
            ax = fig.add_subplot(111)
            ax.set_title('Function ' + "".join(self.formula))
            ax.plot(x, y(x))
        except:
            self.formula = ["ERROR"]
            return

        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        fig.show()

    def quadraticsolve(self):
        inp = Tk()
        inp["bg"] = "#fff"
        inp.geometry("150x110+200+200")
        inp.title("Coeficients")
        inp.resizable(False, False)
        Label(inp, text="a", bg="#fff").grid(row=1, column=1)
        Label(inp, text="b", bg="#fff").grid(row=2, column=1)
        Label(inp, text="c", bg="#fff").grid(row=3, column=1)
        self.e1 = Entry(inp)
        self.e2 = Entry(inp)
        self.e3 = Entry(inp)
        self.e1.grid(row=1, column=3)
        self.e2.grid(row=2, column=3)
        self.e3.grid(row=3, column=3)
        Button(inp, text='Solve', command=self.solveq).grid(row=4, column=3)
        inp.mainloop()

    def solveq(self):
        a = float(self.e1.get())
        if a == 0:
            messagebox.showinfo("Solution", "Error: It's not a quadratic!!")
            return
        b = float(self.e2.get())
        c = float(self.e3.get())
        D = b**2 - 4 * a * c
        x0 = -b / (2 * a)
        y0 = -D / (4 * a)
        if D > 0:
            X1 = (-b + D**0.5) / (2 * a)
            X2 = (-b - D**0.5) / (2 * a)
            t = f"D = {D}:  X1 = {X1}:  X2 = {X2}"
        elif D == 0:
            X = (-b) / (2 * a)
            t = f"D = {D}:  X = {X}"
        else:
            t = "No roots"
        t += f"\n x0 = {x0} y0 = {y0}"
        messagebox.showinfo("Solution", t)


if __name__ == '__main__':
    root = Tk()
    root.iconbitmap("myIcon.ico")
    root["bg"] = "#ececec"
    root.geometry("825x705+200+200")
    root.title("Math Helper")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()
