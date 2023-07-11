# with open('226 weather-data.csv') as file:
# data = file.readlines()
# print(data)

import csv

# with open('226 weather-data.csv') as date_file:
#     data = csv.reader(date_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)

import pandas

data = pandas.read_csv('226 weather-data.csv')

data_dict = data.to_dict()
# print(data_dict)

temp_list = data['temp'].to_list()

# Get Data in Columns
# print(sum(temp_list)/len(temp_list)) #average
# print(data['temp'].mean()) #average
# print(data['temp'].max())
# print(data.condition) # var vnk sita

# Get data in row
# print(data.day()) # tikai monday row ja ja

# print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
print(monday.temp)

data = pandas.DataFrame(data_dict)
data.to_csv('new_data.csv')  #
