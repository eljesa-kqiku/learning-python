#Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

invited_names = []
with open('./Input/Names/invited_names.txt') as file:
    data = file.readlines()
    for name in data:
        invited_names.append(name.strip())

with open('./Input/Letters/starting_letter.txt') as letter:
    template = letter.read()

    for name in invited_names:
        new_letter = template.replace('[name]', name)

        with open(f'./Output/ReadyToSend/letter_for_{name}', mode='w') as created_letter:
            created_letter.write(new_letter)

