import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color = ["Cinnamon", "Gray", "Black"]
count = []

for color in fur_color:
    color_data = data[data["Primary Fur Color"] == color]
    count.append(len(color_data["Primary Fur Color"]))

data_dict = {
    "Fur Color":fur_color,
    "Count": count
}

squirrel_data = pandas.DataFrame(data_dict)
squirrel_data.to_csv("squirrel_count.csv")