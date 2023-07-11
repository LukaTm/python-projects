import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

# print(data_dict)
prim_color = data["Primary Fur Color"]
# gray = sum(prim_color['Gray'])
# print(gray)
gray = len([data["Primary Fur Color"] == "Gray"])
black = len([data["Primary Fur Color"] == "Black"])
cinnamon = len([data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, black, cinnamon]
}
df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')

# data.to_csv('squirrel_count.csv')


# temp_list = data['temp'].to_list()
#
# #Get Data in Columns
# #print(sum(temp_list)/len(temp_list)) #average
# #print(data['temp'].mean()) #average
# #print(data['temp'].max())
# #print(data.condition) # var vnk sita
#
# #Get data in row
# #print(data.day()) # tikai monday row ja ja
#
# #print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.temp)
#
#
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv') #
