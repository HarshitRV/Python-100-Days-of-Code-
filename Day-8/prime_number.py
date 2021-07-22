def prime_checker(number):
    if number <= 0:
        return print("Not valid input")
    flag = 1
    if number > 1:
        for i in range(2,number):
            if number%i == 0:
                flag = 0
                break
            
    if flag == 0:
        print(f"{number} is not prime")
    else:
        print(f"{number} is prime")   

n = int(input("Check this number: "))
prime_checker(number=n)



