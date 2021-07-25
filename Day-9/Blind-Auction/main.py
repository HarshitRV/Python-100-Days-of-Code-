import art as a
import clear as c

print(f"{a.auction}\n {a.start}")

aution_data = {}
more_bidders = 'y'
highest_bid = 0
highest_bid_by = ""

while more_bidders == 'y':
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))

    aution_data[name] = bid

    c.clear()

    more_bidders = input("Is there more people to bid? (y/n) : ").lower()

    c.clear()

for data in aution_data:
    if highest_bid < aution_data[data]:
        highest_bid = aution_data[data]
        highest_bid_by = data

print(f"The highest bid is {highest_bid} by {highest_bid_by}")
print(a.end)

print(f"\nHere are all the bids\n {aution_data}")