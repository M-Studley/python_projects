import random


def player_generator():
    max_players = 6
    _players = {}
    while True:
        user_input = input("Please enter the amount of players from 1 - 6: ").strip().lower()
        if user_input.isnumeric() and int(user_input) in range(max_players):
            player_amount = int(user_input)
            break
        else:
            print("Not a valid amount...")

    for player_number in range(1, player_amount + 1):
        _players[f"player {player_number}"] = {'chips': 0, 'hand': [], 'bet_size': 0}

    _players['dealer'] = {'hand': []}
    return _players


# This function will need the player_list from player_generator()
def deposit(single_player=None):
    # make a copy of players
    _players = players
    # if they want a specific player, change our copy to just the one player
    if single_player:
        _players = [single_player]
    # _players is either a copy of players, or it's a single player now
    # note this is just for the iteration!
    for player in _players:
        if player == 'dealer':
            continue
        # from here on we're still using the real players{}
        while players[player]['chips'] == 0:
            user_input = input(f"Enter deposit amount for {player.upper()} (increments of 100): ")
            if user_input.isnumeric() and int(user_input) % 100 == 0:
                players[player]['chips'] += int(user_input)
            else:
                print("Not a valid amount...")


def generate_deck():
    _deck = []
    card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['clubs', 'spades', 'hearts', 'diamonds']
    for suit in suits:
        for value in card_values:
            _deck.append(f"{value.title()} of {suit.title()}")
    return _deck


def generate_shoe():
    max_deck_amount = 8
    shoe_deck_count = 0
    _shoe = []

    while not shoe_deck_count:
        user_input = input(f"How many decks would you like in the shoe [1 - {max_deck_amount}]? ").strip()
        if user_input.isnumeric() and int(user_input) in range(1, max_deck_amount + 1):
            shoe_deck_count = int(user_input)
        else:
            print("Not a valid amount...")

        for _ in range(shoe_deck_count):
            _shoe.extend(generate_deck())

    random.shuffle(_shoe)
    return _shoe


def take_deposits(player):
    make_deposit = None
    while make_deposit is None:
        user_input = input("You do not have enough chips to play.  Would you like to add more [y/n]? ")
        if user_input in ['y', 'n']:
            make_deposit = user_input == 'y'
    if make_deposit:
        deposit(player)


# will need the player_list from player_generator()
def get_bet_amount():
    for player in players:
        if player == 'dealer':
            continue
        if not players[player]['chips']:
            take_deposits(player)
        if players[player]['chips']:
            while not players[player]['bet_size']:
                user_input = input(f"Enter bet amount for {player.upper()} (increments of 100): ").strip()
                if user_input.isnumeric():
                    bet_amount = int(user_input)
                    if bet_amount % 100 == 0 and bet_amount <= players[player]['chips']:
                        players[player]['bet_size'] += bet_amount
                        players[player]['chips'] -= bet_amount
                else:
                    print("Not a valid amount...")


# we will need player_list from player_generator() and the shoe from shoe_generator()
def starting_deal():
    for _ in range(1, 3):
        for player in players:
            players[player]['hand'].append(shoe.pop())


# will need player_list from player_generator
# when sorting the dealers hand we will need to place under specific variable due to the up card
def hand_sorter(hand):
    # if ace in index 0 put ace in last position.
    for card in hand:
        if card[0].startswith('Ace'):
            last = hand.index(card[0])
            hand[-1], hand[last] = hand[last], hand[-1]
    return hand


# needs players hand: players['player 1']['hand'] OR player_hand = players['player 1']['hand']
# this will only work when the hand has been sorted by hand_sorter()
def get_hand_value(hand):
    hand_value = 0
    hand = hand_sorter(hand)
    for card in hand:
        card_name = card.split()[0]
        if card_name.isnumeric():
            hand_value += int(card_name)
        elif card_name in ['Jack', 'Queen', 'King']:
            hand_value += 10
        elif card_name == 'Ace':
            if hand_value > 10:
                hand_value += 1
            else:
                hand_value += 11
    return hand_value


def main(shoe, player_list):
    get_bet_amount(player_list)
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
        if get_hand_value(dealer_hand) == 21 and get_hand_value(player_hand) != 21:
            print(f"The dealers up card: {dealer_hand[1][0]}")
            print(f"{player} cards: {player_list[player]['hand']}\n"
                  f"{player} total: {get_hand_value(player_hand)}")
            print(f"The dealer has 21: {dealer_hand[0]} {dealer_hand[1]}")
            print(f"You lost {player_bet} chips")
        elif get_hand_value(player_hand) == 21:
            print(f"{player} has Blackjack!  You won {round(player_bet * 3)} chips")
            player_list[player]['chips'] += round(player_bet * 3) + player_bet
            player_list[player].update({'bj': True})
        elif get_hand_value(dealer_hand) == 21 and get_hand_value(player_hand) == 21:
            print(f"{player} and the Dealer both got 21.  It's a push.")
        else:  # Asking player to stay, hit or double
            print(f"The dealers up card: {dealer_hand[1][0]}")
            while get_hand_value(player_hand) < 21:
                print(f"{player} cards: {str(player_list[player]['hand'])}\n"
                      f"{player} total: {get_hand_value(player_hand)}")
                user_input = input(f"{player}: Stay[0] Hit[1] Double[2] ").strip().lower()
                if user_input.isnumeric() and int(user_input) in range(0, 3):
                    if int(user_input) == 1:
                        new_card = [shoe.pop(-1)]
                        player_hand += new_card
                        print(f"Your new card:", new_card[0][0])
                    elif int(user_input) == 2:
                        player_list[player]['chips'] -= player_bet
                        player_list[player]['bet_size'] = player_bet * 2
                        new_card = [shoe.pop(-1)]
                        player_hand += new_card
                        print(f"Your new card:", new_card[0][0])
                        print(f"{player} cards: {str(player_list[player]['hand'])}\n"
                              f"{player} total: {get_hand_value(player_hand)}")
                        break
                    else:
                        print(f"{player} stays with {get_hand_value(player_hand)}")
                        break
                else:
                    print("Not a valid input...")

            if get_hand_value(player_hand) >= 22:
                print(f"You busted!  You lost {player_bet}")
                print(f"You now have {str(player_list[player]['chips'])}")
                player_list[player].update({'bust': True})
            elif get_hand_value(player_hand) == 21:
                print("You have 21")

    # Dealer logic below
    print()
    dealer_finish = False
    dealer_hand = player_list['dealer']['hand']

    while not dealer_finish:
        print(f"Dealers cards are: {dealer_hand}\n"
              f"with the value of: {get_hand_value(dealer_hand)}")
        if (get_hand_value(dealer_hand) < 17 or
                (dealer_hand[-1][0][0] == 'A' and get_hand_value(dealer_hand) == 17)):
            print(f"The dealer will hit")
            new_card = [shoe.pop(-1)]
            dealer_hand += new_card
            print(f"Dealers new card:", new_card[0][0])
        elif 17 <= get_hand_value(dealer_hand) <= 21:
            print(f"The dealer has {get_hand_value(dealer_hand)} and will stay.")
            dealer_finish = True
        else:
            print("The Dealer busted!")
            dealer_finish = True

    for player in player_list:
        dealer_hand_value = get_hand_value(player_list['dealer']['hand'])
        player_hand_value = get_hand_value(player_list[player]['hand'])

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
            player_list[player]['chips'] += player_list[player]['bet_size'] * 2
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


if __name__ == "__main__":
    shoe = generate_shoe()
    players = player_generator()
    deposit()

    main(all_cards, players)

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
