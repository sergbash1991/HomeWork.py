class Thing:
    def __init__(self, name, price, weight):
        self._name = name
        self._price = price
        self._weight = weight

    def __setattr__(self, key, value):
        dict_types = {"_name": str, "_price": float, "_weight": float}
        if isinstance(value, dict_types[key]):
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Name must be string; price and weight must be float")

