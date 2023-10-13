import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    name = input("Your name: ").upper()
    try:
        letter_code = [data_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters of alphabet please!")
        generate_phonetic()
    else:
        print(letter_code)


generate_phonetic()
