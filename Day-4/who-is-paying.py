import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
print(f"Bill will be paid by {random.choice(names)}")


