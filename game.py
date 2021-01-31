# create deck
def init_game():
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    names = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    return [Card(suit, name) for name in names for suit in suits]


# show all card as string
def card_message(cards):
    str_cards = [str(card) for card in cards]
    return ', '.join(str_cards)


# show who win the game
def show_result(player_cards, dealer_cards, bet, chips):
    player_points = [card.point for card in player_cards]
    dealer_points = [card.point for card in dealer_cards]
    player_points = sum(player_points) % 9
    dealer_points = sum(dealer_points) % 9
    if player_points > dealer_points:
        return f'You won!!!, received {bet} chips', chips+bet
    elif player_points == dealer_points:
        return f'You tied!!!, received nothing', chips
    else:
        return f'You lost!!!, lost your bet', chips-bet


# show total chips
def show_chips(chips):
    if chips >= 0:
        print(f'You got total {chips} chips')
    else:
        print(f'You lost total {-chips} chips')


class Card:
    def __init__(self, suit, name):
        self.suit = suit
        self.name = name
        if name == 'Ace':
            self.point = 1
        elif name == 'Jack' or name == 'Queen' or name == 'King' or name == '10':
            self.point = 0
        else:
            self.point = int(name)

    def __str__(self):
        return f'{self.suit}-{self.name}'
