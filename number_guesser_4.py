import random

round_num_points = {'Round 1': {'rand_num': random.randint(1, 5), 'possible_score': 15},
                    'Round 2': {'rand_num': random.randint(1, 10), 'possible_score': 35},
                    'Round 3': {'rand_num': random.randint(1, 15), 'possible_score': 50}}

input("Welcome to the Number Guessing game...\n Press 'Enter' to continue...")

hints = ''
while hints not in ['y', 'n']:
    hints = input("Would you like to enable hints [y/n]? ").strip().lower()

round_num = 1
user_score = 0

while round_num <= 3:
    print(f'Round {round_num}')
    guess_count = 1
    while guess_count <= 3:
        user_input = input(f"Guess a number between 1 and {round_num * 5}: ").strip().lower()
        if not user_input.isnumeric() or int(user_input) not in range(1, round_num * 5 + 1):
            continue
        user_guess = int(user_input)
        if user_guess == round_num_points[f'Round {round_num}']['rand_num']:
            user_score += round_num_points[f'Round {round_num}']['possible_score']
            print("That is correct!")
            print(f"You have earned {round_num_points[f'Round {round_num}']['possible_score']}")
            break

        print(f"Sorry, that is not correct.  You have {3 - guess_count} tries left...")

        if hints == 'y' and guess_count < 3:
            if int(user_guess) < round_num_points[f'Round {round_num}']['rand_num']:
                print("Try guessing a higher number.")
            if int(user_guess) > round_num_points[f'Round {round_num}']['rand_num']:
                print("Try guessing a lower number.")

        round_num_points[f'Round {round_num}']['possible_score'] -= 5
        user_input = ''
        guess_count += 1
    if guess_count > 3:
        print(f"The number was {round_num_points[f'Round {round_num}']['rand_num']}")
    print("End of round...")
    round_num += 1

print(f"You have finished the game!\nYour final score is {user_score} out of 100")
