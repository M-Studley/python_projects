import random

player_amount = int(input("How many players? "))
players_list = {}       # {Player X: [token count, roll counter, existing turn bool]}

# if there is one player it will add a computer player.
# if more than one it will populate the dictionary with the # of players and set the Player 1 turn bool to True.
if player_amount == 1:
    players_list[f"Player {player_amount}"] = [20, 1, True]
    players_list["Computer"] = [20, 1, False]
else:
    for i in range(player_amount):
        players_list[f"Player {i + 1}"] = [20, 1, False]
    players_list["Player 1"][2] = True
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
#
while roll_counter <= 3 or roll_again != 'n':
    roll_again = None
    dice = {'die_one': random.randrange(1, 7),
            'die_two': random.randrange(1, 7),
            'die_three': random.randrange(1, 7)}

    print(f"Roll #{roll_counter}")
    print(f"You rolled: {list(dice.values())}")

    if list(sorted(dice.values())) in dice_set_points.values():
        for key, value in dice_set_points.items():
            if value == list(sorted(dice.values())):
                roll_total += key
        print(f"Roll total: {roll_total}")
    else:
        for i in list(dice.values()):
            roll_total += single_die_points[i]
        print(f"Roll total: {roll_total}")

    if roll_counter < 3:
        while True:
            roll_again = input("Would you like to roll again [y/n]? ").lower().strip()
            if roll_again == 'y':
                roll_total = 0
                break
            elif roll_again == 'n':
                break
    if roll_counter == 3 or roll_again == 'n':
        players_list['Player 1'] += roll_total
        roll_total = 0
        roll_counter = 1
        print(f"Your current score is: {players_list['Player 1']}")
        print("Your turn is over...")
        break
    roll_counter += 1

print(players_list)
