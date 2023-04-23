from models import Operator


class Step:
    def __init__(self, operand1: int, operand2: int, operator: Operator):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operator = operator

    def __str__(self):
        return "{} {} {}".format(self.operand1, self.operator, self.operand2)

    def __repr__(self):
        return "{} {} {}".format(self.operand1, self.operator, self.operand2)

    @property
    def result(self):
        if self.operator == Operator.ADD:
            return self.operand1 + self.operand2
        elif self.operator == Operator.SUBTRACT:
            return self.operand1 - self.operand2
        elif self.operator == Operator.MULTIPLY:
            return self.operand1 * self.operand2
        elif self.operator == Operator.DIVIDE:
            return self.operand1 / self.operand2
