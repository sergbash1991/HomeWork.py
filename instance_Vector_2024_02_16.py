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
        for i, arg in enumerate(args):
            pass