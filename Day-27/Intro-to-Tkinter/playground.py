# # Unlimited Positional Arguments *args
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum

# print(add(5,6,7))

# # Keyword Arguments **kwargs
# def calculate(one_positional_arg, **kwargs):
#     one_positional_arg += kwargs["add"]
#     one_positional_arg *= kwargs["multiply"]

#     return one_positional_arg

# print(calculate(5, add=5, multiply=6))

import time
from itertools import chain

for char in cycle("|/-\\"):
    print(char, end="\r", flush=True)
    sleep(0.08)
