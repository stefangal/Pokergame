import os, time
from Cards import *


winner = Winner()
table = Table()
deck = Deck()

def show_cards(player, deal_on_table):
    os.system('cls')
    table.deal_on_table(deal_on_table)
    print(f'>> Number of cards remained in the deck: {(len(deck.deck_cards))}pcs <<')
    print(f'>> Your remaining money is {bank} EUR. Your bet is now {bet}EUR')
    player1.show_hand()
    print('On table: ')
    table.show_table_cards()
    for card in Table.on_table:
        if card not in player.on_hand:
            player1.on_hand.append(card)
    print()
    print('Right now highest hand is: ', my_status(player1))
    print()

def my_status(player):
    if winner.five_of_kind(player):
        winner.five_of_kind(player)
        return('Five of kind')
    elif winner.straight_flush(player):
        winner.straight_flush(player)
        return('Straight flush')
    elif winner.four_of_kind(player):
        winner.four_of_kind(player)
        return ('Four of kind')
    elif winner.fullhouse(player):
        winner.fullhouse(player)
        return ('Fullhouse')
    elif winner.flush(player):
        winner.flush(player)
        return('Flush')
    elif winner.straight(player):
        winner.straight(player)
        return ('Straight')
    elif winner.three_of_kind(player):
        winner.three_of_kind(player)
        return('3 of kind')
    elif winner.two_pair(player):
        winner.two_pair(player)
        return('2 pairs')
    elif winner.one_pair(player):
        winner.one_pair(player)
        return('1 pair')
    elif winner.high_card(player):
        winner.high_card(player)
        return('High card')


os.system('cls')
name = input('Please insert your name >> ')
player1 = Player(name)
bank = 100
print(f'Welcom in poker {name} !')
print("Let's play...")
print(f'Initially you got {bank} EUR')
print('**********************************')
deck.create_deck()
deck.shuffle_deck()
print('>>> 1 deck of cards with 1 Joker is generated and shuffled')
time.sleep(1)
os.system('cls')
bet = int(input(f'Your bet >> '))
print(f"{name}... You get 2 cards now and your bet is {bet}EUR")
bank -= bet
print()
player1.get_card(2)
player1.show_hand()
print()
choice = ''
choice = input('Choose: call, raise or fold? >> ')
print()
if choice == 'call':
    show_cards(player1, 3) #showing cards of player 1 and table
elif choice == 'raise':
    raised = False
    while not raised:
        raising = int(input('Insert amount: '))
        if raising <= bet:
            bet += raising
            bank -= raising
            raised = True
        else:
            print("You don't have anough money")
elif choice == 'fold':
    print('You have finished the game. Bye!!!')
    choice == '0'

elif choice == '0':
    print('You have finished the game. Bye!!!')
    choice = '0'

while choice != '0' and len(table.on_table)+1 <= 5:
    choice = input('Choose: check or bet ? >> ')
    if choice == 'bet':
        raised = False
        while not raised:
            raising = int(input('Insert amount: '))
            if raising <= bank:
                bank -= raising
                bet = 100-bank
                raised = True
            else:
                print("You don't have anough money")
    elif choice == 'check':
        show_cards(player1, 1)

        print(player1.on_hand)

print(f'Your money is {bank}EUR')