import doctest
from typing import Union


class Kettle:
    def __init__(self, type_of_kettle: str, capacity_volume: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Чайник"

        :param type_of_kettle: Тип чайника
        :param capacity_volume: Объем чайника, л

        Пример:
        >>> kettle = Kettle("Электрический", 0.5) # инициализация экземпляра класса
        """
        if not isinstance(type_of_kettle, str):
            raise TypeError("Тип чайника должен быть типа str")
        self.type_of_kettle = type_of_kettle

        if not isinstance(capacity_volume, (int,float)):
            raise TypeError("Объем чайника должен быть типа int или float")
        if capacity_volume < 0:
            raise ValueError("Объем чайника не может быть отрицательным числом")
        self.capacity_volume = capacity_volume

    def add_water_to_kettle(self, water: float) -> None:
        """
        Добавление воды в чайник
        :param water: Объем добавляемой воды

        :raise ValueError: Если количество добавляемой воды превышает свободное место в чайнике, то вызываем ошибку

        Пример:
        >>> kettle = Kettle("Газовый", 1)
        >>> kettle.add_water_to_kettle(0.3)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая вода должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая вода должна быть положительным числом")
        ...
    def count_of_cups(self, cup_volume: Union[int, float]) -> int:
        """
        Разлитие кипятка по кружкам

        :param cup_volume: Объем кружки, л

        :raise ValueError: Если объем кружки превышает объем чайника, то возвращается ошибка.

        Пример:
        >>> kettle = Kettle("Электрический", 1)
        >>> kettle.count_of_cups(0.25)
        """
        ...

class Flat:
    def __init__(self, length: float, width: float, height: float):
        """
        Создание и подготовка к работе "Квартира"

        :param length: Длина квартиры, м
        :param width: Ширина квартиры, м
        :param height: Высота квартиры, м

        Пример:
        flat = Flat(7, 6, 3) # инициализация экземпляра класса
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина квартиры должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина квартиры должна быть положительным числом")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина квартиры должна быть типа int или float")
        if width <= 0:
            raise ValueError("Ширина квартиры должна быть положительным числом")
        self.width = width

        if not isinstance(height, (int, float)):
            raise TypeError("Высота квартиры должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота квартиры должна быть положительным числом")
        self.height = height

    def volume_calculation(self) -> float:
        """
        Расчет объема квартиры.

        :return: Объем заданной квартиры

        Примеры:
        >>> flat = Flat(7, 5, 2.4)
        >>> flat.volume_calculation()
        """
        ...

    def coverage_area(self) -> float:
        """
        Расчет площади стен для отделки.

        :return: Площадь всех стен

        Пример:
        >>> flat = Flat(7, 5, 3)
        >>> flat.coverage_area()
        """
        ...
    def cabinet(self, cabinet_hight: float, cabinet_length: float) -> bool:
        """
        Функция, проверяющая влезет ли шкаф в квартиру

        :param cabinet_hight: Высота шкафа
        :param cabinet_length: Длина шкафа

        :return: Подойдет ли шкаф для заданной квартиры

        Пример:
        >>> flat = Flat(7, 5, 2.5)
        >>> flat.cabinet(2.8, 3)
        """
        ...

class Hairstyle:
    def __init__(self, colour: str, length: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Прическа"

        :param colour: Цвет
        :param length: Длина волос, см

        Пример:
        >>> hairstyle = Hairstyle("Русый", 80) # инициализация экземпляра класса
        """
        if not isinstance(colour, str):
            raise TypeError("Цвет должен быть типа str")
        self.colour = colour

        if not isinstance(length, (int, float)):
            raise TypeError("Длина должна быть типа int или float")
        if length <= 0:
            raise ValueError("Длина должна быть положительной, либо равна нулю")
        self.length = length

    def haircut(self, haircut_length: Union[int, float]) -> int:
        """
        Функция, которая укорачивает длину волос.

        :param haircut_length: Длина стрижки

        :raise ValueError: Если длина стрижки, больше чем длина волос, то возвращается ошибка.

        Пример:
        >>> hairstyle = Hairstyle("Русый", 80)
        >>> hairstyle.haircut(20)
        """
        ...

    def hair_extensions(self, hair_extensions_length: Union[int, float]) -> int:
        """
        Функция, которая увеличивает длину волос.

        :param hair_extensions_length: Длина наращивания

        Пример:
        >>> hairstyle = Hairstyle("Русый", 80)
        >>> hairstyle.hair_extensions(20)
        """
        ...


if __name__ == "__main__":
    doctest.testmod() # тестирование примеров, которые находятся в документации
    pass
