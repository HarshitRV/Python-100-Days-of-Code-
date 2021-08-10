numbers = [1,2,3,4,5,6,7,8,9,10]

# slicing out 5,6,7
sliced_numbers  = numbers[4:7]
print(sliced_numbers)

# slicing every number from 3 till end
three_till_end = numbers[2:]
print(three_till_end)

# slicing every number from 1 till 7
one_till_seven = numbers[:7]
print(one_till_seven)

# slicing out 3 to 7 but leaving every second number in the sliced out list
three_to_seven = numbers[2:7:2]
print(three_to_seven) # [3, 5, 7] it skipped 4 and 6 

# get all odd number in the list
even = numbers[::1] #it basically skips every 2nd number in the list
print(even)

# reverse the list
reversed_list = numbers[::-1]
# print(reversed_list)