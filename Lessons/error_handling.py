# FileNotFound
# with open('a_file.txt') as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruits = ["Apple", "Banana", "Pineapple"]
# value = fruits[3]

# TypeError
# text = "abc"
# print(text + 5)


"""
Error handling
    try: Something that might cause an exception
    except: Do this if there was an exception
    else: Do this if there was no exception
    finally: Do this no matter what happens
"""

dictionary = {"key": "value"}
try:
    file = open("a.txt")
    print(dictionary['non_existent_key'])
except FileNotFoundError:
    file = open("a.txt", "w")
    file.write("Created new file")
except KeyError as error_message:
    print(f"the key {error_message} doesn't exist")
else:
    print("the file was opened and the dictionary key was found")
    print(file.read())
finally:
    file.close()
    print("done")

# Raising new error
height = float(input("Height: (m)"))
weight = int(input("Weight: (kg)"))
bmi = weight / height ** 2
if height > 3:
    raise ValueError("Please check the typed height! It shouldn't be more than 3m")
print(f"BMI: {bmi}")
