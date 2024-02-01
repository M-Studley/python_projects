import random

# counter will be able to identify the player number and where to...
# remove/add tokens, increase roll counter, tally points and determine the turn status.
counter = 1
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
# Asks how many players and validates if it is a number
while True:
    player_amount = input("How many players? ")
    if player_amount.isnumeric() and int(player_amount) > 1:
        # player_list = {Player X: [token count, points, roll counter, existing turn bool]}
        players_list = {}
        # if there is one player it will add a computer player.
        if int(player_amount) == 1:
            players_list[f"Player {int(player_amount)}"] = [20, 0, 1, True]
            players_list["Computer"] = [20, 0, 1, False]
        # If more than one player, it will populate dictionary with # of players
        # And set Player 1 "turn bool" to True.
        else:
            for i in range(int(player_amount)):
                players_list[f"Player {i + 1}"] = [20, 0, 1, False]
            players_list["Player 1"][3] = True
    else:
        continue
    break

# I need to break this section into functions.
while players_list[f"Player {counter}"][2] <= 3 or roll_again != 'n':
    # Each loop will reset the roll_again value to None.
    roll_again = None
    # Create a list of three dice with random values.
    dice = [random.randint(1, 6) for _ in range(3)]

    print(f"Roll #{players_list[f"Player {counter}"][2]}")
    print(f"You rolled: {dice}")

    # checking to see if the dice values match either dict and calculates the scores.
    # Sorting the dice to match the values in the dice_set_points dictionary.
    if sorted(dice) in dice_set_points.values():
        for key, value in dice_set_points.items():
            if value == sorted(dice):
                roll_total += key
        print(f"Roll total: {roll_total}")
    else:
        for i in dice:
            roll_total += single_die_points[i]
        print(f"Roll total: {roll_total}")

    # gives the player the option to roll again on roll 1 and 2.
    # If they roll again it will reset the roll total to zero.
    if players_list[f"Player {counter}"][2] < 3:
        while True:
            roll_again = input("Would you like to roll again [y/n]? ").lower().strip()
            if roll_again == 'y':
                roll_total = 0
                break
            # was unsure how to both ensure the user input would be either 'y' or 'n' and...
            # if it was 'n' how to continue to the next if statement.  This is my solution.
            elif roll_again == 'n':
                break
    # if the player reaches the 3rd roll or opts to not roll again
    # It will total the existing rolls points.
    # In addition, it will reset their roll total and roll counter.
    if players_list[f"Player {counter}"][2] == 3 or roll_again == 'n':
        players_list[f"Player {counter}"][1] += roll_total
        roll_total = 0
        players_list[f"Player {counter}"][2] = 1
        print(f"Your current score is: {players_list[f"Player {counter}"][1]}")
        print("Your turn is over...")
        break
    # increasing the roll counter.
    players_list[f"Player {counter}"][2] += 1

print(players_list[f"Player {counter}"][1])

# TODO: Advance through player_list and allow each player to use their turn.
#           Use a for loop for player in player_list
#       Create a way to play against a computer and create logic for it to always roll again
#           if its score is less than the player.
#       Once each player has had a turn, compare their points and then remove tokens from
#           each player and add them to the player with the lowest score.
#               1 chip if the highest score is a points total (if the highest score is less than 300)
#               2 chips if the highest score is 1,2,3
#               3 chips if the highest score is three-of-a-kind
#               4 chips if the highest score is 4,5,6 (Zanzibar)
#       The player who won the previous round will begin the next round by rolling first.
#       This will continue until  one player has lost their tokens and declare the winner.
