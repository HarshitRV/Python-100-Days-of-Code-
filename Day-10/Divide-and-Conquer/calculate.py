from calc import Calculator

c = Calculator()

class Calculate:
    def __init__(self):
        self.evaluate()
        pass

    def evaluate(self):

        a = float(input("Enter first num: "))

        print("\n---Select Operations---")
        for operation in c.operations:
            print(operation)

        self.operation = input("\nEnter Operation: ")

        if self.operation in ['log', 'sqrt', 'exp', 'summation']:
            self.single_input(meess)
        else:
            self.second_input()

        def second_input(message, another=False):

            function = op.operations[c.operation]  

            if another:
                prev_num = c.result
                
                if c.operation == 'summation':
                    b = int(input("Enter end limit"))
                    result = function(prev_num, b)
                    print(f"\n{message} =  {result}\n")

                elif c.operation == 'pow':
                    b = int(input("Raised to power of : "))
                    result = function(prev_num, b)
                    print(f"{prev_num} raised to power of {b} = {result}")

                else:
                    result = function(prev_num, c.another_num)
                    print(f"\n{message} of {prev_num} {c.operation} {c.another_num} =  {result}\n")
                calc_again()

            else:
                if c.operation == 'summation':
                    b = float(input("\nEnter end limit: "))
                    result = function(a, b)
                    print(f"\n{message} from {a} to {b} =  {result}\n")

                elif c.operation == 'pow':
                    b = int(input("Raised to power of : "))
                    result = function(a, b)
                    print(f"{a} raised to power of {b} = {result}")

                else:
                    b = float(input("\nEnter second num: "))
                    result = function(a, b) 
                    print(f"\n{message} of {a} {c.operation} {b} = {result}\n")

        def single_input(message, another=False):

            function = operations[c.operation]

            if another:
                prev_num = c.result
                result = function(c.result)
                print(f"{message} of {prev_num} = {result}\n")
                calc_again()
                
            else:
                result = function(a)
                print(f"{message} of {a} = {result}\n")

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
                case "pow":
                    second_input("Power", another)
                case "sqrt":
                    single_input("Square Root", another)
                case "exp":
                    single_input("Exponent", another)
                case "summation":
                    second_input("Summation", another)
                case _:
                    print("Invalid operation. Restarting Calculator...\n")
                    calculate()

        operation_performed(c.operation)

       
        def calc_again():

            print("---Enter your choice---")
            choice  = input("1: Another operation\n2: New Calculation\n3: Exit: ")
            print("\n")

            match choice:
                case "1":
                    c.operation = input("Enter operation: ")

                    if c.operation in ['log', 'pow', 'sqrt', 'exp', 'summation']:
                        operation_performed(c.operation, another=True)
                    else:
                        c.another_num  = float(input("Enter another number : "))
                        operation_performed(c.operation, another=True)
                case "2":
                    calculate()
                case _:
                    print("Exiting....")

        calc_again()