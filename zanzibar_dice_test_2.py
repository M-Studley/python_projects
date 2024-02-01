import random

roll_total = 0
# Three dice combo points.
dice_set_points = {1000: [4, 5, 6],
                   900:  [1, 1, 1],
                   800:  [2, 2, 2],
                   700:  [3, 3, 3],
                   600:  [4, 4, 4],
                   500:  [5, 5, 5],
                   400:  [6, 6, 6],
                   300:  [1, 2, 3]}
# Point totals for individual dice.
single_die_points = {1: 100,
                     6: 60,
                     2: 2,
                     3: 3,
                     4: 4,
                     5: 5}


# Asks how many players [2-4] and validates if it is a number.
# Then will generate a dictionary with the players and their game data
# def player_list_generator():    # This does not need to be a function, but I am practicing.
#     # players = {Player X: [token count, round points, roll counter]}
#     players = {}
#     while True:
#         player_amount = input("How many players[2 - 4]? ")
#         if player_amount.isnumeric() and 2 <= int(player_amount) <= 4:
#             for i in range(int(player_amount)):
#                 players[f"Player {i + 1}"] = [20, 0, 1]
#         else:
#             continue
#         break
#     return players

def player_list_generator():
    players = {}
    player_amount = ''
    while not (player_amount.isnumeric() and 2 <= int(player_amount) <= 4):
        player_amount = input("How many players[2 - 4]? ")
    for i in range(int(player_amount)):
        players[f"Player {i + 1}"] = {'tokens': 20, 'round_points': 0, 'roll_counter': 1}
    return players


# Needless but still practicing.
players_list = player_list_generator()
print(players_list)
print(players_list['Player 1']['roll_counter'])


# function to roll three dice with random numbers from 1 to 6
def roll_dice():
    return [random.randint(1, 6) for _ in range(3)]


# this will accept the result of the roll_dice func and the roll_total to calculate the roll score
def calculate_score(dice, roll_sum):
    if sorted(dice) in dice_set_points.values():
        for key, value in dice_set_points.items():
            if value == sorted(dice):
                return key
    else:
        for i in dice:
            roll_sum += single_die_points[i]
        return roll_sum


def play_round(round_points):
    # Here we will loop through the player_list dict to make sure each player has a turn.
    for player in player_list:
        # Using this to allow the game to hold and wait for the next player to get on the keyboard.
        input(f"\n{player}'s turn\nPress 'Enter' to continue...")
        # below roll_again has an error because 'it might be referenced before assignment'...
        # I am forcing the user below to assign it.  I am sure there is a better way.
        while player_list[player]['roll_counter'] <= 3 or roll_again != 'n':
            # In each loop we are resetting the roll_again input.
            roll_again = None
            # I am assigning the functions to variables to lock in the random roll and did the same for the score calc.
            player_roll = roll_dice()
            player_score = calculate_score(player_roll, round_points)
            print(f"\nRoll #{player_list[player]['roll_counter']}")
            print(f"{player} rolled: {player_roll}\nYour score is: {player_score}")

            # gives the player the option to roll again on roll 1 and 2.
            # If they roll again it will reset the round points to zero.
            # Now that I am using the functions I am not so sure if I need the global variable round_total
            # or define it in the function call?  Need to think about to finish the night.
            if player_list[player]['roll_counter'] < 3:
                while True:
                    roll_again = input("Would you like to roll again [y/n]? ").lower().strip()
                    if roll_again == 'y':
                        round_points = 0
                        break
                    # was unsure how to both ensure the user input would be either 'y' or 'n' and...
                    # if it was 'n' how to continue to the next if statement.  This is my solution.
                    elif roll_again == 'n':
                        break
                # if the player reaches the 3rd roll or opts to not roll again
                # It will total the existing rolls points.
                # In addition, it will reset their roll total and roll counter.
            if player_list[player]['roll_counter'] == 3 or roll_again == 'n':
                player_list[player]['round_points'] = player_score
                round_points = 0
                player_list[player]['roll_counter'] = 1
                print(f"Your current score is: {player_list[player]['round_points']}")
                print("Your turn is over...")
                break
            # increasing the roll counter.
            player_list[player]['roll_counter'] += 1
    # finding the player with the lowest score to determine who will receive all the tokens from the other players.
    print(players_list)
    # loser =
    # print(f"The loser of this round was {loser}")
# I need to store the users roll that they scored with to later determine the highest value roll
# and therefor determine how many chips to add/subtract!!!


player_list = player_list_generator()
play_round(roll_total)

# TODO: DONE...Advance through player_list and allow each player to use their turn.
#           Use a for loop for player in player_list
#       AFTER I MAKE THE GAME WORK...Create a way to play against a computer and create logic for it to always roll
#           again if its score is less than the player.
#       ALMOST THERE...Once each player has had a turn, compare their points and then remove tokens from
#           each player and add them to the player with the lowest score.
#               1 chip if the highest score is a points total (if the highest score is less than 300)
#               2 chips if the highest score is 1,2,3
#               3 chips if the highest score is three-of-a-kind
#               4 chips if the highest score is 4,5,6 (Zanzibar)
#       OH BOY...The player who won the previous round will begin the next round by rolling first.
#       This will continue until  one player has lost their tokens and declare the winner.
