import random
from blackjack_object_funcs import *


class Blackjack:

    def __init__(self):
        self.card_names = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        self.suits = ['clubs', 'spades', 'hearts', 'diamonds']
        self._initial_player_count = self.ask_player_count()
        self.players = self.build_players()
        self.shoe = self.build_shoe()

    @staticmethod
    def get_deposit(player: Player):
        max_deposit = 100000
        deposit_quantity_query = f"{player.name.title()}: How much would you like to deposit (100 - {max_deposit})? "
        player.bank = get_number_from_user(max_deposit, deposit_quantity_query)

    @staticmethod
    def get_bet_amount(player: Player):
        max_bet = player.bank
        bet_quantity_query = f"{player.name.title()}: How much would you like to bet (100 - {max_bet})? "
        player.bet = get_number_from_user(max_bet, bet_quantity_query)
        player.bank -= player.bet

    @staticmethod
    def ask_player_count() -> int:
        max_players = 6
        player_quantity_query = f"Enter the amount of players from 1 - {max_players}: "
        return get_number_from_user(max_players, player_quantity_query)

# the goal of evaluate_hand is to change all the data inside class Hand.  then I can use the information inside the
    # hand Class to determine the next move.  take another card, dont take another, did you get a blackjack, bust?
    @staticmethod
    def evaluate_hand(player: Player):  # -> int
        print("I am the type for player.hands", type(player.hands))
        Hand.cards = player.hands
        print("I am the Hand.cards:", Hand.cards)
        print("I am the type of Hand.cards:", type(Hand.cards))
        Hand.value = sum([card.value for card in Hand.cards])
        print("Im the value of a hand:", Hand.value)
        if Hand.value > 21:
            Hand.is_bust = True
        elif Hand.value == 21:
            Hand.is_blackjack = True
        elif len(Hand.cards) == 2:
            print('there are two cards!!!')
            print(len(Hand.cards))

    def build_players(self) -> list[Player]:
        _players = []
        for i in range(1, self._initial_player_count + 1):
            _players.append(Player(name=f'player {i}'))
        _players.append(Player(name='dealer'))
        return _players

    def build_decks(self) -> list[Card]:
        deck = []
        for suit in self.suits:
            for card_name in self.card_names:
                card_value = 10
                if card_name.isnumeric():
                    card_value = int(card_name)
                elif card_name == 'ace':
                    card_value = 11
                deck.append(Card(name=card_name, suit=suit, value=card_value))
        return deck

    def build_shoe(self) -> list[Card]:
        max_deck_amount = 8
        deck_quantity_query = f"How many decks in the shoe (1 - {max_deck_amount})? "
        shoe = []
        shoe_deck_count = get_number_from_user(max_deck_amount, deck_quantity_query)

        for _ in range(shoe_deck_count):
            shoe.extend(self.build_decks())

        random.shuffle(shoe)
        return shoe

    def deal_cards(self, player: Player):
        player.hands = [self.shoe.pop(), self.shoe.pop()]
