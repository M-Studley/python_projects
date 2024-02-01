import random
import time
import os

title = "The Number Guessing Game"
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
message = {
    "hint": "Try guessing a {} number",
    "earned_points": "You have earned {} points this round.",
    "round_intro": "Round #{}",
    "correct": "Correct!\nGreat job!\n",
    "incorrect": "That's not correct.\nYou have {} guesses left...\n",
    "lets_try": "Let's try Round #{}",
    "thank_you": "\nThank you for playing {}!\nSee you again next time!"
}
user_score = 0
round_number = 1
guess_count = {1: 3, 2: 3, 3: 3}
possible_score = {1: 15, 2: 35, 3: 50}
transition_dict = {"no_points": "You earned 0 points.",
                   "total_points": "You have a total of {} points."}
guess_number_msg = {1: "Guess a number between 1 and 5: ",
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
    message_sleep(transition_dict["total_points"].format(str(user_score)) + "\n")


def end_game_sequence():
    message_sleep(message["thank_you"].format(title))
    while True:
        user_quit = input("Press 'q' to quit the game: ").strip().lower()
        if user_quit == "q":
            time.sleep(2)
            quit()


# Intro sequence
user_name = None
while not user_name:
    user_name = input("Please enter your name: ")
os.system('cls')
time.sleep(1)
message_sleep(f"{title.upper()}\n")
message_sleep(f"Welcome {user_name.title()}! Let us introduce you to '{title}'")
message_sleep(intro)

hints = ""
while not hints in ["y", "n"]:
    hints = input(hints_prompt)
    if hints == "y" or hints == "n":
        print()

# ROUND 1 BLOCK

message_sleep(message["round_intro"].format(round_number) + "\n")

while guess_count[1]:
    print(number_generator[1])
    while True:
        user_guess = input(guess_number_msg[1])
        if user_guess.isnumeric(): break
    if user_guess == str(number_generator[1]):
        message_sleep(message["correct"])
        message_sleep(message["earned_points"].format(str(possible_score[1])) + "\n")
        user_score += possible_score[1]
        message_sleep(transition_dict["total_points"].format(str(user_score)) + "\n")
        round_number += 1
        break
    else:
        guess_count[1] -= 1
        possible_score[1] -= 5
        message_sleep(message["incorrect"].format(guess_count[1]))
        if hints.lower() == 'y' and guess_count[1]:
            if number_generator[1] > int(user_guess):
                message_sleep(message["hint"].format("higher") + "\n")
            else:
                message_sleep(message["hint"].format("lower") + "\n")
else:
    round_number += 1
    round_transition()
    message_sleep(message["lets_try"].format(round_number) + "\n")

message_sleep(message["round_intro"].format(round_number) + "\n")

# ROUND 2 BLOCK

while guess_count[2] != 0:
    print(number_generator[2])
    while True:
        user_guess = input(guess_number_msg[2])
        if user_guess.isnumeric(): break
    if user_guess == str(number_generator[2]):
        message_sleep(message["correct"])
        message_sleep(message["earned_points"].format(str(possible_score[2])) + "\n")
        user_score += possible_score[2]
        message_sleep(transition_dict["total_points"].format(str(user_score)) + "\n")
        round_number += 1
        break
    else:
        guess_count[2] -= 1
        possible_score[2] -= 5
        message_sleep(message["incorrect"].format(guess_count[2]))
        if hints.lower() == 'y' and guess_count[1]:
            if number_generator[1] > int(user_guess):
                message_sleep(message["hint"].format("higher") + "\n")
            else:
                message_sleep(message["hint"].format("lower") + "\n")
if guess_count[2] == 0:
    round_number += 1
    round_transition()
    message_sleep(message["lets_try"].format(round_number) + "\n")

message_sleep(message["round_intro"].format(round_number) + "\n")

# ROUND 3 BLOCK

while guess_count[3] != 0:
    print(number_generator[3])
    while True:
        user_guess = input(guess_number_msg[3])
        if user_guess.isnumeric(): break
    if user_guess == str(number_generator[3]):
        message_sleep(message["correct"])
        message_sleep(message["earned_points"].format(str(possible_score[3])) + "\n")
        user_score += possible_score[3]
        message_sleep(transition_dict["total_points"].format(str(user_score)) + "\n")
        break
    else:
        guess_count[3] -= 1
        possible_score[3] -= 5
        message_sleep(message["incorrect"].format(guess_count[3]))
        if hints.lower() == "y" and number_generator[3] > int(user_guess) and guess_count[3] != 0:
            message_sleep(message["hint"].format("higher") + "\n")
        elif hints.lower() == "y" and number_generator[3] < int(user_guess) and guess_count[3] != 0:
            message_sleep(message["hint"].format("lower") + "\n")
if guess_count[3] == 0:
    round_transition()

end_game_sequence()
