import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []
life = 5

print(f'Pssst, the solution is {chosen_word}.')

for i in range(len(chosen_word)):
  display.append("_")


print(display)
print(life)

guess = input("Guess a letter: ").lower()

for j in range(len(chosen_word)):
    if chosen_word[j] == guess:
        display[j] = guess

print(display)
while display.count("_") != 0 and life !=0:
  guess = input("Guess a letter: ").lower()

  for j in range(len(chosen_word)):
      if chosen_word[j] == guess:
          display[j] = guess

  print(display)
  print(life)


if display.count("_") == 0 :
  print("You win")
else:
  print("You loose")
