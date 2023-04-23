from enum import Enum


class Operator(Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    @classmethod
    def list(cls):
        return [_ for _ in Operator]
