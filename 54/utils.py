"""
High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

Hands are in format 8C TS KC 9H 4S 7D 2S 5D 3S AC.
Player 1's hand is 8C TS KC 9H 4S. 
"""
VALUE = 0
SUIT = 1
VALID_STRAIGHTS = ['12345', '23456', '34567', '45678', '56789', '6789T', '789TJ', '89TJQ', '9TJQK']

def parse_hand(line):
    """
    Returns a tuple containing tuples of each player's hand
    """
    cards = line.split(' ')
    return tuple(cards[:5]), tuple(cards[5:])
        
class Hand:
    """docstring for hand"""
    def __init__(self, cards):
        self.cards = cards
        self.rank, self.metarank = self.getrank(cards)
        self.highcard = self.get_high_card(cards)
    
    def __lt__(self, other):
        if self.rank == other.rank:
            if self.metarank == other.metarank:
                return self.highcard < other.highcard
            return self.metarank < other.metarank
        return self.rank < other.rank
    
    def __gt__(self, other):
        return not self.__lt__(other)
    
    def get_high_card(self, hand):
        values = [card[VALUE] for card in hand]
        if 'A' in values:
            return 14
        elif 'K' in values:
            return 13
        elif 'Q' in values:
            return 12
        elif 'J' in values:
            return 11
        elif 'T' in values:
            return 10
        return int(max(values))
    
    def getrank(self, hand):
        if self.is_royal_flush(hand):
            return (24, 'A')
        elif self.is_straight_flush(hand):
            return (23, max(hand, key=lambda x: x[VALUE]))
        elif self.is_four_of_kind(hand):
            d = self.get_card_counts(hand)
            return (22, self.cardtoint(max(d, key=lambda x: d[x])))
        elif self.is_full_house(hand):
            d = self.get_card_counts(hand)
            return (21, self.cardtoint(max(d, key=lambda x: d[x])))
        elif self.is_flush(hand):
            return (20, self.get_high_card(hand))
        elif self.is_straight(hand):
            return (19, None)
        elif self.is_three_of_kind(hand):
            d = self.get_card_counts(hand)
            return (18, self.cardtoint(max(d, key=lambda x: d[x])))
        elif self.is_two_pair(hand):
            d = self.get_card_counts(hand)
            return (17, self.cardtoint(max(d, key=lambda x: d[x])))
        elif self.is_one_pair(hand):
            d = self.get_card_counts(hand)
            return (16, self.cardtoint(max(d, key=lambda x: d[x])))
        elif self.is_straight_flush(hand):
            return (15, self.get_high_card(hand))
        return (self.get_high_card(hand), self.get_high_card(hand))
        
    def is_royal_flush(self, hand):
        if self.suit_constraint(hand) and self.is_flush(hand):
            return True
        return False

    def suit_constraint(self, hand):
        return [card[SUIT] for card in hand] == ['T','J','Q','K','A']

    def is_straight_flush(self, hand):
        return self.is_straight(hand) and self.is_flush(hand)

    def is_four_of_kind(self, hand):
        return max(self.get_card_counts(hand).values()) == 4

    def is_full_house(self, hand):
        return len(self.get_card_counts(hand)) == 2

    def is_flush(self, hand):
        return len(set([card[1] for card in hand])) == 1

    def is_straight(self, hand):
        return ''.join([card[1] for card in hand]) in VALID_STRAIGHTS

    def is_three_of_kind(self, hand):
        return max(self.get_card_counts(hand).values()) == 3

    def is_two_pair(self, hand):
        return list(self.get_card_counts(hand).values()).count(2) == 2

    def is_one_pair(self, hand): 
        return max(self.get_card_counts(hand).values()) == 2

    def get_card_counts(self, hand):
        counts = dict()
        for card in hand:
            if card[VALUE] in counts:
                counts[card[VALUE]] += 1
            else:
                counts[card[VALUE]] = 1
        return counts

    def cardtoint(self, card):
        if card == 'T':
            return 10
        if card == 'J':
            return 11
        if card == 'Q':
            return 12
        if card == 'K':
            return 13
        if card == 'A':
            return 14
        return int(card)
