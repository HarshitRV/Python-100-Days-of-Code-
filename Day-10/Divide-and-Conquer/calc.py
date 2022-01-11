import math

class Calculator:
    def __init__(self):
        self.result = 0
        self.another_num = 0
        self.operator = ""
        self.operations = {
            "+" : self.add,
            "-" : self.sub,
            "*" : self.mul,
            "/" : self.div,
            "!" : self.factorial,
            "log": self.log,
            "pow": self.power,
            "sqrt": self.sqare_root,
            "exp": self.exponent,
            "summation": self.summation
        }

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

    def summation(self, a, b):
        for i in range(int(a), int(b+1)):
            self.result += i
        return self.result