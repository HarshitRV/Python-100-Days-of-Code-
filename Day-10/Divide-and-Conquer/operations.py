from calc import Calculator

c = Calculator()

class Operations:
    def __init__(self):
        self.operations = {
        "+" : c.add,
        "-" : c.sub,
        "*" : c.mul,
        "/" : c.div,
        "!" : c.factorial,
        "log": c.log,
        "pow":c.power,
        "sqrt": c.sqare_root,
        "exp": c.exponent,
        "summation": c.summation
    }
