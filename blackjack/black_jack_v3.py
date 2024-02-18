import random


# iterating through the card values and suits to create a deck of 52 cards ace to king for all 4 suits.
def generate_deck() -> list:
    _deck = []
    card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['clubs', 'spades', 'hearts', 'diamonds']
    for suit in suits:
        for value in card_values:
            _deck.append(f"{value.title()} of {suit.title()}")
    return _deck


# this will generate X amount of decks to place in the shoe for the game to deal from.
def generate_shoe() -> list:
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


# ask user for number of players.  generates a dictionary with the number of players and a dealer at the end.
# each player will have a balance and bet set to 0 and hand set to an empty list.
def player_generator() -> dict:
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
        _players[f"player {player_number}"] = {'balance': 0, 'bet': 0, 'hands': {}}

    _players['dealer'] = {'hands': {}, 'soft': False}
    return _players


# accepts a deposit amount from a single player.  this will be added to the players balance.
def deposit(single_player=None) -> None:
    # make a copy of players
    _players = players
    # if they want a specific player, change our copy to just the one player
    if single_player:
        _players = [single_player]
    # _players is either a copy of players, or it's a single player now
    # note this is just for the iteration!
    for active_player in _players:
        if active_player == 'dealer':
            continue
        # from here on we're still using the real players{}
        while players[active_player]['balance'] == 0:
            user_input = input(f"Enter deposit amount for {active_player.upper()} (minimum of 1000): ")
            if user_input.isnumeric() and int(user_input) >= 1000:
                players[active_player]['balance'] += int(user_input)
            else:
                print("Not a valid amount...")


# this is used to add to their balance if the player does not have enough.  this will only be asked only for...
# the initial bet and not when doubling.
def take_deposits(active_player) -> None:
    make_deposit = ''
    while len(make_deposit) == 0:
        user_input = input("You do not have enough in your balance to play.  "
                           "Would you like to add more [y/n]? ").strip().lower()
        if user_input in ['y', 'n']:
            make_deposit = user_input
    if make_deposit == 'y':
        deposit(active_player)


# asks each player how much they would like to bet on their hand, checks their balance, removes the bet amount...
# from their balance and places it into the players bet.
def get_bet_amount() -> None:
    for active_player in players:
        if active_player == 'dealer':
            continue
        if not players[active_player]['balance']:
            take_deposits(active_player)
        if players[active_player]['balance']:
            while not players[active_player]['bet']:
                user_input = input(f"Enter bet amount for {active_player.upper()} (increments of 100): ").strip()
                if user_input.isnumeric():
                    bet_amount = int(user_input)
                    if bet_amount % 100 == 0 and bet_amount <= players[active_player]['balance']:
                        players[active_player]['bet'] += bet_amount
                        players[active_player]['balance'] -= bet_amount
                else:
                    print("Not a valid amount...")


# for all players, including the dealer, will receive two cards to begin the game.
def starting_deal() -> None:
    for active_player in players:
        players[active_player]['hands'].update({'hand 1': [shoe.pop(), shoe.pop()]})


# this is a helper function to sort the hand and place aces at the end of the players hand list[]...
# for ease of calculating the hand value.
def hand_sorter(hand) -> list:
    for index, card in enumerate(hand):
        if card.startswith('Ace'):
            hand[index], hand[-1] = hand[-1], hand[index]
    return hand


# calculating the hand value.  10, j, q, k = 10, number cards = number and ace = 1 or 11.
# identifies a soft 17 for the dealer and later will be used to determine if the dealer hits or stays.
def get_hand_value(hand, player_list) -> int:
    hand_value = 0
    num_aces = 0
    for card in hand:
        card_name = card.split()[0]
        if card_name.isnumeric():
            hand_value += int(card_name)
        elif card_name in ['Jack', 'Queen', 'King']:
            hand_value += 10
        elif card_name == 'Ace':
            num_aces += 1
            hand_value += 11
    while num_aces > 0 and hand_value > 21:
        hand_value -= 10
        num_aces -= 1
    if num_aces == 1:
        player_list['dealer']['soft'] = True
    else:
        player_list['dealer']['soft'] = False

    return hand_value


# determines if the opening hand of the player vs dealer results in a push (21 & 21), dealer BJ, or player BJ.
# This will return a bool. True to stop play or False to continue play.
def check_for_21(player_list, active_player, dealer_cards, sorted_player_hand, bet_amount) -> bool:
    if (get_hand_value(dealer_cards, player_list) == 21
            and get_hand_value(sorted_player_hand, player_list) == 21):
        print(f"{active_player} and Dealer both have 21.")
        player_list[active_player].update({'bj_push': True})
        player_list['dealer'].update({'dealer_21': True})
        return True
    elif (get_hand_value(dealer_cards, player_list) == 21 and
          get_hand_value(sorted_player_hand, player_list) != 21):
        print(f"{active_player} cards: {sorted_player_hand}\n"
              f"{active_player} total: {get_hand_value(sorted_player_hand, player_list)}")
        print(f"The dealer has 21: {dealer_cards[0]} & {dealer_cards[1]}")
        player_list['dealer'].update({'dealer_21': True})
        return True
    elif get_hand_value(sorted_player_hand, player_list) == 21:
        print(f"{active_player} has Blackjack!")
        player_list[active_player]['balance'] += round(bet_amount * 3)
        player_list[active_player].update({'bj': True})
        return True
    return False


def split_hand(player_list, active_player):
    hands = player_list[player]['hands']
    popped_card = player_list[player]['hands']['hand 1'].pop()
    hand_counter = 2
    player_list[active_player]['hands'].update({f'hand {hand_counter}': popped_card})
    hand_counter += 1
    for hand in hands:
        print("hand in hands: ", hand)


# this will use the check for 21 function if it returns true this func will return the sorted players hand to exit.
# if check for 21 is False, we ask the player if they will stay, hit or double.
# this will continue until the player either busts, hits 21 or chooses to stay.
def player_choices(player_list, active_player) -> list:
    dealer_hand = player_list['dealer']['hands']['hand 1']
    sorted_player_hand = hand_sorter(player_list[active_player]['hands']['hand 1'])
    player_bet = player_list[active_player]['bet']

    if check_for_21(player_list, active_player, dealer_hand, sorted_player_hand, player_bet):
        return sorted_player_hand
    else:
        print(f"The dealers up card: {dealer_hand[1]}\n")

    while get_hand_value(sorted_player_hand, player_list) < 21:
        print(f"{active_player} cards: {sorted_player_hand}\n"
              f"{active_player} total: {get_hand_value(sorted_player_hand, player_list)}\n")
        user_input = input(f"{active_player}: Stay[0] Hit[1] Double[2] ").strip()
        if user_input.isnumeric() and int(user_input) in range(3):
            if int(user_input) == 1:
                new_card = [shoe.pop()]
                sorted_player_hand += new_card
                sorted_player_hand = hand_sorter(sorted_player_hand)
                print(f"\nYour new card:", new_card[0])
            elif int(user_input) == 2:
                if player_list[active_player]['balance'] >= player_bet * 2:
                    player_list[active_player]['balance'] -= player_bet
                    player_list[active_player]['bet'] = player_bet * 2
                    new_card = [shoe.pop()]
                    sorted_player_hand += new_card
                    sorted_player_hand = hand_sorter(sorted_player_hand)
                    print(f"\nYour new card: {new_card[0]}")
                    print(f"{active_player} cards: {sorted_player_hand}\n"
                          f"{active_player} total: {get_hand_value(sorted_player_hand, player_list)}\n")
                    print("*" * 88)
                    print()
                    break
                else:
                    print("You do no have enough chips to double...")
                    continue
            # elif int(user_input) == 3:
            #     # ******************
            #     print("player handS", player_list[player]['hands'])
            #     for card in player_list[active_player]['hands']['hand 1']:
            #         print("card: ", card)
            #     split_hand(player_list, active_player)
            #     print(player_list[player]['hands'])
            else:
                print(f"{active_player} stays with {get_hand_value(sorted_player_hand, player_list)}\n")
                print("*" * 88)
                print()
                break
        else:
            print("Not a valid input...")

        if get_hand_value(sorted_player_hand, players) >= 22:
            print(f"You busted!\n")
            print("*" * 88)
            print()
            players[player].update({'bust': True})
        elif get_hand_value(sorted_player_hand, players) == 21:
            print("You have 21\n")
            print("*" * 88)
            print()
            players[player].update({'player_21': True})

    return sorted_player_hand


# dealer logic - hit on soft 17 or below hard 17.
def dealer_turn(player_list) -> None:
    dealer_finish = False
    dealer_hand = player_list['dealer']['hands']['hand 1']
    dealer_hand_value = get_hand_value(hand_sorter(dealer_hand), player_list)
    while not dealer_finish:
        print(f"Dealers cards are: {dealer_hand}\n"
              f"Hand Value: {dealer_hand_value}\n")
        if dealer_hand_value < 17 or player_list['dealer']['soft'] and dealer_hand_value == 17:
            print(f"The dealer will hit...")
            new_card = [shoe.pop()]
            dealer_hand += new_card
            hand_sorter(dealer_hand)
            dealer_hand_value = get_hand_value(dealer_hand, player_list)
            print(f"Dealers new card: {new_card[0]}")
        elif 17 <= dealer_hand_value <= 21:
            print(f"The dealer has {dealer_hand_value} and will stay.")
            dealer_finish = True
        else:
            print("The Dealer busted!")
            dealer_finish = True


# determines if the player will quit the game or continue.
def play_again() -> None:
    valid_input = ''
    while valid_input not in ['y', 'n']:
        user_input = input("\nWould you like to play another hand [y/n]? ").strip().lower()
        if user_input in ['y', 'n']:
            valid_input = user_input
        else:
            print("Not a valid input...")
    if valid_input not in ['', 'y']:
        quit()
    else:
        print("\n" * 8)
        print("*" * 88)
        print("\n" * 8)


# determines who won, handles bets and balances.
def end_of_round_results(player_list, active_player) -> None:
    dealer_hand_value = get_hand_value(player_list['dealer']['hands']['hand 1'], player_list)
    player_hand_value = get_hand_value(player_list[active_player]['hands']['hand 1'], player_list)

    print(f"\n{active_player} has {player_hand_value}\n"
          f"The dealer has {dealer_hand_value}")

    if 'bust' in player_list[active_player]:
        print(f"{active_player} busted...\n"
              f"You lost: {player_list[active_player]['bet']}\n"
              f"Your balance is: {player_list[active_player]['balance']}")
    elif 'bj' in player_list[active_player]:
        print(f"You got a Blackjack!\n"
              f"You won: {player_list[active_player]['bet'] * 3}\n"
              f"Your balance is: {player_list[active_player]['balance']}")
    elif player_hand_value == dealer_hand_value:
        player_list[active_player]['balance'] += player_list[active_player]['bet']
        print(f"It's a push.\n"
              f"Your balance is: {player_list[active_player]['balance']}")
    elif player_hand_value > dealer_hand_value or dealer_hand_value > 21:
        player_list[active_player]['balance'] += player_list[active_player]['bet'] * 2
        print(f"You won {player_list[active_player]['bet']}\n"
              f"Your balance is: {player_list[active_player]['balance']}")
    elif player_hand_value < dealer_hand_value:
        print(f"The Dealer won...\n"
              f"You lost: {player_list[active_player]['bet']}\n"
              f"Your balance is: {player_list[active_player]['balance']}")


# generating the shoe and the players.  This is kept out of the while loop to ensure the users, balances and shoe...
# remains the same for as long as the game is played
shoe = generate_shoe()
players = player_generator()
deposit()
# The game is played below as long as the user does not quit when asked.
while True:
    # gets bet amounts and deals the opening hand.
    get_bet_amount()
    starting_deal()
    print()

    # loops through all players except dealer to allow them their turns.
    for player in players:
        if player == 'dealer':
            continue

        # allows player to choose their plays and returns their sorted hand.
        player_hand_sorted = player_choices(players, player)

    # if bust, bj, bj_push or dealer_21 are false the dealer will play their turn for single player game
    if len(players) == 2:
        player1_conditions = ('bust' not in players['player 1'] and
                              'bj' not in players['player 1'] and
                              'bj_push' not in players['player 1'])
        dealer_condition = 'dealer_21' not in players['dealer']

        if player1_conditions and dealer_condition:
            dealer_turn(players)

    # for multiple players
    if len(players) > 2 and 'dealer_21' not in players['dealer']:
        dealer_turn(players)

    # end of game results.
    for player in players:
        if player == 'dealer':
            continue

        end_of_round_results(players, player)
        # resetting the players information and carrying over their balance at end of round.
        players[player] = {'balance': players[player]['balance'], 'bet': 0, 'hands': {}}
    # resetting the dealers information at the end of the round.
    players['dealer'] = {'hands': {}, 'soft': False}
    play_again()
