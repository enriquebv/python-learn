class Class:
    base = 2

    def multiply(self, n):
        return n * self.base


object = Class()

print(object.base)  # 2
print(object.multiply(2))  # 4

object.base = 4
print(object.multiply(2))  # 8


# Use __init__ special function to define the constructor
class ClassWithConstructor:
    base = None

    def __init__(self, base) -> None:
        self.base = base

    def multiply(self, n):
        return n * self.base


object = ClassWithConstructor(16)
print(object.multiply(2))  # 32
