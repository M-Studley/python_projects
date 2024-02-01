from blackjack_v4 import Blackjack
bj = Blackjack()

print(bj.players)
for player in bj.players:
    if player.name != 'dealer':
        bj.get_deposit(player)
        bj.get_bet_amount(player)
        # TODO:
        #  deal the cards.
        #  .
print(bj.players)
