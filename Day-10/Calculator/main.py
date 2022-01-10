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
        function = operations[c.operation]
        if another:
            prev_num = c.result
            result = function(prev_num, c.another_num)
            print(f"\n{message} of {prev_num} {c.operation} {c.another_num} =  {result}\n")
            init()
        else:
            b = float(input("\nEnter second num: "))
            result = function(a, b)
            print(f"\n{message} of {a} {c.operation} {b} = {result}\n")

    def single_input(message, another=False):
        function = operations[c.operation]
        if another:
            result = function(c.result)
            print(f"{message} of {c.result} = {result}")
        else:
            result = function(a)
            print(f"{message} of {a} = {result}")

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
                print("Invalid Choice\n")
                print("Recalculate...")

    a = float(input("Enter first num: "))

    print("\n---Operations---")
    for operation in operations:
        print(operation)

    c.operation = input("\nEnter operation: ")

    operation_performed(c.operation)

    def init():
        print("---Enter your choice---")
        choice  = input("1: Another operation\n2: New Calculation (2)\n2: Exit: ")
        print("\n")

        match choice:
            case "1":
                global another_num 
                c.another_num  = float(input("Enter another number : "))
                c.operation = input("Enter operation: ")
                operation_performed(c.operation, another=True)
            case "2":
                calculate()
            case _:
                print("Exiting....")

    init()

calculate()