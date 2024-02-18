import random
import os
from hangman_helper import word_lib, draw_hangman


def get_word():
    game_category = random.choice(list(word_lib.keys()))
    game_word = random.choice(word_lib[game_category])
    print(f"The category for this game will be {game_category.upper()}")
    # print(game_word.upper())
    return game_word.upper(), game_category


def play_game(word, category):
    blank_word = ""
    for char in word:
        if ord(char) in range(65, 91):
            blank_word += "_"
        else:
            blank_word += " "

    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 6

    print("Let's play Hangman!")
    print(draw_hangman(attempts))
    print(blank_word)

    while not guessed and attempts > 0:
        guess = input("Guess a letter or a word: ").upper().strip()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                os.system('cls')
                print(f"Sorry, you have already guessed the letter, {guess}")
            elif guess not in word:
                os.system('cls')
                print(f"Sorry, the letter, {guess}, is not in the word...")
                guessed_letters.append(word)
                attempts -= 1
            else:
                os.system('cls')
                print(f"{guess} is correct!")
                guessed_letters.append(guess)
                word_as_list = list(blank_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                blank_word = "".join(word_as_list)
                if "_" not in blank_word:
                    guessed = True
        elif len(guess) == len(word):
            if guess in guessed_words:
                os.system('cls')
                print(f"Sorry, you have already guessed the word, {word}")
            elif guess != word:
                os.system('cls')
                print(f"Sorry, {word} is not in the word...")
                attempts -= 1
                guessed_letters.append(word)
            else:
                guessed = True
                blank_word = word
        else:
            os.system('cls')
            print(f"{guess} is not a valid entry...")

        print(f"The category is: {category.upper()}")
        print(draw_hangman(attempts))
        print(blank_word)
        print("\n")
    if guessed:
        print("Congratulations!!!  You have won the game!")
    else:
        print("Sorry you have run out of tries...  Game Over.")
        print(f"The word was {word}")


def main():
    word, category = get_word()
    play_game(word, category)
    play_again = ''
    while play_again not in ['Y', 'N']:
        play_again = input("Would you like to play again [Y/N]? ").upper().strip()
        if play_again == 'Y':
            os.system('cls')
            word, category = get_word()
            play_game(word, category)
            play_again = ''
        print("Thank you for playing Hangman!\nSee you again soon...")


if __name__ == "__main__":
    main()
