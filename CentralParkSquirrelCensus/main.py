import pandas

filepath = '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'
data = pandas.read_csv(filepath)

black_count = len(data[data['Primary Fur Color'] == 'Black'])
gray_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])

fur_count = {
    "Fur Color": ["Black", "Gray", "Cinnamon"],
    "Count": [black_count, gray_count, cinnamon_count]
}

fur_count = pandas.DataFrame(fur_count)
fur_count.to_csv("fur_count_data.csv")
print(fur_count)
