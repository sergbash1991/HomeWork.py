# Объявите в программе класс Vector, объекты которого создаются командой:
#
# v = Vector(x1, x2, x3,..., xN)
# где x1, x2, x3,..., xN - координаты вектора (числа: целые или вещественные).
#
# С каждым объектом класса Vector должны выполняться операторы:
#
# v1 + v2 # суммирование соответствующих координат векторов
# v1 - v2 # вычитание соответствующих координат векторов
# v1 * v2 # умножение соответствующих координат векторов
#
# v1 += 10 # прибавление ко всем координатам вектора числа 10
# v1 -= 10 # вычитание из всех координат вектора числа 10
# v1 += v2
# v2 -= v1
#
# v1 == v2 # True, если соответствующие координаты векторов равны
# v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает
# При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с новыми (вычисленными) координатами.
# При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.
#
# Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -, * должно генерироваться исключение командой:
#
# raise ArithmeticError('размерности векторов не совпадают')

class Vector:
    def __init__(self, *args):
        self.coords = []
        for arg in args:
            if isinstance(arg, int | float):
                self.coords.append(arg)
            else:
                raise TypeError('Type must be int or float')

    def __add__(self, other):
        new_coords = []
        if len(self.coords) > len(other.coords):
            for i in range(len(other.coords)):
                new_coords.append(sum([self.coords[i], other.coords[i]]))
            for j in range(len(other.coords), len(self.coords)):
                new_coords.append(self.coords[j])
        elif len(self.coords) < len(other.coords):
            for i in range(len(self.coords)):
                new_coords.append(sum([self.coords[i], other.coords[i]]))
            for j in range(len(self.coords), len(other.coords)):
                new_coords.append(other.coords[j])
        else:
            for i in range(len(other.coords)):
                new_coords.append(sum([self.coords[i], other.coords[i]]))
        return Vector(*new_coords)


    def __sub__(self, other):
        new_coords = []
        if len(self.coords) > len(other.coords):
            for i in range(len(other.coords)):
                new_coords.append(self.coords[i] - other.coords[i])
            for j in range(len(other.coords), len(self.coords)):
                new_coords.append(self.coords[j])
        elif len(self.coords) < len(other.coords):
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] - other.coords[i])
            for j in range(len(self.coords), len(other.coords)):
                new_coords.append(other.coords[j])
        else:
            for i in range(len(other.coords)):
                new_coords.append(self.coords[i] - other.coords[i])
        return Vector(*new_coords)

    def __mul__(self, other):
        new_coords = []
        if len(self.coords) > len(other.coords):
            for i in range(len(other.coords)):
                new_coords.append(self.coords[i] * other.coords[i])
            for j in range(len(other.coords), len(self.coords)):
                new_coords.append(self.coords[j])
        elif len(self.coords) < len(other.coords):
            for i in range(len(self.coords)):
                new_coords.append(self.coords[i] * other.coords[i])
            for j in range(len(self.coords), len(other.coords)):
                new_coords.append(other.coords[j])
        else:
            for i in range(len(other.coords)):
                new_coords.append(self.coords[i] * other.coords[i])
        return Vector(*new_coords)

    def __iadd__(self, other):
        if isinstance(other, Vector):
            return self + other
        elif isinstance(other, int | float):
            self.coords = [num + other for num in self.coords]
            return self

    def __isub__(self, other):
        if isinstance(other, Vector):
            return self - other
        elif isinstance(other, int | float):
            self.coords = [num - other for num in self.coords]
            return self

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.coords == other.coords

    def __ne__(self, other):
        if isinstance(other, Vector):
            return self.coords != other.coords


    def __str__(self):
        return str(self.coords)


v1 = Vector(1, 2, 3.5, -2)
v2 = Vector(2, 3)
v3 = v1 + v2
print(v3)
v4 = v1 - v2
print(v4)
v5 = v1 * v2
print(v5)
v1 += v2
print(v1)
print(v1 != v2)
