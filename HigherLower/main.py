import art
import os
import game_data
import random


def full_item(item):
    return f"{item['name']}, {item['description']} from {item['country']}"


def rewrite_output(item1, item2):
    print(f"Compare A: " + full_item(item1))
    print(art.vs)
    print("Against B: " + full_item(item2))


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art.logo)


def validate_answer(item1, item2, ans):
    correct_ans = 'a' if item1['follower_count'] > item2['follower_count'] else 'b'
    return correct_ans == ans.lower()


def generate_random(old_item):
    new_item = game_data.data[random.randint(0, 50)]
    if old_item is not None and old_item['name'] == new_item['name']:
        return generate_random(old_item)
    return new_item


def start_game():
    clear_console()
    game_over = False
    points = 0
    last_compared_item = None
    while not game_over:
        if last_compared_item is None:
            last_compared_item = generate_random(None)
        new_item = generate_random(last_compared_item)
        rewrite_output(last_compared_item, new_item)
        ans = input("Who has more followers? Type 'a' or 'b' ")
        if validate_answer(last_compared_item, new_item, ans):
            clear_console()
            points += 1
            print(f"You're right! Your current score: {points}")
            last_compared_item = new_item
        else:
            clear_console()
            print(f"Sorry that's wrong! Final score: {points}")
            game_over = True


start_game()
