import random
import art as a
import clear as c
import game_data as d

def higher_or_lower():
    game_over = False
    num_data = len(d.data)-1
    i=random.randint(0,num_data)
    if i == 49:
        j = 0
    else:
        j = i+1
    
    score = 0

    while not game_over:
        c.clear()
        print(a.logo)
        print(f"Your current score: {score}")
        print(f"Compare A: {d.data[i]['name']}, a {d.data[i]['description']}, from {d.data[i]['country']} Follower: {d.data[i]['follower_count']} , index: {i}")

        print(a.vs)

        print(f"Against B: {d.data[j]['name']}, a {d.data[j]['description']}, from {d.data[j]['country']} Follower: {d.data[j]['follower_count']} , index: {j}")

        user_answer = input("Who has the more follower, A or B: ").lower()

        if d.data[i]['follower_count'] > d.data[j]['follower_count']:
            answer = 'a'
        else: 
            answer = 'b'

        if user_answer == answer:
            if i == 49:
                i=0
            else:
                i+=1
            
            if j == 49:
                j = 0
            else:
                j+=1

            score +=1
            
        else:
            print(f"Game Over")
            game_over = True
        
    play_again = input("Do you want to play again? (y/n): ").lower()

    if play_again == 'y':
        higher_or_lower()
    else:
        print("Bye")
    
higher_or_lower()