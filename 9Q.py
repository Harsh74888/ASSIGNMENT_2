# write a python program to create class name claculator with method of basic
#  arthmetic operation like add,subtract,multiply and divide also opererator 
# overloading by defining special methods like add,sub,mul and truediv for the calculator class 
class Calculator:
    def __init__(self, value):
        self.value = value

    def add(self, other):
        return self.value + other

    def subtract(self, other):
        return self.value - other

    def multiply(self, other):
        return self.value * other

    def divide(self, other):
        if other != 0:
            return self.value / other
        else:
            return "Cannot divide by zero."

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __mul__(self, other):
        return self.value * other

    def __truediv__(self, other):
        if other != 0:
            return self.value / other
        else:
            return "Cannot divide by zero."

# Create a Calculator object
calc = Calculator(10)

# Using methods for basic arithmetic operations
print("Addition:", calc.add(5))
print("Subtraction:", calc.subtract(3))
print("Multiplication:", calc.multiply(4))
print("Division:", calc.divide(2))

# Using operator overloading
print("Operator Overloading - Addition:", calc + 5)
print("Operator Overloading - Subtraction:", calc - 3)
print("Operator Overloading - Multiplication:", calc * 4)
print("Operator Overloading - Division:", calc / 2)
