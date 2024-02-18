import random
import time
import os

title_sequence = "The Number Guessing Game"
intro = """
This is a very simple game.
There are three rounds of increasing difficulty.
Use the keyboard to enter the number you think is the correct answer and press 'Enter'.
You will have three chances to guess the number correctly.
Every guess reduces the amount of points you can score.
You may enable hints before the round begins.
Have fun!!!
"""
hints_prompt = "Would you like to enable hints? (y/n) "
hint_higher = "Try guessing a higher number\n"
hint_lower = "Try guessing a lower number\n"
earned_points = "You have earned {} points this round.\n"
round_intro = "Round #{}\n"
correct = "Correct!\nGreat job!\n"
incorrect = "That's not correct.\n  You have {} guesses left...\n"
lets_try = "Let's try Round #{}\n"
thank_you = "\nThank you for playing {}!\nSee you again next time!"
user_score = 0
round_number = 1
guess_count = {1: 3, 2: 3, 3: 3}
possible_score = {1: 15, 2: 35, 3: 50}
transition_dict = {"no_points": "You earned 0 points.",
                   "total_points": "You have a total of {} points.\n"}
guess_number_str = {1: "Guess a number between 1 and 5: ",
                    2: "Guess a number between 1 and 10: ",
                    3: "Guess a number between 1 and 15: "}
number_generator = {1: random.randrange(1, 6),
                    2: random.randrange(1, 11),
                    3: random.randrange(1, 15)}


def message_sleep(message):
    print(message)
    time.sleep(1)


def round_transition():
    message_sleep(transition_dict["no_points"])
    message_sleep(transition_dict["total_points"].format(str(user_score)))


def end_game_sequence():
    message_sleep(thank_you.format(title_sequence))
    while True:
        user_quit = input("Press 'q' to quit the game: ")
        if user_quit == "q":
            time.sleep(2)
            quit()


while True:
    user_name = input("Please enter your name: ")
    if len(user_name): break
os.system('cls')
time.sleep(1)
message_sleep(f"{title_sequence.upper()}\n")
message_sleep(f"Welcome {user_name.title()}! Let us introduce you to '{title_sequence}'")
message_sleep(intro)

while True:
    hints = input(hints_prompt)
    if hints == "y" or hints == "n":
        print()
        break

# ROUND 1 BLOCK

message_sleep(round_intro.format(round_number))

while guess_count[1] != 0:
    print(number_generator[1])
    while True:
        user_guess = input(guess_number_str[1])
        if user_guess.isnumeric(): break
    if user_guess == str(number_generator[1]):
        message_sleep(correct)
        message_sleep(earned_points.format(str(possible_score[1])))
        user_score += possible_score[1]
        message_sleep(transition_dict["total_points"].format(str(user_score)))
        round_number += 1
        break
    else:
        guess_count[1] -= 1
        possible_score[1] -= 5
        message_sleep(incorrect.format(guess_count[1]))
        if hints.lower() == "y" and number_generator[1] > int(user_guess) and guess_count[1] != 0:
            message_sleep(hint_higher)
        elif hints.lower() == "y" and number_generator[1] < int(user_guess) and guess_count[1] != 0:
            message_sleep(hint_lower)
else:
    round_number += 1
    round_transition()
    message_sleep(lets_try.format(round_number))

message_sleep(round_intro.format(round_number))

# ROUND 2 BLOCK

while guess_count[2] != 0:
    print(number_generator[2])
    while True:
        user_guess = input(guess_number_str[2])
        if user_guess.isnumeric(): break
    if user_guess == str(number_generator[2]):
        message_sleep(correct)
        message_sleep(earned_points.format(str(possible_score[2])))
        user_score += possible_score[2]
        message_sleep(transition_dict["total_points"].format(str(user_score)))
        round_number += 1
        break
    else:
        guess_count[2] -= 1
        possible_score[2] -= 5
        message_sleep(incorrect.format(guess_count[2]))
        if hints.lower() == "y" and number_generator[2] > int(user_guess) and guess_count[2] != 0:
            message_sleep(hint_higher)
        elif hints.lower() == "y" and number_generator[2] < int(user_guess) and guess_count[2] != 0:
            message_sleep(hint_lower)
if guess_count[2] == 0:
    round_number += 1
    round_transition()
    message_sleep(lets_try.format(round_number))

message_sleep(round_intro.format(round_number))

# ROUND 3 BLOCK

while guess_count[3] != 0:
    print(number_generator[3])
    while True:
        user_guess = input(guess_number_str[3])
        if user_guess.isnumeric(): break
    if user_guess == str(number_generator[3]):
        message_sleep(correct)
        message_sleep(earned_points.format(str(possible_score[3])))
        user_score += possible_score[3]
        message_sleep(transition_dict["total_points"].format(str(user_score)))
        break
    else:
        guess_count[3] -= 1
        possible_score[3] -= 5
        message_sleep(incorrect.format(guess_count[3]))
        if hints.lower() == "y" and number_generator[3] > int(user_guess) and guess_count[3] != 0:
            message_sleep(hint_higher)
        elif hints.lower() == "y" and number_generator[3] < int(user_guess) and guess_count[3] != 0:
            message_sleep(hint_lower)
if guess_count[3] == 0:
    round_transition()

end_game_sequence()
