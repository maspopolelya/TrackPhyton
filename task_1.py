class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    """Свойства атрибутов name и author"""
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть строкового типа")
        self._name = name

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, author: str) -> None:
        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкового типа")
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """Бумажная книга"""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    """Свойства атрибута pages"""
    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, correct_pages: int) -> None:
        if not isinstance(correct_pages, int):
            raise TypeError("Число страниц должно быть целочисленного типа")
        if correct_pages < 0:
            raise ValueError("Число страниц должно быть больше 0")
        self._pages = correct_pages

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Количество страниц: {self._pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}), pages={self._pages!r}"


class AudioBook(Book):
    """Аудиокнига"""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    """Свойства атрибута duration"""
    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, correct_duration: float) -> None:
        if not isinstance(correct_duration, float):
            raise TypeError("Продолжительность аудиокниги должна быть числом с плавающей запятой")
        if correct_duration < 0:
            raise ValueError("Продолжительность аудиокниги должна быть больше 0")
        self._duration = correct_duration

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Продолжительность {self._duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}), duration={self._duration!r}"


if __name__ == "__main__":
    paper = PaperBook("Война и мир", "Толстой", 2000)
    print(paper)
    print(repr(paper))
    print()

    audioo = AudioBook("Война и мир", "Толстой", 10.1)
    print(audioo)
    print(repr(audioo))
    print()

    book = Book("Война и мир", "Толстой")
    print(book)
    print(repr(book))
