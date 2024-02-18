import random


def player_generator():
    player_amount = ''
    player_list = {}
    while not player_amount.isnumeric():
        user_input = input("Please enter the amount of players from 1 - 6: ").strip().lower()
        if user_input.isnumeric() and int(user_input) in range(1, 7):
            player_amount = int(user_input)
            break
        else:
            print("Not a valid amount...")

    for num in range(player_amount):
        player_list[f"player {num + 1}"] = {'chips': 0, 'hand': list(), 'bet_size': 0}

    player_list['dealer'] = {'hand': list()}
    return player_list


# This function will need the player_list from player_generator()
def bank_deposit(players):
    for player in players.keys():
        if player == 'dealer':
            continue
        while players[player]['chips'] == 0:
            user_input = input(f"Enter deposit amount for {player.upper()} (increments of 100): ")
            if user_input.isnumeric() and int(user_input) % 100 == 0:
                players[player]['chips'] += int(user_input)
            else:
                print("Not a valid amount...")
    return players


def shoe_generator():
    card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['clubs', 'spades', 'hearts', 'diamonds']
    deck_amount = ''
    shoe = []
    while not deck_amount.isnumeric():
        user_input = input("How many decks would you like in the shoe [1 - 8]? ").strip().lower()
        if user_input.isnumeric() and int(user_input) in range(1, 9):
            deck_amount = int(user_input)
            break
        else:
            print("Not a valid amount...")

    for _ in range(deck_amount):
        for suit in suits:
            for value in card_values:
                shoe += [[f"{value.title()} of {suit.title()}"]]
    random.shuffle(shoe)
    return shoe


# will need the player_list from player_generator()
def bet_amount(players):
    for player in players.keys():
        if player == 'dealer':
            continue
        if players[player]['chips'] < 100:
            print(f"You do not have enough chips to play.  Would you like to add more [y/n]? ")
        while players[player]['bet_size'] == 0:
            user_input = input(f"Enter bet amount for {player.upper()} (increments of 100): ").strip().lower()
            if user_input.isnumeric() and int(user_input) % 100 == 0 and int(user_input) <= players[player]['chips']:
                players[player]['bet_size'] += int(user_input)
                players[player]['chips'] -= int(user_input)
            else:
                print("Not a valid amount...")
    return players


# we will need player_list from player_generator() and the shoe from shoe_generator()
def starting_deal(players, cards):
    for i in range(1, 3):
        for player in list(players.keys()):
            players[player]['hand'] += [cards.pop(-1)]
    return players


# will need player_list from player_generator
# when sorting the dealers hand we will need to place under specific variable due to the up card
def hand_sorter(hand):
    for card in hand:
        if card[0][0] == 'A':
            ace = card
            last = hand.index(ace)
            hand[-1], hand[last] = hand[last], hand[-1]
    return hand


# needs players hand: players['player 1']['hand'] OR player_hand = players['player 1']['hand']
# this will only work when the hand has been sorted by hand_sorter()
def hand_value(hand):
    value = 0
    hand_sorter(hand)
    for card in hand:
        split_card = card[0].split(" ")
        if split_card[0].isnumeric():
            value += int(split_card[0])
        elif split_card[0] in ['Jack', 'Queen', 'King']:
            value += 10
        elif split_card[0] == 'Ace':
            if value > 10:
                value += 1
            else:
                value += 11
    return value


all_cards = shoe_generator()
people = player_generator()
bank_deposit(people)
######################
while play_again:
    bet_amount(player_list)
    starting_deal(player_list, shoe)
    print("***")
    print(player_list)
    print("***")
    for player in player_list:
        if player == 'dealer':
            continue
        dealer_hand = player_list['dealer']['hand']
        player_hand = player_list[player]['hand']
        player_bet = player_list[player]['bet_size']
        print()

        # BJ, Dealer 21 or BJ & Dealer 21 in starting hand check.
        if hand_value(dealer_hand) == 21 and hand_value(player_hand) != 21:
            print(f"The dealers up card: {dealer_hand[1][0]}")
            print(f"{player} cards: {player_list[player]['hand']}\n"
                  f"{player} total: {hand_value(player_hand)}")
            print(f"The dealer has 21: {dealer_hand[0]} {dealer_hand[1]}")
            print(f"You lost {player_bet} chips")
        elif hand_value(player_hand) == 21:
            print(f"{player} has Blackjack!  You won {round(player_bet*3)} chips")
            player_list[player]['chips'] += round(player_bet*3) + player_bet
            player_list[player].update({'bj': True})
        elif hand_value(dealer_hand) == 21 and hand_value(player_hand) == 21:
            print(f"{player} and the Dealer both got 21.  It's a push.")
        else:   # Asking player to stay, hit or double
            print(f"The dealers up card: {dealer_hand[1][0]}")
            while hand_value(player_hand) < 21:
                print(f"{player} cards: {str(player_list[player]['hand'])}\n"
                      f"{player} total: {hand_value(player_hand)}")
                user_input = input(f"{player}: Stay[0] Hit[1] Double[2] ").strip().lower()
                if user_input.isnumeric() and int(user_input) in range(0, 3):
                    if int(user_input) == 1:
                        new_card = [shoe.pop(-1)]
                        player_hand += new_card
                        print(f"Your new card:", new_card[0][0])
                    elif int(user_input) == 2:
                        player_list[player]['chips'] -= player_bet
                        player_list[player]['bet_size'] = player_bet*2
                        new_card = [shoe.pop(-1)]
                        player_hand += new_card
                        print(f"Your new card:", new_card[0][0])
                        print(f"{player} cards: {str(player_list[player]['hand'])}\n"
                              f"{player} total: {hand_value(player_hand)}")
                        break
                    else:
                        print(f"{player} stays with {hand_value(player_hand)}")
                        break
                else:
                    print("Not a valid input...")

            if hand_value(player_hand) >= 22:
                print(f"You busted!  You lost {player_bet}")
                print(f"You now have {str(player_list[player]['chips'])}")
                player_list[player].update({'bust': True})
            elif hand_value(player_hand) == 21:
                print("You have 21")

    # Dealer logic below
    print()
    dealer_finish = False
    dealer_hand = player_list['dealer']['hand']

    while not dealer_finish:
        print(f"Dealers cards are: {dealer_hand}\n"
              f"with the value of: {hand_value(dealer_hand)}")
        if (hand_value(dealer_hand) < 17 or
                (dealer_hand[-1][0][0] == 'A' and hand_value(dealer_hand) == 17)):
            print(f"The dealer will hit")
            new_card = [shoe.pop(-1)]
            dealer_hand += new_card
            print(f"Dealers new card:", new_card[0][0])
        elif 17 <= hand_value(dealer_hand) <= 21:
            print(f"The dealer has {hand_value(dealer_hand)} and will stay.")
            dealer_finish = True
        else:
            print("The Dealer busted!")
            dealer_finish = True

    for player in player_list:
        dealer_hand_value = hand_value(player_list['dealer']['hand'])
        player_hand_value = hand_value(player_list[player]['hand'])

        if player == 'dealer':
            continue

        print(f"\n{player} has {player_hand_value}\n"
              f"The dealer has {dealer_hand_value}")

        if 'bust' or 'bj' in player_list[player]:
            if 'bust' in player_list[player]:
                print(f"{player} busted...")
                player_list[player]['hand'] = list()
                player_list[player]['bet_size'] = 0
                del player_list[player]['bust']
            elif 'bj' in player_list[player]:
                print(f"You got a Blackjack!")
                player_list[player]['hand'] = list()
                player_list[player]['bet_size'] = 0
                del player_list[player]['bj']
        # else:
        if player_hand_value == dealer_hand_value:
            player_list[player]['chips'] += player_list[player]['bet_size']
            print(f"It's a push.  Your balance is: {player_list[player]['chips']}")
        elif player_hand_value > dealer_hand_value or dealer_hand_value > 21:
            player_list[player]['chips'] += player_list[player]['bet_size']*2
            print(f"You won {player_list[player]['bet_size']}\n"
                  f"Your balance is: {player_list[player]['chips']}")
        elif player_hand_value < dealer_hand_value:
            print(f"The Dealer won.  You lost: {player_list[player]['bet_size']}\n"
                  f"Your balance is: {player_list[player]['chips']}")

        player_list[player]['bet_size'] = 0
        player_list[player]['hand'] = list()

    play_again = ''
    while play_again not in ['y', 'n']:
        user_input = input("Would you like to play another hand [y/n]? ").strip().lower()
        if user_input in ['y', 'n']:
            play_again = user_input
        else:
            print("Not a valid input...")
    play_again = ''
    if play_again not in ['', 'y']:
        quit()
    else:
        player_list['dealer']['hand'] = list()
        main(all_cards, people)



# TODO:
#  DONE 1.  store the player(s) zero chip amount to start and the hand [] (allow for split hands).
#  DONE 2.  ask the player to deposit into their bank (increments of 100 only).
#  DONE 3.  generate a shoe with X amount of decks (if shoe has been used 50%, repeat step 3).
#  DONE 4.  ask the user how much they would like to bet for this hand (min bet = 100).
#  DONE 5.  deal the opening hands.
#  DONE 6.  determine the hands values (helper function for sorting hands).
#  DONE 7.  check for player BJ, dealer 21.
#  DONE 8.  show the dealers up card (prior to sorting the hand).
#  DONE 9.  total the amount of the dealer and users hands and display users total for them.
#  DONE 10.  ask the user if they want to hit, stay, double or split.
#      DONE a. if hit, deal a card from the top of the shuffled shoe.
#          DONE I.  check total for bust or 21.
#         DONE II. repeat step 8 until the user either hits 21, busts or opts to stay.
#      DONE b. if double, double the bet and allow user to draw one more card, then move to step 9.
#           c. if split, split the users hand into two hands and cycle through both using step 8.
#      DONE d. if stay or dealer 21, allow the dealer to play their turn.
#          DONE I.  follow BJ dealer rules (hit on < 17 and soft 17).
#  DONE 11. add or subtract from users bank if win or lose.
#  DONE 12. ask the player if they would like to begin another hand.
#  LINE 63 ADD MORE MONEY.
#  WHEN DOUBLING CHECK THE PLAYERS CHIP AMOUNT.
#  CHANGE BET SIZE TO BET.
#  CHANGE CHIPS TO BALANCE.
