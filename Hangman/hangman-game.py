import random
import hangman_words
import hangman_art

chosen_word = hangman_words.word_list[random.randrange(0, len(hangman_words.word_list))]
letters_left = len(chosen_word)
guessed_word = ['_'] * letters_left
lives = 6
guessed_letters = []
print(hangman_art.logo)

while letters_left > 0 and lives > 0:
    print(hangman_art.stages[lives - 1])
    print("".join(guessed_word))
    guess = input("Type a letter: ").lower()
    letters_left_start = letters_left

    if guess in guessed_letters:
        print("You have already guessed letter " + guess)
        continue
    guessed_letters.append(guess)

    for index, char in enumerate(chosen_word):
        if char == guess:
            guessed_word[index] = char
            letters_left -= 1

    if letters_left == letters_left_start:
        lives -= 1
        print(f"The letter {guess} is not in the word.")


if letters_left == 0:
    print("\nYou have won! The word was: " + chosen_word)
elif lives == 0:
    print("\nYou lost! The word was: " + chosen_word)

