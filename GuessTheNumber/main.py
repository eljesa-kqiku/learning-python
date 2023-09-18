import random

print("Welcome to Guess the Number Game!")
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty: 'easy' or 'hard': ")

number = random.randrange(1, 100)
tries_left = 5 if difficulty == 'hard' else 10

game_over = False
while not game_over:
    print(f"\nYou have {tries_left} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess == number:
        print("\nYou are correct!")
        game_over = True
        break
    elif guess < number:
        print("Too low.")
    else:
        print("Too high.")
    tries_left -= 1
    if tries_left == 0:
        game_over = True
        print(f"\nNo more attempts left. The number was: {number}")
    print("Guess again.")