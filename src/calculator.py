class Calculator:
    def __init__(self, op1: float, op2: float):
        self.op1 = op1
        self.op2 = op2

    def sum(self):
        return self.op1 + self.op2
    def subtract(self):
        return self.op1 - self.op2
    def multiply(self):
        return self.op1 * self.op2
    def divide(self):
        if self.op2 != 0:
            return self.op1 / self.op2
        else:
            raise ZeroDivisionError('Nie dziel przez zero')


calculator = Calculator(2,3)
print(calculator.sum())