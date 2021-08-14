import pandas

data = pandas.read_csv("weather_data.csv")

temp_list = data["temp"].to_list()
# print(temp_list)

# Task-1 : Get average temperature for the given week

# print(f"Average temp: {round(sum(temp_list)/len(temp_list), 2)}")

# using data series in pandas
# print(data["temp"].mean())

# Tasks-2 : Get the max temp for the week
# print(data["temp"].max())

# We can use .(DOT) notation as well
# Eg:  ->
# print(data.temp.max())

# Task -3 : Get the particular row from the table
print(len(data[data.condition == "Sunny"].day.to_list()))

# Create data from scratch
# data_dict = {
#     "students": ["Amy","Jack","Mike"],
#     "scores": [75,68,95]
# }
# data = pandas.DataFrame(data_dict)
# print(data)

# Converting data to csv file
# data.to_csv("new_file.csv")
