class IteratorAttrs:
    __index = 0

    def __iter__(self):
        IteratorAttrs.__index = 0
        return self

    def __next__(self):
        if self.__index < len(self.__dict__):
            result = tuple(self.__dict__.items())[self.__index]
            IteratorAttrs.__index += 1
            return result
        raise StopIteration


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self._model = model
        self._size = size
        self._memory = memory

    def __setattr__(self, key, value):
        dict_types = {"_model": str, "_size": tuple, "_memory": int}
        if isinstance(value, dict_types[key]):
            object.__setattr__(self, key, value)
        else:
            raise TypeError


phone = SmartPhone('nokia', (10, 5), 8)

# print(len(phone.__dict__))

# iterator = iter(phone)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

for key, value in phone:
    print(key, value)