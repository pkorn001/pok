from game import init_game, card_message, show_result, show_chips
import random
player_cards = []
dealer_cards = []
chips = 0
deck = init_game()  # create decks
playing = False
try:
    command = input()
    if command == 'node start':
        playing = True
    else:
        # invalid input
        raise Exception()
    while (playing):
        # shuffle the deck
        random.shuffle(deck)
        # give two cards to player
        for i in range(1, 3):
            player_cards.append(deck[-i])
        # last pair for dealer
        for i in range(2):
            dealer_cards.append(deck[i])
        bet = int(input('Plase put your bet\n'))
        print(f'You got {card_message(player_cards)}')
        print(f'Dealer got {card_message(dealer_cards)}')
        # check who win this game
        result, chips = show_result(player_cards, dealer_cards, bet, chips)
        print(result)
        command = input('Wanna play more (Yes/No)?\n')
        if command.lower() == 'no':
            playing = False
        elif command.lower() == 'yes':
            player_cards = []
            dealer_cards = []
        else:
            # invalid input
            raise Exception()
except:
    print('Invalid Input')
finally:
    # show total chips before leaving
    show_chips(chips)