import random
import art as a 
import clear as c

def guess_the_number():
    print(f"{a.logo}\n")
    print("Thinking of a number between 1 and 100\n")

    random_number = random.randint(1,100)

    difficulty = input("Choose your difficulty level.\n\nEasy(e)\nMedium(m)\nHard(h)\n").lower()

    if difficulty == 'e':
        gusseses = 15
    elif difficulty =='m':
        gusseses = 10
    elif difficulty == 'h':
        gusseses = 5
    else:
        print("Invalid Choice")
        print("Setting difficulty to easy")
        gusseses = 15

    game_over = False

    print(f"You have {gusseses} guessess.")


    while not game_over and gusseses != 0:
        user_guess = int(input("Guess the number : "))

        if user_guess == random_number:
            print(f"\nGuessed it right\n{a.win}")
            game_over = True

            play_again = input("Play Again? (y/n) : ")

            if play_again == 'y':
                c.clear()
                guess_the_number()
            else:
                return print("Bye! 🙂")
            
        elif user_guess > random_number:
            print("\nToo High 🔺")  
            gusseses -=1
            print(f"\nGuesses left : {gusseses}")
        else:
            print("\nToo Low 🔽")  
            gusseses -=1
            print(f"\nGuesses left : {gusseses}")

    if gusseses == 0:
        print(f"Game Over 😞\n {a.lost}")  
    
    play_again = input("Play Again? (y/n) : ").lower()

    if play_again == 'y':
        c.clear()
        guess_the_number()
    else:
        return print("Bye! 🙂")   

guess_the_number() 


