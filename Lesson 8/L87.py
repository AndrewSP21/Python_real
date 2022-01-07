'''7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата. '''


class ComplexDigit:
    def __init__(self, a, b):
        self.x = complex(a, b)

    def __str__(self):
        return str(self.x)

    def __add__(self, other):
        y = self.x + other.x
        return ComplexDigit(y.real, y.imag)


e = ComplexDigit(1, 2)
s = ComplexDigit(3, 4)
print(e)
