from abc import ABC


class MovieAbstract(ABC):

    def __init__(self, name: str, date: int, lieu=None):
        self.name = name
        self.date = date
        self.lieu = lieu

    def __str__(self) -> str:
        return f"{self.name} ({self.date})"

    def __repr__(self) -> str:
        return str(self)
