from typing import List


class Digits:
    def __init__(self, options: List[int], goal: int):
        self.options = options
        self.goal = goal

    def __str__(self):
        return "{} -> {}".format(self.options, self.goal)

    def __repr__(self):
        return "{} -> {}".format(self.options, self.goal)


