import random

old_list = [1, 2, 3]
new_list = [item + 1 for item in old_list]  # [2, 3, 4]

name_list = [letter for letter in "Eljesa"]  # ['E', 'l', 'j', 'e', 's', 'a']

number_list = [2 * n for n in range(1, 5)]  # [2, 4, 6, 8]

names = ["Alex", "Beth", "Dave", "Eleanor", "Caroline", "Freddie"]
short_names = [name for name in names if len(name) <= 4]  # ['Alex', 'Beth', 'Dave']
uppercase_long_names = [name.upper() for name in names if len(name) >= 5]  # ['ELEANOR', 'CAROLINE', 'FREDDIE']

students = {student: random.randint(1, 100) for student in names}
passed_students = {student: points for (student, points) in students.items() if points >= 60}

