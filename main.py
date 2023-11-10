class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def input_data(self):
        self.num1 = int(input("Введите первое число: "))
        self.num2 = int(input("Введите второе число: "))

    def sum(self):
        return self.num1 + self.num2

    def difference(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 == 0:
            print("Деление на ноль невозможно")
        else:
            return self.num1 / self.num2


calc = Calculator(0, 0)
calc.input_data()
print("Сумма чисел:", calc.sum())
print("Разность чисел:", calc.difference())
print("Произведение чисел:", calc.multiplication())
print("Частное чисел:", calc.division())