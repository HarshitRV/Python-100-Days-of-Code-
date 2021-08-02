# from turtle import *

# timmy = Turtle()

# timmy.shape("turtle")
# timmy.color("red")

# timmy.position()
# timmy.forward(25)
# timmy.position()
# timmy.forward(-75)
# timmy.position

# my_screen = Screen()

# my_screen.exitonclick()

from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["Pokemon Name", "Type"]
x.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Balbasaur", "Grass"],
        ["Squirtle", "Water"]
    ]
)
x.align = 'l'
print(x)
