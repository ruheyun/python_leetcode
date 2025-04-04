import math


class Circle:
    def __init__(self, r):
        self.r = r
    def get_area(self):
        print(math.pi*self.r**2)
    def get_peri(self):
        print(2*math.pi*self.r)

r = float(input('请输入半径：'))
c = Circle(r)
c.get_area()
c.get_peri()