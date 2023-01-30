import math
# 1. Створіть клас «Прямокутник», у якого є два поля (ширина і висота). Реалізуйте метод порівняння прямокутників за площею.
# Також реалізуйте методи складання прямокутників (площа сумарного прямокутника повинна дорівнювати сумі площ прямокутників, які ви складаєте).
# Реалізуйте методи множення прямокутника на число n (це має збільшити площу базового прямокутника в n разів).

class Box:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __volume(self):
        return self.x * self.y

    def add(self, other):
        return self.__volume() + other.__volume()

    def __mul__(self, n):
        return self * n

    def __lt__(self, other):
        return self.__volume() < other.__volume()

    def __eq__(self, other):
        return self.__volume() < other.__volume()

    def __ge__(self, other):
        return self.__volume() == other.__volume()

    def __le__(self, other):
        return self.__volume() <= other.__volume()

    def __gt__(self, other):
        return self.__volume() >= other.__volume()

    def __ne__(self, other):
        return self.__volume() != other.__volume()

    def __str__(self):
        return f'{self.x}x{self.y}'


x_1 = Box(2, 3)
x_2 = Box(6, 2)
x_add = Box.add(x_1, x_2)

print(x_1 < x_2)
print(x_1 > x_2)
print(x_add * 5)

#2. Створіть клас «Правильна дроба» та реалізуйте методи порівняння, додавання,
# віднімання та множення для екземплярів цього класу.

class Correct_fraction:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0

    def __gt__(self, other):
        if self.y == other.y and self.x > other.x:
            return self.x > other.x
        if self.y < other.y:
            return True
        if self.y > other.y:
            return False

    def __lt__(self, other):
        if self.y == other.y and self.x < other.x:
            return self.x < other.x
        if self.y > other.y:
            return True
        if self.y < other.y:
            return False

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __add__(self, other):
        if self.x == other.x and self.y == other.y:
            return 1
        if self.x == self.y:
            if (other.x % other.y) == 0:
                return f'{1} {other.x}/{other.y}'
            if (other.x % other.y) != 0:
                return f'{1}  {int(other.x/math.gcd(other.x, other.y))}/{int(other.y/math.gcd(other.x, other.y))}'
        if other.x == other.y:
            if (self.x % self.y) == 0:
                return f'{1} {self.x}/{self.y}'
            if (self.x % self.y) != 0:
                return f'{1}  {int(self.x/math.gcd(self.x, self.y))}/{int(self.y/math.gcd(self.x, self.y))}'
        if self.y == other.y:
            if ((self.x + other.x) % other.y) == 0:
                return f'{self.x + other.x}/{other.y}'
            if ((self.x + other.x) % other.y) != 0:
                return f'{math.gcd(self.x + other.x, other.y)}  {int((self.x + other.x)/math.gcd(self.x + other.x, other.y))}/{int((other.y)/math.gcd(self.x + other.x, other.y))}'
        if self.y != other.y:
            if (self.x % self.y) == 0:
                self.x = int(self.x / (math.gcd(self.x, self.y)))
                self.y = int(self.y / (math.gcd(self.x, self.y)))
                if self.x/self.y == self.x:
                    return f'{self.x} {int(other.x/(math.gcd(other.x, other.y)))}/{int(other.y/(math.gcd(other.x, other.y)))}'
            if (other.x % other.y) == 0:
                other.x = int(other.x / (math.gcd(other.x, other.y)))
                other.y = int(other.y / (math.gcd(other.x, other.y)))
                if other.x/other.y == other.x:
                    return f'{other.x} {int(self.x/(math.gcd(self.x, self.y)))}/{int(self.y/(math.gcd(self.x, self.y)))}'
            self.x1 = self.x * other.y
            self.x2 = self.y * other.y
            self.y1 = other.x * self.y
            self.y2 = other.y * self.y
            t = self.x1 + self.y1
            c = self.y2
            if math.gcd(t, c) == t and math.gcd(t, c) == c:
                return 1
            if math.gcd(t, c) == 1:
                return f'{t}/{c}'
            else:
                return f'{math.gcd(t, c)} {int(t/math.gcd(t, c))}/{int(c/math.gcd(t, c))}'

    def __sub__(self, other):
        if self.y == other.y:
            return f'{self.x + other.x}/{other.y}'
        if self.y != other.y:
            self.y1 = self.x * other.y
            self.y2 = self.y * other.y
            self.x1 = other.x * self.y
            self.x2 = other.y * self.y
            t = self.x1 - self.y1
            c = self.y2
            if math.gcd(t, c) == t and math.gcd(t, c) == c:
                return '1'
            if math.gcd(t, c) == 1:
                return f'{t}/{c}'
            else:
                return f'{math.gcd(t, c)} {int(t/math.gcd(t, c))}/{int(c/math.gcd(t, c))}'

    def __mul__(self, other):
        self.x1 = int(self.x / math.gcd(self.x, self.y))
        self.x2 = int(self.y / math.gcd(self.x, self.y))
        self.y1 = int(other.x / math.gcd(other.x, other.y))
        self.y2 = int(other.y / math.gcd(other.x, other.y))
        if math.gcd(self.y, other.x) > 1:
            self.x2 = int(self.y / math.gcd(self.y, other.x))
            self.y1 = int(other.x / math.gcd(self.y, other.x))
        if math.gcd(self.x, other.y) > 1:
            self.x1 = int(self.x / math.gcd(self.x, other.y))
            self.y2 = int(other.y / math.gcd(self.x, other.y))
        if (self.x1 * self.y1) > (self.x2 * self.y2) and math.gcd(self.x1 * self.y1, self.x2 * self.y2) == 1:
            return f'{(self.x1 * self.y1)//(self.x2 * self.y2)} {(self.x1 * self.y1)%(self.x2 * self.y2)}/{self.x2 * self.y2}'
        return f'{self.x1 * self.y1}/{self.x2 * self.y2}'

drib1 = Correct_fraction(35, 8)
drib2 = Correct_fraction(12, 7)
drib = drib1 * drib2
print(drib)
