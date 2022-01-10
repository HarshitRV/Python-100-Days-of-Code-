import math

class Calculator:
    def __init__(self):
        self.result = 0
        self.another_num = 0
        self.operation = ""

    def add(self, a, b):
        self.result = a + b
        return self.result

    def sub(self, a, b):
        self.result =  a-b
        return self.result

    def mul(self, a, b):
        self.result = a * b
        return self.result

    def div(self, a, b):
        self.result =  a / b
        return self.result

    def log(self, a):
        self.result = math.log(a)
        return self.result

    def factorial(self, a):
        self.result =  math.factorial(int(a))
        return self.result

    def exponent(self, a):
        self.result =  math.exp(a)
        return self.result

    def power(self, a, b):
        self.result =  math.pow(a, b)
        return self.result

    def sqare_root(self, a):
        self.result =  math.sqrt(a)
        return self.result