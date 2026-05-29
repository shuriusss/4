import math

class Triangle:
    def __init__(self, a, b, c):
        self.a=float(a)
        self.b=float(b)
        self.c=float(c)
    def perimeter(self):
        return self.a+self.b+self.c
    def area(self):
        p=self.perimeter()/2
        arg=p*(p-self.a)*(p-self.b)*(p-self.c)
        return arg**0.5 if arg>0 else 0.0

class Rectangle:
    def __init__(self, a, b):
        self.a=float(a)
        self.b=float(b)
    def perimeter(self):
        return 2*(self.a+self.b)
    def area(self):
        return self.a*self.b

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a=float(a)
        self.b=float(b)
        self.c=float(c)
        self.d=float(d)
    def perimeter(self):
        return self.a+self.b+self.c+self.d
    def area(self):
        if self.a==self.b:
            return 0.0
        try:
            num=((self.b-self.a)**2+self.c**2-self.d**2)
            den=2*(self.b-self.a)
            h_sq=self.c**2-(num/den)**2
            if h_sq>0:
                return 0.5*(self.a+self.b)*h_sq**0.5
        except ZeroDivisionError:
            pass
        return 0.0

class Parallelogram:
    def __init__(self, a, b, h):
        self.a=float(a)
        self.b=float(b)
        self.h=float(h)
    def perimeter(self):
        return 2*(self.a+self.b)
    def area(self):
        return self.a*self.h

class Circle:
    def __init__(self, r):
        self.r = float(r)
    def perimeter(self):
        return 2*math.pi*self.r
    def area(self):
        return math.pi*(self.r**2)

def process_shapes_file(file_path):
    shapes = []
    with open(file_path, 'r') as file:
        for line in file:
            tokens=line.strip().split()
            if not tokens:
                continue
            name=tokens[0]
            args=[float(x) for x in tokens[1:]]
            if name=="Triangle" and len(args)==3:
                    shapes.append(Triangle(*args))
            elif name=="Rectangle" and len(args)==2:
                    shapes.append(Rectangle(*args))
            elif name=="Trapeze" and len(args)==4:
                    shapes.append(Trapeze(*args))
            elif name=="Parallelogram" and len(args)==3:
                    shapes.append(Parallelogram(*args))
            elif name=="Circle" and len(args)==1:
                    shapes.append(Circle(*args))
    max_area_shape=max(shapes, key=lambda s: s.area())
    max_perimeter_shape=max(shapes, key=lambda s: s.perimeter())
    print(f"Результати для файлу {file_path}:\nФігура з найбільшою площею: {type(max_area_shape).__name__}\nПлоща цієї фігури: {max_area_shape.area():.2f}\nПериметр цієї фігури: {max_area_shape.perimeter():.2f}\nФігура з найбільшим периметром: {type(max_perimeter_shape).__name__}\nПлоща цієї фігури: {max_perimeter_shape.area():.2f}\nПериметр цієї фігури: {max_perimeter_shape.perimeter():.2f}")

files = ["input01.txt", "input02.txt", "input03.txt"]
for f in files:
    process_shapes_file(f)