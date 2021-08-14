# File system in python

# To read data from a file
with open(file="my_file.txt") as file:
    file.read()

#To write data from a fileR
with open(file="my_file.txt", mode="w") as file:
    file.write("Some text")
    #note the write mode deletes the previous data

#To append data to a file 
with open(file="my_file", mode="a") as file:
    file.write("Some text")