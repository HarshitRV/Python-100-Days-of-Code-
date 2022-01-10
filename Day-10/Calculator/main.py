from calc import Calculator
from art import logo

print(logo)

c = Calculator()

operations = {
    "+" : c.add,
    "-" : c.sub,
    "*" : c.mul,
    "/" : c.div,
    "!" : c.factorial,
    "log": c.log,
    "power":c.power,
    "square root": c.sqare_root,
    "exponent": c.exponent
}

def calculate():
    def second_input(message, another=False):
        function = operations[op]
        if another:
            prev_num = c.result
            result = function(prev_num, c.another_num)
            print(f"{message} of {c.another_num} {op} {prev_num} =  {result}")
            init()
        else:
            b = float(input("Enter second num: "))
            result = function(a, b)
            print(f"{message} of {a} {op} {b} = : {result}")

    def single_input(message, another=False):
        function = operations[op]
        if another:
            result = function(c.result)
            print(f"{message} of {c.result} = : {result}")
        else:
            result = function(a)
            print(f"{message} of {a} = : {result}")

    def operation_performed(op, another=False):
        match op:   
            case "+":
                second_input("Addition", another)
            case "-":
                second_input("Subtraction", another)
            case "*":
                second_input("Multiplication", another)
            case "/":
                second_input("Division", another)
            case "!":
                single_input("Factorial", another)
            case "log":
                single_input("Log", another)
            case "power":
                second_input("Power", another)
            case "square root":
                single_input("Square Root", another)
            case "exponent":
                single_input("Exponent", another)
            case _:
                print("Invalid Choice")


    a = float(input("Enter first num: "))

    for operation in operations:
        print(operation)

    op = input("Enter opeation: ")

    operation_performed(op)

    def init():
        choice  = input("Another operation (1)\nNew Calculation (2)\n Exit (3): ")

        match choice:
            case "1":
                global another_num 
                c.another_num  = float(input("Enter another number : "))
                op = input("Enter operation: ")
                operation_performed(op, another=True)
            case "2":
                calculate()
            case _:
                print("Exiting....")

    init()

calculate()