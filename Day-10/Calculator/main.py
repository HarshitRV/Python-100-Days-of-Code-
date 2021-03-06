from calc import Calculator
from art import logo
from greet import Greet

try:
    
    print(logo)

    # Object of Greet class
    g = Greet(input("What's your good name: "))

    # Object of calculator class
    c = Calculator()

    # Operations dictionary
    operations = {
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

    def calculate():

        # 1. Taking the first num from user.
        a = float(input("Enter first num: "))

        # 2. Displaying the list of operations that can be performed.
        print("\n---Select Operations---")
        for operation in operations:
            print(operation)

        # 3. Asking for the choice of operation and storing it into
        #    operation variable of the object c of the Calculator class.
        c.operation = input("\nEnter Operation: ")

        def second_input(message, another=False):
            """
            This function is called if the operation chosen is +, -, / , * , pow or summation.
            """

            # From the operation dictionary using the operation chosen by user as 
            # key the function is called and assigned to the function variable.
            function = operations[c.operation]  

            # If another is passed as true means an operations has already been performed
            # and now using the result of previous operation new opeation is performed.
            if another:

                # Storing the result of previous operation in prev_num variable.
                prev_num = c.result
                
                # If new operation is summation we ask for end limit and 
                # display message result.
                if c.operation == 'summation':
                    b = int(input("Enter end limit"))
                    result = function(prev_num, b)
                    print(f"\n{message} =  {result}\n")

                # If operation is pow we ask for raised to power of 
                # and display the message result.
                elif c.operation == 'pow':
                    b = int(input("Raised to power of : "))
                    result = function(prev_num, b)
                    print(f"{prev_num} raised to power of {b} = {result}")

                # If it's not summation or pow then we display the regular message
                # with result.
                else:
                    result = function(prev_num, c.another_num)
                    print(f"\n{message} of {prev_num} {c.operation} {c.another_num} =  {result}\n")
                
                # Calling calc_again to ask for user choices wether or not continue 
                # calculations.
                calc_again()
            
            # If the calculations are performed for the very first time then else block is 
            # executed.
            else:
                # If operation is summation we ask for end limit and 
                # display message result.
                if c.operation == 'summation':
                    b = float(input("\nEnter end limit: "))
                    result = function(a, b)
                    print(f"\n{message} from {a} to {b} =  {result}\n")

                # If operation is pow we ask for raised to power of 
                # and display the message result.
                elif c.operation == 'pow':
                    b = int(input("Raised to power of : "))
                    result = function(a, b)
                    print(f"{a} raised to power of {b} = {result}")
                
                # If it's not summation or pow then we display the regular message
                # with result.
                else:
                    b = float(input("\nEnter second num: "))
                    result = function(a, b) 
                    print(f"\n{message} of {a} {c.operation} {b} = {result}\n")

        def single_input(message, another=False):
            """
            This function is called if the chosen operation is log, sqrt, exp.
            """

            # From the operation dictionary using the operation chosen by user as 
            # key the function is called and assigned to the function variable.
            function = operations[c.operation]

            # If another is passed as true means an operations has already been performed
            # and now using the result of previous operation new opeation is performed.
            if another:
                prev_num = c.result
                result = function(c.result)
                print(f"{message} of {prev_num} = {result}\n")
                calc_again()

            # If the calculations are performed for the very first time then else block is 
            # executed. 
            else:
                result = function(a)
                print(f"{message} of {a} = {result}\n")

                
        def operation_performed(op, another=False):
            """
            This function calls the single_input or the second_input depending 
            upon the operation passed in. By default another is set to false as 
            initially we are doing the operation for first time.
            """

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

        # 4. Calling the operation performed function and passing in the operation chosen
        #    by the user.
        operation_performed(c.operation)

       
        def calc_again():
            """
            This function is called to ask user to perform another operation on
            previous result , perform a fresh calculation or exit.
            """
            print("---Enter your choice---")
            choice  = input("1: Another operation\n2: New Calculation\n3: Exit: ")
            print("\n")

            match choice:
                case "1":
                    c.operation = input("Enter operation: ")

                    # Calling the operations performed without asking for another 
                    # number if operations are log, pow, sqrt, exp, factorial or summation
                    # and setting another as True
                    if c.operation in ['log', 'pow', 'sqrt', 'exp', 'summation', '!']:
                        operation_performed(c.operation, another=True)

                    # Asking another number from user if operation performed are
                    # +, -, *, / and setting another as True
                    else:
                        c.another_num  = float(input("Enter another number : "))
                        operation_performed(c.operation, another=True)
                case "2":
                    calculate()
                case _:
                    print("Exiting....")

        calc_again()

    calculate()

except KeyboardInterrupt:
    print("\nExiting....")