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
Value is in pos1, and suit is in pos2.
"""
player1score = 0

#### HAND CHECKING ####
def is_royal_flush(hand):
    constraint1 = [card[1] for card in hand] == ['T','J','Q','K','A']
    constraint2 = is_flush(hand)
    if constraint1 and constraint2:
        return True
    return False

def is_straight_flush(hand):
    return is_straight(hand) and is_flush(hand)

def is_four_of_kind(hand):
    return max(get_card_counts(hand).values()) == 4

def is_full_house(hand):
    return len(get_card_counts(hand)) == 2

def is_flush(hand):
    return len(set([card[1] for card in hand])) == 1

def is_straight(hand):
    return ''.join([card[1] for card in hand]) in VALID_STRAIGHTS

def is_three_of_kind(hand):
    return max(get_card_counts(hand).values()) == 3

def is_two_pair(hand):
    return list(get_card_counts(hand).values()).count(2) == 2

def is_one_pair(hand): 
    return max(get_card_counts(hand).values()) == 2

def p1_wins_w_high_card(p1, p2):
    while max(p1) == max(p2):
        p1.remove(max(p1))
        p2.remove(max(p2))
    if max(p1) > max(p2):
        return True
    return False

#### UTILS ####
VALID_STRAIGHTS = ['12345', '23456', '34567', '45678', '56789',
    '6789T', '789TJ', '89TJQ', '9TJQK']

def get_hand_value(hand):
    if is_royal_flush(hand):
        24
    if is_straight_flush(hand):
        23 
    if is_four_of_kind(hand):
        22
    if is_full_house(hand):
        21
    if is_flush(hand):
        20
    if is_straight(hand):
        19
    if is_three_of_kind(hand):
        18
    if is_two_pair(hand):
        17
    if is_one_pair(hand):
        16
    if is_straight_flush(hand):
        15
    else:
        return get_high_card(hand)

def get_card_counts(hand):
    counts = dict()
    for card in hand:
        if card[0] in counts:
            counts[card[0]] += 1
        else:
            counts[card[0]] = 1
    return counts

def read_hands(line):
    cards = line[:-1].split(' ')
    return cards[:5], cards[5:]

def get_high_card(hand):
    values = [card[0] for card in hand]
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
    else:
        return int(max(values))

def hand_to_int(hand):
    h = [card[0] for card in hand]
    for n in range(len(h)): 
        if h[n] == 'T':
            h[n] = 10
        if h[n] == 'J':
            h[n] = 11
        if h[n] == 'Q':
            h[n] = 12
        if h[n] == 'K':
            h[n] = 13
        if h[n] == 'A':
            h[n] = 14
    return [int(card) for card in h]

f = open('pokertest.txt', 'r')

for line in f:
    hand = read_hands(line)
    p1 = hand[0]
    p2 = hand[1]
    if get_hand_value(p1) == get_hand_value(p2):
        if get_high_card(p1) != get_high_card(p2):
            if get_high_card(p1) > get_high_card(p2):
                player1score += 1
        else: 
            if p1_wins_w_high_card(hand_to_int(p1), hand_to_int(p2)):
                player1score += 1
                print(p1,p2)
    else:
        if get_hand_value(p1) > get_hand_value(p2):
            player1score += 1
            print(p1,p2)

print(player1score)
