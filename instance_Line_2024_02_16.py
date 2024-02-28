# Объявите класс Line, объекты которого создаются командой:
#
# line = Line(x1, y1, x2, y2)
# где x1, y1, x2, y2 - координаты начала линии (x1, y1) и координаты конца линии (x2, y2).
# Могут быть произвольными числами.
# В объектах класса Line должны создаваться соответствующие локальные атрибуты с именами x1, y1, x2, y2.
#
# В классе Line определить магический метод len() так, чтобы функция:
#
# bool(line)
# возвращала False, если длина линии меньше 1.

import math
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self):
        res = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        return int(res)

    def __bool__(self):
        return self.__len__() > 1

line1 = Line(1, 1, 1, 2)
print(len(line1))
print(bool(line1))