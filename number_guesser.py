# title sequence *
# ask the user to enter their name *
# welcome the user by their name *
# game explanation and rules. *
# rules = three guesses per round, three rounds each a little harder ask if they would like hints
#         first round worth 12 pts with one guess, 10 pts with two guesses, 5 pts with three guesses
#         second round worth 33 pts with one guess, 20, 10
#         final round worth 50 pts with one guess, 30, 10
#         maybe modify the pts with hints enabled or disabled?

import random
import time
import os

hints = "Would you like to enable hints? (y/n) "
title_sequence = "'The Number Guessing Game'"
user_name = "Please enter your name: "
welcome_user = "Welcome {}! Let us introduce you to 'The Number Guessing Game'"
intro = """
This is a very simple number guessing game.
There are three rounds of increasing difficulty
Once asked you will use the keyboard to type the number you think is the correct answer and press 'Enter'
You will have three chances to guess the number correctly.  Every guess reduces the amount of points you can score.
You may enable hints before the round begins.
Have fun!!!
"""
user_score = 0
guess_count_round_one = guess_count_round_two = guess_count_round_three = 3
round_one_possible_score = 15
round_one = "Guess a number between 1 and 5: "
round_one_number = random.randrange(1, 6)
round_two_possible_score = 35
round_two = "Guess a number between 1 and 10: "
round_two_number = random.randrange(1, 11)
round_three_possible_score = 50
round_three = "Guess a number between 1 and 15: "
round_three_number = random.randrange(1, 15)
correct = "Correct!"
incorrect = "That's not correct.\n  You have {} guesses left..."

user_name = input(user_name)
os.system('cls')
time.sleep(1)
print(title_sequence.upper() + "\n")
time.sleep(1)
print(welcome_user.format(user_name))
time.sleep(1)
print(intro)
time.sleep(1)
hints = input(hints)
time.sleep(1)
print()

# ROUND 1 BLOCK

while True and guess_count_round_one != 0:
    round_one_guess = input(round_one)
    if round_one_guess == str(round_one_number):
        print(correct)
        time.sleep(1)
        print("You earned {} points.".format(str(round_one_possible_score)))
        time.sleep(1)
        user_score += round_one_possible_score
        time.sleep(1)
        print("You have {} points.\n".format(str(user_score)))
        time.sleep(1)
        break
    else:
        guess_count_round_one -= 1
        round_one_possible_score -= 5
        print(incorrect.format(guess_count_round_one) + "\n")
        time.sleep(1)
        if hints == "y" and round_one_number > int(round_one_guess) and guess_count_round_one != 0:
            print("Try guessing a higher number\n")
            time.sleep(1)
        elif hints == "y" and round_one_number < int(round_one_guess) and guess_count_round_one != 0:
            print("Try guessing a lower number\n")
            time.sleep(1)
if guess_count_round_one == 0:
    round_one_possible_score = 0
    user_score += round_one_possible_score
    print("No more guesses...")
    time.sleep(1)
    print("You earned {} points.".format(str(round_one_possible_score)))
    time.sleep(1)
    print("You have a total of {} points.".format(str(user_score)))
    time.sleep(1)
    print("Let's try round 2...")
    time.sleep(1)
time.sleep(1)
print()

# ROUND 2 BLOCK

while True and guess_count_round_two != 0:
    round_two_guess = input(round_two)
    if round_two_guess == str(round_two_number):
        print(correct)
        time.sleep(1)
        print("You earned {} points.".format(str(round_two_possible_score)))
        time.sleep(1)
        user_score += round_two_possible_score
        time.sleep(1)
        print("You have {} points.".format(str(user_score)))
        time.sleep(1)
        break
    else:
        guess_count_round_two -= 1
        round_two_possible_score -= 10
        print(incorrect.format(guess_count_round_two) + "\n")
        time.sleep(1)
        if hints == "y" and round_two_number > int(round_two_guess) and guess_count_round_two != 0:
            print("Try guessing a higher number\n")
            time.sleep(1)
        elif hints == "y" and round_two_number < int(round_two_guess) and guess_count_round_two != 0:
            print("Try guessing a lower number\n")
            time.sleep(1)
if guess_count_round_two == 0:
    round_two_possible_score = 0
    user_score += round_two_possible_score
    print("No more guesses...")
    time.sleep(1)
    print("You earned {} points.".format(str(round_two_possible_score)))
    time.sleep(1)
    print("You have a total of {} points.".format(str(user_score)))
    time.sleep(1)
    print("Let's try round 3...")
    time.sleep(1)
time.sleep(1)
print()

# ROUND 3 BLOCK

while True and guess_count_round_three != 0:
    round_three_guess = input(round_three)
    if round_three_guess == str(round_three_number):
        print(correct)
        time.sleep(1)
        print("You earned {} points.".format(str(round_three_possible_score)))
        time.sleep(1)
        user_score += round_three_possible_score
        time.sleep(1)
        print("You have {} points.".format(str(user_score)))
        time.sleep(1)
        break
    else:
        guess_count_round_three -= 1
        round_three_possible_score -= 5
        print(incorrect.format(guess_count_round_three) + "\n")
        time.sleep(1)
        if hints == "y" and round_three_number > int(round_three_guess) and guess_count_round_three != 0:
            print("Try guessing a higher number\n")
            time.sleep(1)
        elif hints == "y" and round_three_number < int(round_three_guess) and guess_count_round_three != 0:
            print("Try guessing a lower number\n")
            time.sleep(1)
if guess_count_round_three == 0:
    round_three_possible_score = 0
    user_score += round_three_possible_score
    print("No more guesses...")
    time.sleep(1)
    print("You earned {} points.".format(str(round_three_possible_score)))
    time.sleep(1)
    print("You have a total of {} points.".format(str(user_score)))
    time.sleep(1)
time.sleep(1)
print()

print("Thank you for playing {}!\nSee you again next time!".format(title_sequence))
time.sleep(1)
while True:
    user_quit = input("Press 'q' to quit the game: ")
    if user_quit == "q":
        time.sleep(2)
        quit()
