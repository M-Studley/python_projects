from dataclasses import field, dataclass


# pass in the upper max range and the string you would like to ask the user.
def get_number_from_user(max_number, input_string):
    valid_input = 0
    while not valid_input:
        user_input = input(input_string).strip()
        if user_input.isnumeric() and int(user_input) in range(1, max_number + 1):
            valid_input = int(user_input)
        else:
            print("Not a valid amount...")
    return valid_input


@dataclass
class Card:
    name: str
    suit: str
    value: int
    face_up: bool = True


@dataclass
class Hand:
    cards: list[Card]
    value: int
    is_blackjack: bool = False
    is_bust: bool = False
    is_splittable = bool = False
    can_double: bool = False
    has_been_doubled = bool = False


@dataclass
class Shoe:
    cards: list[Card]


@dataclass
class Player:
    name: str
    bank: int = 0
    bet: int = 0
    hand: list[Hand] = field(default_factory=list)


@dataclass
class Round:
    players: list[Player] = field(default_factory=list)
