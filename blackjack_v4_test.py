from blackjack_v4 import Blackjack
bj = Blackjack()

for player in bj.players:
    if player.name != 'dealer':
        bj.get_deposit(player)
        bj.get_bet_amount(player)
    bj.deal_cards(player)

for player in bj.players:
    print("im a player:", player)
    for hands in player.hands:
        bj.evaluate_hand(player)
        print("Im a card:", hands)
        print("Im the value of a card:", hands.value)

print("All players:", bj.players)
