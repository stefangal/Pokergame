import random


class Deck:
    """Deck of cards and used/thrown away cards"""

    deck_cards = []
    used_cards = []

    def create_deck(self):

        for suit in ['Diamonds', 'Hearts', 'Clubs', 'Spades']:
            for nr in range(2, 11):
                self.deck_cards.append(str(nr)+' of '+str(suit))
            for x in ['J', 'Q', 'K', 'A']:
                self.deck_cards.append(str(x)+' of '+str(suit))
        self.deck_cards.append('_JOKER_')
        return self.deck_cards

    def shuffle_deck(self):
        random.shuffle(self.deck_cards)


class Table(Deck):
    on_table = []

    def deal_on_table(self, qty):
        for i in range(qty):
            deal_card = Deck.deck_cards.pop()
            self.on_table.append(deal_card)
        return self.on_table

    def show_table_cards(self):
        for cards in self.on_table:
            print("| ", cards, end=" |")
        print()

class Player(Deck):
    counter = 0
    def __init__(self, name):
        self.name = name
        self.dealed_card = []
        self.on_hand = []
        Player.counter += 1

    def take_card(self, qty):
        for _ in range(qty):
            taken = Deck.deck_cards.pop()
            self.on_hand.append(taken)

    def show_hand(self):
        print()
        print(f"{self.name}'s cards:\n")
        for cards in self.on_hand[0:2]:
            print(cards)
        print()

    def get_card(self, qty):
        for i in range(qty):
            self.dealed_card = Deck.deck_cards.pop()
            self.on_hand.append(self.dealed_card)
        return self.on_hand

    def return_card(self, returned):
        self.on_hand.pop(returned)
        Deck.used_cards.append(returned)
        print(f'>>> {self.name} thrown away 1 card.<<<')


class Winner(Player):
    """ Checking and assigning rank based on hand-ranking categories.
        The better the lowest rank. """
    classif = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    # https://en.wikipedia.org/wiki/List_of_poker_hands

    def __init__(self):
        #super().__init__(self, on_hand)
        self.rank = 0
        self. clif = 0

    def five_of_kind(self, player):
        """rank: 1, classification: 0-13"""
        uniqe = set()
        for nr in player.on_hand:
            uniqe.add(nr[0])
        if len(uniqe) == 2 and '_' in uniqe:
            self.rank = 1
            for nr in player.on_hand:
                if nr[0] in self.classif.keys():
                    self.clif = self.classif[nr[0]]-2
            return True
        return False

    def straight_flush(self, player):
        """rank: 2, classification: 5-14"""
        differences, flush, all_suits = [], [], []

        for nr in player.on_hand:
            if nr.split()[0] != '_JOKER_':
                flush.append(self.classif[nr.split()[0]])
                all_suits.append(nr.split()[2])
        if len(set(all_suits)) != 1:
            return False
        s_flush = sorted(flush)
        for idx in range(len(s_flush)-1):
            differences.append(s_flush[idx+1] - s_flush[idx])

        nr_of_differences = len(differences)
        if '_JOKER_' not in player.on_hand:
            if max(differences) == 1 and differences.count(1) == 4:
                # No Joker
                self.clif = max(s_flush)
                self.rank = 2
                return True
            return False
        elif '_JOKER_' in player.on_hand:
            if max(differences) == 1 and differences.count(1) == 3:
                # Joker at the end
                self.clif = max(s_flush)+1
                if self.clif == 14:
                    self.clif = 13
                self.rank = 2
                return True
            elif max(differences) == 2 and differences.count(2) == 1 and differences.count(1) == 2:
                # Joker in middle somewhere
                self.clif = max(s_flush)
                self.rank = 2
                return True
            return False
        return False

    def four_of_kind(self, player):
        """rank: 3, classification: 0-13"""
        uniqe = set()
        uniqelist, repeated, allofthem = [], [], []
        for nr in player.on_hand:
            uniqe.add(nr.split()[0])
            allofthem.append(nr.split()[0])

        for i in allofthem:
            if i not in uniqelist:
                uniqelist.append(i)
            else:
                repeated.append(i)

        for idx in range(len(repeated)-1):
            if repeated[idx] != repeated[idx+1]:
                return False
        if len(uniqe) == 2 and '_' not in uniqe and len(repeated) == 3:
            self.rank = 3

            if repeated[0] in self.classif.keys():
                self.clif = self.classif[repeated[0]]
            return True
        return False

    def fullhouse(self, player):
        """ rank: 4, classification: 9 - 47  """
        allofthem = []
        first_pair, second_pair, joker, trio = 0, 0, 0, 0

        #getting sorted values of cards
        for nr in player.on_hand:
            allofthem.append(nr.split()[0])
        sorted_allofthem = sorted(allofthem)

        if '_JOKER_' in sorted_allofthem:
            #with Joker
            joker = 1
            sorted_allofthem.pop((sorted_allofthem.index('_JOKER_')))

            if sorted_allofthem[0] == sorted_allofthem[1]:
                first_pair = self.classif[sorted_allofthem[0]]

                if sorted_allofthem[2] == sorted_allofthem[3]:
                    second_pair = self.classif[sorted_allofthem[2]]

                    self.rank = 4
                    self.clif = ((first_pair*2)+(second_pair*2)) // 2
            else:
                return False

        elif '_JOKER_' not in sorted_allofthem:
            #without Joker
            if sorted_allofthem[0] == sorted_allofthem[1] == sorted_allofthem[2] and sorted_allofthem[3] == sorted_allofthem[4]:
                trio = self.classif[sorted_allofthem[0]]
                first_pair = self.classif[sorted_allofthem[3]]

                self.rank = 4
                self.clif = (first_pair*2)+(trio*3) // 2
                return True
            elif sorted_allofthem[0] == sorted_allofthem[1] and sorted_allofthem[2] == sorted_allofthem[3] == sorted_allofthem[4]:
                first_pair = self.classif[sorted_allofthem[0]]
                trio = self.classif[sorted_allofthem[2]]
                self.rank = 4
                self.clif = (first_pair*2)+(trio*3) // 2

                return True
            else:
                return False


    def flush(self, player):
        """ rank: 5, classification: 20 - 60  """
        all_suits, allofthem = [], []
        # with Joker
        if '_JOKER_' in player.on_hand:
            joker = 1
            for nr in player.on_hand:
                if nr != '_JOKER_':
                    all_suits.append(nr.split()[2])
                    allofthem.append(self.classif[nr.split()[0]])

            if len(set(all_suits)) == 1:
                self.rank = 5
                self.clif = sum(allofthem)
                return True
            return False
        else:
            # no Joker
            for nr in player.on_hand:
                    all_suits.append(nr.split()[2])
                    allofthem.append(self.classif[nr.split()[0]])

            if len(set(all_suits)) == 1:
                self.rank = 5
                self.clif = sum(allofthem)
                return True
            return False

    def straight(self, player):
        """rank: 6, classification: 5-14"""
        differences, flush, all_suits = [], [], []

        for nr in player.on_hand:
            if nr.split()[0] != '_JOKER_':
                flush.append(self.classif[nr.split()[0]])

        s_flush = sorted(flush)
        for idx in range(len(s_flush)-1):
            differences.append(s_flush[idx+1] - s_flush[idx])

        nr_of_differences = len(differences)
        if '_JOKER_' not in player.on_hand:
            if max(differences) == 1 and differences.count(1) == 4:
                # No Joker
                self.clif = max(s_flush)
                self.rank = 6
                return True
            return False
        elif '_JOKER_' in player.on_hand:
            if max(differences) == 1 and differences.count(1) == 3:
                # Joker at the end
                self.clif = max(s_flush)+1
                if self.clif == 14:
                    self.clif = 13
                self.rank = 6
                return True
            elif max(differences) == 2 and differences.count(2) == 1 and differences.count(1) == 2:
                # Joker in middle somewhere
                self.clif = max(s_flush)
                self.rank = 6
                return True
            return False
        return False

    def three_of_kind(self, player):
        """rank: 7, classification: ?"""
        allofthem, trio = [], []
        for nr in player.on_hand:
            allofthem.append(nr.split()[0])

        for nr in allofthem:
            if allofthem.count(nr) == 3 and '_JOKER_' not in allofthem:
                trio.append(nr)
                self.rank = 7
                self.clif = self.classif[trio[0]]
                return True
            elif allofthem.count(nr) == 2 and '_JOKER_' in allofthem:
                trio.append(nr)
                self.rank = 7
                self.clif = self.classif[trio[0]]
                return True
        return False

    def two_pair(self, player):
        """rank: 8, classification: 5-27"""
        allofthem, pair = [], []

        for nr in player.on_hand:
            allofthem.append(nr.split()[0])

        for nr in allofthem:
            if allofthem.count(nr) == 2 and '_JOKER_' not in allofthem:
                pair.append(nr)
                allofthem.pop(allofthem.index(nr))
                allofthem.pop(allofthem.index(nr))
                if len(pair) == 2:
                    self.rank = 8
                    self.clif = sum((self.classif[nr] for nr in pair))
                    return True
            elif allofthem.count(nr) == 2 and '_JOKER_' in allofthem:
                    pair.append(nr)
                    allofthem.pop(allofthem.index(nr))
                    allofthem.pop(allofthem.index(nr))
                    if len(pair) == 1:
                        self.rank = 8
                        self.clif = self.classif[pair[0]] + max((self.classif[nr] for nr in allofthem if nr != '_JOKER_'))
                        return True
        return False

    def one_pair(self, player):
        """rank: 9, classification: 2-14"""
        allofthem, pair = [], []

        for nr in player.on_hand:
            allofthem.append(nr.split()[0])

        for nr in allofthem:
            if allofthem.count(nr) == 2 and '_JOKER_' not in allofthem:
                pair.append(nr)
                self.rank = 9
                self.clif = self.classif[nr]
                return True
            elif '_JOKER_' in allofthem:
                self.rank = 9
                self.clif = max((self.classif[nr] for nr in allofthem if nr != '_JOKER_'))
                return True
        return False

    def high_card(self, player):
        """rank: 10, classification: 2-14"""
        card_nr = []
        self.rank = 10
        if '_JOKER_' not in player.on_hand:
            for nr in player.on_hand:
                card_nr.append(self.classif[nr.split()[0]])
            self.clif = max(card_nr)
            return True
        # if Joker on hand, value = Ace
        else:
            self.clif = 14
            return True

