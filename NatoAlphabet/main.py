import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for(index, row) in data.iterrows()}

name = input()
letter_code = [data_dict.get(letter.upper()) for letter in name]
print(letter_code)
