import random
import time

players = {'Player': [],
           'Dealer': []}


def create_shuffled_deck():     # Yes the shuffle is pointless for how I am choosing the cards.  Will change do
    card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['clubs', 'spades', 'hearts', 'diamonds']
    deck = [[f"{value.title()} of {suit.title()}"] for suit in suits for value in card_values]
    random.shuffle(deck)
    return deck


def starting_deal(cards):
    for player in list(players.keys()):
        while len(players[player]) < 2:
            new_card = random.choice(cards.pop())
            if new_card[0] == 'A' and players[player] == players['Player']:
                players[player].append(new_card)
            else:
                players[player].insert(0, new_card)
    return players


def hand_value(hand):
    value = 0
    soft = False
    for card in hand:
        split_card = card.split(" ")
        if split_card[0].isnumeric():
            value += int(split_card[0])
        elif split_card[0] in ['Jack', 'Queen', 'King']:
            value += 10
        elif split_card[0] == 'Ace':
            if value > 10:
                value += 1
            else:
                value += 11
                soft = True
    return value, soft


def hand_sorter(hand, card):
    last = hand.index(card)
    hand[-1], hand[last] = hand[last], hand[-1]
    return hand


def load_money():
    bank = 0
    while bank < 100:
        deposit_input = input("How much money would you like to deposit [100 minimum]? ").strip()
        if deposit_input.isnumeric() and int(deposit_input) >= 100:
            bank += int(deposit_input)
            break
        else:
            print("Not a valid input...")
    return bank


def main():
    player_bust = False
    dealer_finished = False
    bj = False
    dealer_bust = False
    sum_twentyone = False
    push = False
    stay = False
    player_bank = 0
    play_again = ''

    while play_again in ['', 'y']:
        deck = create_shuffled_deck()
        starting_deal(deck)
        player_hand = players['Player']
        dealer_hand = players['Dealer']
        player_hand_value, toss = hand_value(player_hand)
        dealer_hand_value, soft_svntn = hand_value(dealer_hand)
        print("Dealer Hand:", players['Dealer'])        # Testing

        if player_bank < 100:
            player_bank = load_money()

        print(f"Bank Total: {player_bank}")
        print(f"The dealers face up card is: {players['Dealer'][1]}")
        print(f"Your cards are: {player_hand}\n"
              f"with a total value of {player_hand_value}")

        if dealer_hand_value == 21 and player_hand_value != 21:
            print(f"Dealers got 21!  You lose...")
            dealer_finished = True
        elif dealer_hand_value == 21 and player_hand_value == 21:
            print("It's a push.")
            push = True
        elif len(player_hand) == 2 and player_hand_value == 21:
            print("Black Jack!!!")
            bj = True

        while not stay and not sum_twentyone and not player_bust and not dealer_finished and not push and not bj:
            player_input = input("Would you like to stay[0] or hit[1]? ").strip().lower()
            if player_input in ['0', '1']:
                hit_stay = player_input
                if hit_stay == '1':
                    new_player_card = random.choice(deck.pop())
                    if new_player_card[0] == 'A':
                        players['Player'].append(new_player_card)
                    else:
                        players['Player'].insert(0, new_player_card)
                    print(f"Your new card is: {new_player_card}")
                else:
                    print("\nYou stay...\n")
                    stay = True
            else:
                print("Not a valid input...")

            player_hand_value, toss = hand_value(player_hand)

            print(f"Your cards are: {player_hand}\n"
                  f"with a total value of {player_hand_value}")

            if player_hand_value == 21:
                print("You hit 21...")
                sum_twentyone = True

            if player_hand_value > 21:
                print("You went over 21, you busted!!!")
                player_bust = True

        print("\n")

        for card in dealer_hand:
            if card[0] == 'A':
                ace_card = card
                hand_sorter(players['Dealer'], ace_card)

        while not dealer_finished and not dealer_bust and not player_bust and not bj:

            dealer_hand_value, soft_svntn = hand_value(dealer_hand)

            print(f"Dealers cards are: {dealer_hand}\n"
                  f"with the value of: {dealer_hand_value}")

            if 17 <= dealer_hand_value <= 21:
                dealer_finished = True
            if dealer_hand_value > 21:
                print("Dealer Busted!")
                dealer_bust = True
            if dealer_hand_value > player_hand_value:
                break

            if dealer_hand_value < 17 or (soft_svntn and dealer_hand_value == 17) or not dealer_finished:
                print("The dealer will take another card...")
                new_dealer_card = random.choice(deck.pop())
                if new_dealer_card[0] == 'A':
                    players['Dealer'].append(new_dealer_card)
                else:
                    players['Dealer'].insert(0, new_dealer_card)
                print(f"Dealers new card is: {new_dealer_card}\n")

        if not dealer_bust and not player_bust and push and dealer_finished:
            if player_hand_value > dealer_hand_value:
                print("You won this hand!")
            elif player_hand_value < dealer_hand_value and not dealer_bust:
                print("The dealer won this hand!")
            else:
                print("It's a push!")
        elif player_bust:
            print("You lost this many chips.  you have this many left.  ready to continue?")
        else:
            print("You won this many chips.  you now have this many. ready to continue?")

        while play_again not in ['y', 'n']:
            play_again = input("Would you like to play again [Y/N]? ").strip().lower()
            if play_again == 'y':
                players['Dealer'].clear()
                players['Player'].clear()
            else:
                print("Thank you for playing!")
                time.sleep(3)
                quit()


if __name__ == "__main__":
    main()

# TODO
#  1. include player bank in the players dict. refactor the code to allow for this.
#  2. add in the bet size for each hand player_bet = input("How much would you like to bet? ) check if balance is good.
#  3. add in checks for the player bank total and +- bet amounts when player win/loses.
#  4. add in appropriate pay outs for blackjack, double, split(OMG).
#  5. recursive main() while the player has money or until the player hits Q.
