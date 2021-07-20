row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

x_axis = int(position[0])
y_axis = int(position[1])

if x_axis > 2 or y_axis > 2:
  print("Not a valid coordinates")
else:
  map[x_axis][y_axis]='❎'
  print(f"{row1}\n{row2}\n{row3}")


