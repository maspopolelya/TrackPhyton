if __name__ == "__main__":
    class Predators:

        """Базовый класс Хищники."""

        def __init__(self, average_weight: float, prey: str):
            """
            Создание и подготовка к работе класса "Хищники"

            :param average_weight: Средний вес особи.
            :param prey: Наименование добычи, чем питается хищник.
            """
            self.average_weight = average_weight
            self.prey = prey

        def hunting_skills(self, average_weight: float) -> int:
            """
            Функция, оценивающая навыки охоты хищника в зависимости от веса.
            Возвращает значение от 0 до 10, где 0 - навык охоты молодой, нетяжелой особи.

            :param average_weight: Средний вес особи.
            """
            ...

        def production_limit(self, population: int, amount_of_production: int) -> int:
            """
            Функция, показывающая предел добычи хищника в следующий сезон
            :param population: Популяция хищника в мире.
            :param amount_of_production: Количество добычи хищника за прошлый сезон.
            """
            ...

        def __str__(self):
            return f"Средний вес хищника {self.average_weight}, добыча, на которую охотится хищник {self.prey}"

        def __repr__(self):
            return f"{self.__class__.__name__}(average_weight = {self.average_weight}, prey = {self.prey}"

    class Tuna(Predators):

        "Дочерний класс Тунец"

        def __init__(self, average_weight: float, prey: str, habitat_depth: float):
            """
            Расширяет конструктор базового класса: добавляет глубину обитания
            :param average_weight: Средний вес тунца.
            :param prey: Наименование добычи, чем питается тунец.
            :param habitat_depth: Глубина обитания.
            """
            super().__init__(average_weight, prey)
            self.habitat_depth = habitat_depth

        def __str__(self):
            """Расширяет строковое предствление, добавляя информацию о глубине обитания тунца"""
            return f"Средний вес тунца {self.average_weight}, добыча, на которую охотится тунец {self.prey}, глубина обитания {self.habitat_depth}"

        def __repr__(self):
            """Расширяет официальное преставление с учетом новых атрибутов"""
            return f"{self.__class__.__name__}(average_weight = {self.average_weight}, prey = {self.prey}, habitat_depth = {self.habitat_depth}"
    pass
