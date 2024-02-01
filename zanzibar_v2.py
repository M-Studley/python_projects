import random
import os

# Three dice combo points.
dice_set_points = {1000: [4, 5, 6],
                   900: [1, 1, 1],
                   800: [2, 2, 2],
                   700: [3, 3, 3],
                   600: [4, 4, 4],
                   500: [5, 5, 5],
                   400: [6, 6, 6],
                   300: [1, 2, 3]}
# Point totals for individual dice.
single_die_points = {1: 100,
                     6: 60,
                     2: 2,
                     3: 3,
                     4: 4,
                     5: 5}


# Asks how many players [2-4] and validates if it is a number.
# Then will generate a dictionary with the players and their starting 20 tokens.  Using 5 for testing.
def player_list_generator():
    players = {}
    player_amount = ''
    while not (player_amount.isnumeric() and 1 <= int(player_amount) <= 4):
        player_amount = input("\nHow many players[1 - 4]? ")
    if int(player_amount) > 1:
        for i in range(int(player_amount)):
            players[f"Player {i + 1}"] = 5
    # if player number is one it will generate Player 1 and a Computer player.
    players = {'Player 1': 5,
               'Computer': 5}
    return players


# function to roll three dice with random numbers from 1 to 6
def roll_dice():
    return [random.randint(1, 6) for _ in range(3)]


# this will accept the result of the roll_dice func and the roll_total to calculate the roll score
def calculate_score(dice, roll_sum):
    for key in dice_set_points:
        if dice_set_points[key] == sorted(dice):
            return key
    for i in dice:
        roll_sum += single_die_points[i]
    return roll_sum


# Creating the logic for the computer to play against the human player.
def computer(dictionary):
    roll_total = 0
    roll_count = 1
    while roll_count <= 3:
        player_roll = roll_dice()
        player_score = calculate_score(player_roll, roll_total)
        print(f"\nRoll #{roll_count}: {player_roll} for {player_score} points.")
        if roll_count == 3 or player_score >= 300 or player_score > dictionary['Player 1']:
            print(f"\nThe computer kept their last roll.")
            print(f"The computers score is {player_score}.\n")
            dictionary['Computer'] = player_score
            return
        roll_count += 1


def play_round():
    # for each player the roll counter will be set to one and roll_total to zero.  High_low will be cleared.
    high_low = {}
    roll_counter = 1
    roll_total = 0
    # Here we will loop through the player_list dict to make sure each player has a turn.
    for player in player_list:
        # Here I am making sure the roll_again input is set to an empty string
        roll_again = ''
        # Using this to allow the game to hold and wait for the next player to get on the keyboard.
        input(f"\n{player}'s turn\nPress 'Enter' to continue...")
        os.system('cls')
        while roll_counter <= 3 or roll_again != 'n':
            # Checking if the player is Computer and if so it will call the computer func
            # to allow the computer to take its turn and then once completed it will break out
            # to advance to the next player.
            if player == 'Computer':
                computer(high_low)
                break
            # In each loop we are resetting the roll_again input.
            roll_again = ''
            # I am assigning the functions to variables to lock in the random roll and did the same for the score calc.
            player_roll = roll_dice()
            player_score = calculate_score(player_roll, roll_total)
            print(f"\nRoll #{roll_counter}")
            if player_score == 1000:
                print("ZANZIBAR!")
            print(f"{player} rolled: {player_roll}\nYour score is: {player_score}")
            # gives the player the option to roll again on roll 1 and 2.
            # If they roll again it will reset the roll_total to zero.
            if roll_counter < 3:
                while roll_again not in ['y', 'n']:
                    roll_again = input("Would you like to roll again [y/n]? ").lower().strip()
                    if roll_again == 'y':
                        roll_total = 0
                # if the player reaches the 3rd roll or opts to not roll again
                # It will total the existing rolls points and add that to their score.
                # In addition, it will reset their roll total and roll counter.
            if roll_counter == 3 or roll_again == 'n':
                roll_counter = 1
                # creating a dictionary to determine the player that has the lowest score (will receive tokens)
                # And the highest roll value to determine the amount of tokens they will receive from each player.
                high_low[player] = player_score
                print(f"Your current score is: {player_score}")
                print("Your turn is over...")
                break
            # increasing the roll counter.
            roll_counter += 1
    # finding the player with the lowest value and the highest roll in the high_low dict.
    loser = min(high_low, key=high_low.get)
    highest_roll = max(high_low.values())
    # Assigning the correct amount of tokens to remove/add
    if highest_roll < 300:
        token_count = 1
    elif highest_roll == 300:
        token_count = 2
    elif highest_roll in range(301, 1000):
        token_count = 3
    else:
        token_count = 4
    print(f"The loser of this round was {loser}")
    print(f"Each player will give {loser}... {token_count} token(s).\n")
    # adding and subtracting tokens from the winners and losers.
    # Also checking to see after the round if any player has zero tokens.  If so, declare the winner and exit the game
    for player in player_list:
        if player != loser:
            player_list[player] -= token_count
        else:
            player_list[loser] += (len(player_list) - 1) * token_count
        # Determining the winner
        if player_list[player] <= 0:
            print(f"The winner of the game is {player}!!!")
            return
    # If no winner, the function will call itself again until there is one.
    for player in player_list:
        print(f"{player} has {player_list[player]} tokens")
    play_round()


player_list = player_list_generator()
play_round()
play_again = ''
while play_again not in ['y', 'n']:
    play_again = input("Would you like to play again [y/n]? ")
if play_again == 'y':
    os.system('cls')
    player_list = player_list_generator()
    play_round()
else:
    input(f"Press 'Enter' to exit the game")


# TODO:
#       Figure out what to do if there is a tie between players
#           Especially if there are only 2 players.
#           But need to take care of this even if there are 4 players.
#       The player who won the previous round will begin the next round by rolling first.
#           Having trouble thinking of a way to do this.
#           One way would be to also store the winning player of the round in the high_low func
#           then maybe reorder the player list???
#           maybe before resetting the high_low, sort the dict in reverse... IDK
