import random
import os
import time
from rps_ascii import rps_ascii_list, game_rules, user_score, computer_score

file_location = r"C:\Users\Michael\Desktop\rps_save.txt"
user_name = ""
win = 0
loss = 0
# user_round_score = 0
# computer_score = 0
choices = ["rock", "paper", "scissors"]


def message_sleep(message):
    print(message)
    time.sleep(1)


def user_intro(win, loss):
    message_sleep(f"Welcome, {user_name} to...")
    message_sleep(rps_ascii_list[0])
    message_sleep(rps_ascii_list[1])
    message_sleep(rps_ascii_list[2] + "\n")
    message_sleep(game_rules)
    data = []
    with open(file_location, "a+") as file:
        lines = file.readlines()
        for line in lines:
            data.append(line)
        for user in data:
            if user_name in user:
                main()
    with open(file_location, "w") as file:
        data.append(f"{user_name}:{0}:{0}\n")
        for i in data:
            file.write(i)
    main()
    return user_name, win, loss


def game_play():
    while True:
        user_choice = input("Choose: Rock, Paper, Scissors - ").strip().lower()
        if user_choice == "q":
            while True:
                final_answer = input("Are you sure?  All progress will not be saved (y/n): ")
                if final_answer.strip().lower() == "y":
                    message_sleep("Thank you for playing!")
                    quit()
                else:
                    break
        if user_choice not in choices:
            continue

        random_number = random.randint(0, 2)
        computer_choice = choices[random_number]
        game_logic(user_choice, computer_choice, win, loss)
    return


def game_logic(user_choice, computer_choice, win, loss):
    if user_choice == "rock" and computer_choice == "scissors":
        message_sleep("The computer chose " + computer_choice + ".")
        user_score += 1
        message_sleep("You won!")
    elif user_choice == "paper" and computer_choice == "rock":
        message_sleep("The computer chose " + computer_choice + ".")
        rps_ascii.user_round_score += 1
        message_sleep("You won!")
    elif user_choice == "scissors" and computer_choice == "paper":
        message_sleep("The computer chose " + computer_choice + ".")
        rps_ascii.user_round_score += 1
        message_sleep("You won!")
    elif user_choice == computer_choice:
        message_sleep("The computer chose " + computer_choice + ".")
        message_sleep("It's a tie!")
    else:
        message_sleep("The computer chose " + computer_choice + ".")
        rps_ascii.computer_score += 1
        message_sleep("You lost!")

    if rps_ascii.user_round_score == 2 or rps_ascii.computer_score == 2:
        message_sleep("Round finished...")
        message_sleep(f"You scored {rps_ascii.user_round_score}.")
        message_sleep(f"the Computer scored {rps_ascii.computer_score}.")
        if rps_ascii.user_round_score > rps_ascii.computer_score:
            win += 1
            message_sleep(f"You won the game!  Congratulations {user_name}!")
            save_game(win, loss)
            while True:
                play_again = input("Would you like to play again (y/n)? ").strip().lower()
                if play_again == "y":
                    main()
                else:
                    message_sleep("Thank you for playing!")
                    quit()
        else:
            loss += 1
            message_sleep("Sorry, you did not win this time.")
            save_game(win, loss)
            while True:
                play_again = input("Would you like to play again (y/n)? ")
                if play_again.strip().lower() == "y":
                    main()
                else:
                    message_sleep("Thank you for playing!")
                    quit()
    return win, loss


def save_game(win, loss):
    while True:
        user_save = input("Would you like to save your progress (y/n)? ").strip().lower()
        if user_save == "y":
            try:
                with open(file_location, "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        if line.find(user_name) == 0:
                            save_file(win, loss)
            except FileNotFoundError:
                print("File not found...")
                break
        break
    return


def save_file(win, loss):
    data = []
    try:
        with open(file_location, "r") as file:
            lines = file.readlines()
            for line in lines:
                data.append(line)
                if line.find(user_name) != -1:
                    word_location = lines.index(line)
            for user in lines:
                if user.startswith(user_name):
                    win += int(user[-4])
                    loss += int(user[-2])
    except FileNotFoundError:
        print("File not found.")
    data.remove(data[word_location])
    updated_user_record = f"{user_name}:{str(win)}:{str(loss)}\n"
    data.insert(word_location, updated_user_record)
    with open(file_location, "w") as file:
        for i in data:
            file.write(i)


def main():
    data = []
    try:
        with open(file_location, "r") as file:
            lines = file.readlines()
            for line in lines:
                data.append(line)
            for user in lines:
                if user.startswith(user_name):
                    print(f"You currently have {user[-4]} wins and {user[-2]} losses against the computer.\n")
    except FileNotFoundError:
        print("File not found.")
    rps_ascii.user_round_score = 0
    rps_ascii.computer_score = 0
    game_play()


while True:
    user_name = input("Please enter a user name (no spaces): ").strip().replace(" ", "_")
    if len(user_name):
        os.system('cls')
        break

user_intro(win, loss)
