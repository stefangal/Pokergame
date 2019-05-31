import random
import os
from Cards import *

winner = Winner()
counter = 0

counter += 1
table = Table()
player1 = Player('Stefan')
player2 = Player('Marianna')
deck = Deck()
deck.create_deck()
deck.shuffle_deck()
player1.get_card(5)
player2.get_card(5)
print(f'>> Number of cards remained in the deck: {(len(deck.deck_cards))}pcs <<')
print(f'>> Number of players:{Player.counter} <<')
print(f'>>>>>{counter} cycles<<<<<')
#player1.on_hand = ['_JOKER_', '9 of Spades', 'K of Spades', 'Q of Spades', 'J of Spades'] # straight flush with Joker
#player1.on_hand = ['9 of Spades', '10 of Spades', 'K of Spades', 'Q of Spades', 'J of Spades'] # straight flush
#player1.on_hand = ['2 of Hearts', '10 of Spades', '10 of Diamonds', '10 of Clubs', '10 of Clubs'] #4 of kind
#Player1.on_hand = ['2 of Hearts', '2 of Spades', '2 of Diamonds', '2 of Clubs', '_JOKER_'] #5 of kind
#player2.on_hand = ['J of Hearts', '3 of Hearts', '3 of Diamonds', '3 of Clubs', '3 of Hearts']
#player1.on_hand = ['J of Hearts', 'J of Diamonds', '3 of Diamonds', '3 of Clubs', '_JOKER_'] #fullhouse with Joker
#player1.on_hand = ['A of Hearts', 'J of Diamonds', 'A of Diamonds', 'K of Clubs', 'K of Spades'] #fullhouse no Joker
#player1.on_hand = ['_JOKER_', 'J of Diamonds', '2 of Diamonds', 'K of Diamonds', '9 of Diamonds'] #flush with Joker
#player1.on_hand = ['_JOKER_', '10 of Spades', 'K of Spades', 'Q of Spades', 'J of Spades'] # straight

player1.show_hand()
print()
player2.show_hand()

# print(winner.five_of_kind(player1), ' <-  5 of kind p1')
# print(winner.five_of_kind(player2), ' <-  5 of kind p2')
# print(winner.straight_flush(player1), ' <- Straight flush p1')
# print(winner.straight_flush(player2), ' <-  Straight flush p2')
# print(winner.four_of_kind(player1), ' <- 4 of kind p1')
# print(winner.four_of_kind(player2), ' <- 4 of kind p2')
# print(winner.flush(player1), '<- Flush p1')
# print(winner.straight(player1), '<- Straight p1')
print(winner.high_card(player1), '<- High card p1')

print()
print(f'Rank:{winner.rank} -- Classifiction:{winner.clif}')
