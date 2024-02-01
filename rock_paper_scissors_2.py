import random
import os

directory = "rps_v2.0"
parent_dir = os.path.join(os.path.expanduser('~'), "Desktop", directory)

key_beats_value = {"rock": "scissors",
                   "paper": "rock",
                   "scissors": "paper"}
user_round_score = 0
computer_score = 0
user_wins = 0
user_losses = 0
play_again = None

while True:
    user_name = input("Enter your user name [no spaces]: ").strip().replace(" ", "_")
    if len(user_name) > 0:
        print(f"Welcome {user_name}!  Lets begin...")
        try:
            with open(os.path.join(parent_dir, user_name + ".txt"), 'r') as user_info:
                user_record = user_info.readline()
                user_wins += int(user_record[-3])
                user_losses += int(user_record[-1])
                break
        except FileNotFoundError:
            break

while user_round_score != 2 and computer_score != 2:
    computer_choice = random.choice(list(key_beats_value))
    print(computer_choice)    # Uncomment for computers choice.
    user_input = input("Choose 'rock', 'paper', 'scissors', or 'q' to quit: ").lower().strip()

    if user_input == 'q':
        print("Thank you for playing!")
        quit()

    if user_input in key_beats_value:
        user_choice = user_input
        if user_choice == key_beats_value[computer_choice]:
            print(f"The computer chose {computer_choice.upper()}")
            print("You lost!")
            computer_score += 1
        elif user_choice == computer_choice:
            print("It's a tie...")
        else:
            print(f"The computer chose {computer_choice.upper()}")
            print("You won!!!")
            user_round_score += 1
        print(f"{user_name}: {user_round_score} Computer: {computer_score}")
    else:
        print("Please enter a valid input...")

    while user_round_score == 2 or computer_score == 2:
        if user_round_score == 2:
            user_wins += 1
        elif computer_score == 2:
            user_losses += 1

        try:
            os.makedirs(parent_dir)
        except FileExistsError:
            pass

        try:
            with open(os.path.join(parent_dir, user_name + ".txt"), 'w') as save_file:
                save_file.write(user_name + ":" + str(user_wins) + ":" + str(user_losses))
        except FileNotFoundError:
            print("Could not create file...")

        while True:
            play_again = input("Would you like to play again [y/n]? ").strip().lower()
            if play_again == "n":
                print("Thank you for playing!")
                quit()
            elif play_again == "y":
                user_round_score = computer_score = 0
                break
            else:
                print("Please enter a valid input...")
