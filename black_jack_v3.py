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
        _players[f"player {player_number}"] = {'balance': 0, 'hand': [], 'bet': 0}

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
        while players[player]['balance'] == 0:
            user_input = input(f"Enter deposit amount for {player.upper()} (minimum of 1000): ")
            if user_input.isnumeric() and int(user_input) >= 1000:
                players[player]['balance'] += int(user_input)
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
        if not players[player]['balance']:
            take_deposits(player)
        if players[player]['balance']:
            while not players[player]['bet']:
                user_input = input(f"Enter bet amount for {player.upper()} (increments of 100): ").strip()
                if user_input.isnumeric():
                    bet_amount = int(user_input)
                    if bet_amount % 100 == 0 and bet_amount <= players[player]['balance']:
                        players[player]['bet'] += bet_amount
                        players[player]['balance'] -= bet_amount
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
    for index, card in enumerate(hand):
        if card.startswith('Ace'):
            hand[index], hand[-1] = hand[-1], hand[index]
    return hand


# needs players hand: players['player 1']['hand'] OR player_hand = players['player 1']['hand']
# this will only work when the hand has been sorted by hand_sorter()
def get_hand_value(hand):
    hand_value = 0
    for card in hand:
        card_name = card.split()[0]
        if card_name.isnumeric():
            hand_value += int(card_name)
        elif card_name in ['Jack', 'Queen', 'King']:
            hand_value += 10
        elif card_name == 'Ace':
            if len(hand) == 2 and hand_value > 10:
                hand_value += 1
            elif len(hand) > 2 and hand_value >= 10:
                hand_value += 1
            else:
                hand_value += 11
    return hand_value


# dealer logic - hit on soft 17 or below hard 17
def dealer_turn(player_list):
    dealer_finish = False
    dealer_hand = player_list['dealer']['hand']
    dealer_hand_value = get_hand_value(hand_sorter(dealer_hand))
    while not dealer_finish:
        print(f"Dealers cards are: {dealer_hand}\n"
              f"Hand Value: {dealer_hand_value}\n")
        if dealer_hand_value < 17 or ('Ace' in dealer_hand and dealer_hand_value == 17):
            print(f"The dealer will hit...")
            new_card = [shoe.pop()]
            dealer_hand += new_card
            hand_sorter(dealer_hand)
            dealer_hand_value = get_hand_value(dealer_hand)
            print(f"Dealers new card: {new_card[0]}")
        elif 17 <= dealer_hand_value <= 21:
            print(f"The dealer has {dealer_hand_value} and will stay.\n")
            dealer_finish = True
        else:
            print("The Dealer busted!")
            dealer_finish = True


def check_for_21(player_list, player, dealer_cards, sorted_player_hand, bet_amount):
    # BJ, Dealer 21 or BJ & Dealer 21 in starting hand check.
    if get_hand_value(dealer_cards) == 21 and get_hand_value(sorted_player_hand) == 21:
        print(f"{player} and Dealer both have 21.")
        player_list[player].update({'bj_push': True})
        player_list['dealer'].update({'dealer_21': True})
        return True
    elif get_hand_value(dealer_cards) == 21 and get_hand_value(sorted_player_hand) != 21:
        print(f"{player} cards: {sorted_player_hand}\n"
              f"{player} total: {get_hand_value(sorted_player_hand)}")
        print(f"The dealer has 21: {dealer_cards[0]} & {dealer_cards[1]}")
        player_list['dealer'].update({'dealer_21': True})
        return True
    elif get_hand_value(sorted_player_hand) == 21:
        print(f"{player} has Blackjack!")
        player_list[player]['balance'] += round(bet_amount * 3)
        player_list[player].update({'bj': True})
        return True
    return False


def main(shoe, player_list):
    get_bet_amount()
    starting_deal()
    print()
    for player in player_list:
        if player == 'dealer':
            continue
        dealer_hand = player_list['dealer']['hand']
        player_hand_sorted = hand_sorter(player_list[player]['hand'])
        player_bet = player_list[player]['bet']

        if check_for_21(player_list, player, dealer_hand, player_hand_sorted, player_bet):
            break
        else:
            print(f"The dealers up card: {dealer_hand[1]}\n")

        while get_hand_value(player_hand_sorted) < 21:
            print(f"{player} cards: {player_hand_sorted}\n"
                  f"{player} total: {get_hand_value(player_hand_sorted)}\n")
            user_input = input(f"{player}: Stay[0] Hit[1] Double[2] ").strip()
            if user_input.isnumeric() and int(user_input) in range(0, 3):
                if int(user_input) == 1:
                    new_card = [shoe.pop()]
                    player_hand_sorted += new_card
                    player_hand_sorted = hand_sorter(player_hand_sorted)
                    print(f"\nYour new card:", new_card[0])
                elif int(user_input) == 2:
                    if player_list[player]['balance'] >= player_bet * 2:
                        player_list[player]['balance'] -= player_bet
                        player_list[player]['bet'] = player_bet * 2
                        new_card = [shoe.pop()]
                        player_hand_sorted += new_card
                        player_hand_sorted = hand_sorter(player_hand_sorted)
                        print(f"\nYour new card: {new_card[0]}")
                        print(f"{player} cards: {player_hand_sorted}\n"
                              f"{player} total: {get_hand_value(player_hand_sorted)}")
                        break
                    else:
                        print("You do no have enough chips to double...")
                        continue
                else:
                    print(f"{player} stays with {get_hand_value(player_hand_sorted)}\n")
                    break
            else:
                print("Not a valid input...")

        if get_hand_value(player_hand_sorted) >= 22:
            print(f"You busted!")
            player_list[player].update({'bust': True})
        elif get_hand_value(player_hand_sorted) == 21:
            print("You have 21")
            player_list[player].update({'player_21': True})

    # Dealer turn
    if len(player_list) == 2:
        if 'bust' not in player_list['player 1']:
            if 'bj' not in player_list['player 1']:
                if 'bj_push' not in player_list['player 1']:
                    if 'dealer_21' not in player_list['dealer']:
                        dealer_turn(player_list)
    if len(player_list) > 2:
        dealer_turn(player_list)

    for player in player_list:
        dealer_hand_value = get_hand_value(player_list['dealer']['hand'])
        player_hand_value = get_hand_value(player_list[player]['hand'])

        if player == 'dealer':
            continue

        print(f"\n{player} has {player_hand_value}\n"
              f"The dealer has {dealer_hand_value}")

        if 'bust' in player_list[player]:
            print(f"{player} busted...  "
                  f"You lost: {player_list[player]['bet']}  "
                  f"Your balance is: {player_list[player]['balance']}")
        elif 'bj' in player_list[player]:
            print(f"You got a Blackjack!  "
                  f"You won: {player_list[player]['bet'] * 3}  "
                  f"Your balance is: {player_list[player]['balance']}")
        elif player_hand_value == dealer_hand_value:
            player_list[player]['balance'] += player_list[player]['bet']
            print(f"It's a push.  Your balance is: {player_list[player]['balance']}")
        elif player_hand_value > dealer_hand_value or dealer_hand_value > 21:
            player_list[player]['balance'] += player_list[player]['bet'] * 2
            print(f"You won {player_list[player]['bet']}\n"
                  f"Your balance is: {player_list[player]['balance']}")
        elif player_hand_value < dealer_hand_value:
            print(f"The Dealer won...\n"
                  f"You lost: {player_list[player]['bet']}\n"
                  f"Your balance is: {player_list[player]['balance']}")

        player_list[player] = {'balance': player_list[player]['balance'], 'hand': [], 'bet': 0}

    play_again = ''
    while play_again not in ['y', 'n']:
        user_input = input("\nWould you like to play another hand [y/n]? ").strip().lower()
        if user_input in ['y', 'n']:
            play_again = user_input
        else:
            print("Not a valid input...")
    if play_again not in ['', 'y']:
        quit()
    else:
        player_list['dealer'] = {'hand': []}
        print("\n"*8)
        print("*" * 88)
        print("\n"*8)
        main(shoe, players)


if __name__ == "__main__":
    shoe = generate_shoe()
    players = player_generator()
    deposit()

    main(shoe, players)
