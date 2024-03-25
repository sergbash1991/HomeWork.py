class Planet:
    def __init__(self, name, diametr, period_solar, period):
        self._name = name
        self._diametr = diametr
        self._period_solar = period_solar
        self._period = period

    def __setattr__(self, key, value):
        dict_types = {"_name": str, "_diametr": int | float, "_period_solar": float, "_period": int | float}
        if dict_types[key] == value:
            if key in ("_diametr", "_period_solar", "_period") and value <= 0:
                raise ValueError("Diameter, period solar and period must be positive")
            object.__setattr__(self, key, value)


class SolarSystem:
    __instance = None

    __slots__ = ('_mercury', '_venus', '_earth', '_mars', '_jupiter', '_saturn', '_uranus', '_neptune')

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance._mercury = Planet("Меркурий", 4879, 87.969, 58.646)
            cls.__instance._venus = Planet("Венера", 12104, 224.701, 243.025)
            cls.__instance._earth = Planet("Земля", 12742, 365.256, 1.0)
            cls.__instance._mars = Planet("Марс", 6792, 686.971, 1.025)
            cls.__instance._jupiter = Planet("Юпитер", 142984, 4332.59, 0.412)
            cls.__instance._saturn = Planet("Сатурн", 120536, 10759.22, 0.428)
            cls.__instance._uranus = Planet("Уран", 51118, 30688.5, 0.718)
            cls.__instance._neptune = Planet("Нептун", 49528, 60182, 0.671)
        return cls.__instance


solar_system = SolarSystem()
print(solar_system)

