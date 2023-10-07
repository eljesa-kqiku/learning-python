# CSV Library
import csv

with open('weather_data.csv') as file:
    data = csv.DictReader(file)
    temperatures = []
    for row in data:
        temp = int(row['temp'])
        temperatures.append(temp)

    print(temperatures)

# Pandas Library
import pandas

data = pandas.read_csv('weather_data.csv')  # A DataFrame object
# print(data)
print(data['temp'])  # A Series object
print()

# Find average with traditional method
temp_data = data['temp'].to_list()
avg_temp = sum(temp_data) / len(temp_data)
print(f"Average temp: {avg_temp}\n")

# Find average with Pandas
avg_temp = data['temp'].mean()
print(f"Average temp: {avg_temp}\n")


# we can also use . notation
print(f"Max temp: {data.temp.max()}\n")

# query
max_temp_row = data[data.temp == data.temp.max()]
print(f"The record with highest temperature:\n{max_temp_row}\n")

monday = data[data.day == 'Monday']
print(monday.condition)

# Create a dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)

# Saving this data to a file (generates the file)
data.to_csv("new_files.csv")

# Iterating through rows in a DataFrame
students_dict = {
    "student": ["Angela", "James", "Lily"],
    "scores": [56, 76, 58]
}
student_data_frame = pandas.DataFrame(students_dict)
for(index, row) in student_data_frame.iterrows():
    print(row.student)