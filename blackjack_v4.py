import random
from blackjack_object_funcs import *


class Blackjack:
    _card_names = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    _suits = ['clubs', 'spades', 'hearts', 'diamonds']

    def __init__(self):
        self._initial_player_count = self.ask_player_count()
        self.players = self.build_players()
        self.shoe = self.build_shoe()
        print(self.players)
        print(self.shoe)
        print(len(self.shoe))

    @staticmethod
    def get_deposit(player: Player):
        max_deposit = 100000
        deposit_quantity_query = f"How much would you like to add to your bank (100 - {max_deposit})? "
        player.bank = get_number_from_user(max_deposit, deposit_quantity_query)

    @staticmethod
    def get_bet_amount(player: Player):
        max_bet = player.bank
        bet_quantity_query = f"How much would you like to bet (100 - {max_bet})? "
        player.bet = get_number_from_user(max_bet, bet_quantity_query)

    @staticmethod
    def ask_player_count():
        max_players = 6
        player_quantity_query = f"Enter the amount of players from 1 - {max_players}: "
        return get_number_from_user(max_players, player_quantity_query)

    def build_players(self):
        _players = []
        for i in range(1, self._initial_player_count + 1):
            _players.append(Player(name=f'player {i}'))
        _players.append(Player(name='dealer'))
        return _players

    def build_decks(self):
        deck = []
        for suit in self._suits:
            for card_name in self._card_names:
                card_value = 10
                if card_name.isnumeric():
                    card_value = int(card_name)
                elif card_name == 'ace':
                    card_value = 11
                deck.append(Card(name=card_name, suit=suit, value=card_value))
        return deck

    def build_shoe(self):
        max_deck_amount = 8
        deck_quantity_query = f"How many decks in the shoe (1 - {max_deck_amount})? "
        shoe = []
        shoe_deck_count = get_number_from_user(max_deck_amount, deck_quantity_query)

        for _ in range(shoe_deck_count):
            shoe.extend(self.build_decks())

        random.shuffle(shoe)
        return shoe
