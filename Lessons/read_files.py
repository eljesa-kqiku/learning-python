file = open("my_filte.txt")
content = file.read()
print(content)
file.close()

# Write mode, it will replace the file content on write()
# if the file doesn't exist, it will create the file
with open("my_filte.txt", mode='w') as file:
    file.write("new text")

# Append mode, appends the text at the end of the file on write()
with open("my_filte.txt", mode='a') as file:
    file.write("\nAdded a new text")

# Read mode, also default
with open("my_filte.txt", mode='r') as file:
    content = file.read()
    print(content)
