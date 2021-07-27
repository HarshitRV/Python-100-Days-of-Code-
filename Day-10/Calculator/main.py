from art import logo

print(logo)

def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


operations = {
    "+" : sum,
    "-" : sub,
    "*" : mul,
    "/" : div
}

def calculator():
    num1 = float(input("Enter first num : "))

    for operation in operations:
        print(f"{operation}")

    operation = input("Enter the symbol : ")

    num2 = float(input("Enter second num : "))

    function = operations[operation]

    answer_1 = function(num1, num2)

    print(f"{num1} {operation} {num2} = {answer_1}")


    another_operation = input("Do you want to perform another operation? (y/n) : ")

    answer = answer_1

    while another_operation == "y":
        operation = input("Enter the symbol : ")
        num3 = float(input("Enter another number: "))

        function = operations[operation]

        pre_answer = answer

        answer = function(answer, num3)


        print(f"{pre_answer} {operation} {num3} = {answer}")

        another_operation = input(f"Type 'y' to continue calculation on {answer}  or 'n' for new calculation : ")

    if another_operation != 'y':
        calculator()
        
    
calculator()

