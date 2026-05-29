import random
from turtle import *

class Figure:
    def __init__(self, x, y, color):
        self._x=x
        self._y=y
        self._visible=False
        self._color=color
    def _draw(self, color):
        pass
    def show(self):
        if not self._visible:
            self._visible=True
            self._draw(self._color)
    def hide(self):
        if self._visible:
            self._visible=False
            self._draw(bgcolor())
    def move(self, dx, dy):
        isVisible=self._visible
        if isVisible:
            self.hide()
        self._x+=dx
        self._y+=dy
        if isVisible:
            self.show()

class Circle(Figure):
    def __init__(self, x, y, r, color):
        super().__init__(x, y, color)
        self._r=r
    def _draw(self, color):
        pencolor(color)
        up()
        setpos(self._x, self._y - self._r)
        down()
        circle(self._r)
        up()

class Rectangle(Figure):
    def __init__(self, x, y, a, b, color):
        super().__init__(x, y, color)
        self._a=a
        self._b=b
    def _draw(self, color):
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        for _ in range(2):
            forward(self._a)
            left(90)
            forward(self._b)
            left(90)
        up()

class Square(Rectangle):
    def __init__(self, x, y, a, color):
        super().__init__(x, y, a, a, color)

class Triangle(Figure):
    def __init__(self, x, y, a, color):
        super().__init__(x, y, color)
        self._a=a
    def _draw(self, color):
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        for _ in range(3):
            forward(self._a)
            left(120)
        up()

class Trapezoid(Figure):
    def __init__(self, x, y, a, b, h, color):
        super().__init__(x, y, color)
        self._a=a
        self._b=b
        self._h=h
    def _draw(self, color):
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        indent=(self._a-self._b)/2
        forward(self._a)
        goto(self._x+self._a-indent, self._y+self._h)
        goto(self._x+indent, self._y+self._h)
        goto(self._x, self._y)
        up()

class Car:
    def __init__(self, x, y, color="black"):
        self.body=Rectangle(x, y, 160, 40, color)
        self.cabin=Trapezoid(x + 20, y + 40, 110, 70, 30, color)
        self.window=Square(x + 60, y + 45, 20, color)
        self.wheel1=Circle(x + 30, y, 15, color)
        self.wheel2=Circle(x + 130, y, 15, color)
        self.parts=[self.body, self.cabin, self.window, self.wheel1, self.wheel2]
    def show(self):
        for part in self.parts:
            part.show()
    def hide(self):
        for part in self.parts:
            part.add_shape=part.hide()
    def move(self, dx, dy):
        for part in self.parts:
            part.hide()
        for part in self.parts:
            part._x+=dx
            part._y+=dy
        for part in self.parts:
            part.show()

if __name__=='__main__':
    screen = Screen()
    screen.setup(900, 700)
    home()
    speed(0)
    delay(0)
    ht()
    print("--- 1. Перевірка базових класів з шаблону ---")
    c=Circle(120, 120, 50, "blue")
    c.show()
    c.move(-30, -140)
    c.hide()
    s=Square(0, 0, 150, "red")
    s.show()
    s.move(0, 140)
    s.hide()
    t=Triangle(120, 120, 50, "blue")
    t.show()
    t.move(-30, -140)
    t.hide()
    trap=Trapezoid(120, 120, 80, 40, 30, "magenta")
    trap.show()
    trap.move(-30, -140)
    trap.hide()
    rect=Rectangle(120, 120, 80, 40, "green")
    rect.show()
    rect.move(-30, -140)
    rect.hide()
    print("--- 2. Демонстрація роботи класу Автомобіль ---")
    car = Car(-300, -200, "purple")
    car.show()
    for _ in range(15):
        car.move(30, 10)
    print("--- 3. Генерація 100 випадкових фігур ---")
    colors=["red", "blue", "green", "orange", "purple", "brown", "cyan", "magenta"]
    random_figures=[]
    for _ in range(100):
        fig_type=random.choice(["circle", "rectangle", "square", "triangle", "trapezoid"])
        x=random.randint(-400, 400)
        y=random.randint(-300, 300)
        color=random.choice(colors)
        if fig_type=="circle":
            r=random.randint(10, 50)
            fig=Circle(x, y, r, color)
        elif fig_type=="rectangle":
            a=random.randint(20, 100)
            b=random.randint(20, 100)
            fig=Rectangle(x, y, a, b, color)
        elif fig_type=="square":
            a=random.randint(20, 80)
            fig=Square(x, y, a, color)
        elif fig_type=="triangle":
            a=random.randint(20, 100)
            fig=Triangle(x, y, a, color)
        elif fig_type=="trapezoid":
            a=random.randint(40, 100)
            b=random.randint(10, 30)
            h=random.randint(20, 60)
            fig=Trapezoid(x, y, a, b, h, color)
        random_figures.append(fig)
    for fig in random_figures:
        fig.show()
    mainloop()
