import csv
import pandas

# temperatures = []
#
# with open("weather_data.csv") as data_file  :
#     data = csv.reader(data_file)
#     for row in data:
#         if row != "temp":
#             temperatures.append(row[1])
#
# print(temperatures)

data = pandas.read_csv("squirrel_data.csv")
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ['Gray', 'Red', 'Black'],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}
print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_color.csv")