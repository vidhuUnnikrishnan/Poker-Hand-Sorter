# Poker Hand Sorter Program

# Author : Vidhu Krishnan Unnikrishnan
# Email id : vdhukrishnan@gmail.com

from collections import defaultdict
import sys

CARD_FACE = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


# Function to convert card face to numeric
def to_number(card):
    # Return number values for 1-9
    if card.isnumeric():
        return int(card)

    # Return numeric for T-A
    else:
        return CARD_FACE[card]


# Function to check Straight Flush or Royal Flush
def check_flush_type(player):

    if check_flush(player) and check_straight(player):
        value = sorted([to_number(card[0]) for card in player])

        # Royal Flush
        if value[0] == 10:
            return 10

        # Straight Flush
        else:
            return 9

    else:
        return 0


# Function for checking four of a kind, full house
def check_full_house_4kind(player):
    value = [card[0] for card in player]
    value_count = defaultdict(lambda: 0)

    for val in value:
        value_count[val] += 1

    # Four of a kind
    if sorted(value_count.values()) == [1, 4]:
        return 8

    # Full house
    elif sorted(value_count.values()) == [2, 3]:
        return 7

    else:
        return 0


# Function to check flush
def check_flush(player):
    suit = [card[1] for card in player]

    if len(set(suit)) == 1:
        return True

    else:
        return False


# Function to check straight
def check_straight(player):
    numbered_card = []
    value = [card[0] for card in player]
    value_count = defaultdict(lambda: 0)

    for val in value:
        value_count[val] += 1
        numbered_card.append(to_number(val))

    value_range = max(numbered_card) - min(numbered_card)

    if len(set(value_count.values())) == 1 and value_range == 4:
        return True

    else:
        return False


# Function for checking three of a kind, 2 pairs or a pair
def check_pairs_3_kind(player):
    value = [card[0] for card in player]
    value_count = defaultdict(lambda: 0)

    for val in value:
        value_count[val] += 1

    # Three of a kind
    if set(value_count.values()) == {3, 1}:
        return 4

    # 2 Pairs
    elif sorted(value_count.values()) == [1, 2, 2]:
        return 3

    # Pair
    elif 2 in value_count.values():
        return 2

    else:
        return 0


# Function to check who won when ranks are same
def check_hands(p1, p2):
    p1_values = sorted([to_number(card[0]) for card in p1])
    p2_values = sorted([to_number(card[0]) for card in p2])

    # print(p1_values, p2_values)
    for i in range(len(p1_values) - 1, -1, -1):
        if p1_values[i] == p2_values[i]:
            # print(i)
            pass
        else:
            if p1_values[i] > p2_values[i]:
                return True
            else:
                # print(p1_values, p2_values)
                return False


def check_rank(player):

    flush_type = check_flush_type(player)
    if flush_type != 0:
        return flush_type

    full_or_kind = check_full_house_4kind(player)

    if full_or_kind != 0:
        return full_or_kind

    if check_flush(player):
        return 6

    if check_straight(player):
        return 5

    pair_or_kind = check_pairs_3_kind(player)

    if pair_or_kind != 0:
        return pair_or_kind

    return 1


def main():

    # Initialise counter for hands won
    player_one = 0
    player_two = 0

    # Read from STDIN
    for hands in sys.stdin:

        hands = hands.strip().split(' ')
        p1_rank = check_rank(hands[:5])
        p2_rank = check_rank(hands[-5:])

        if p1_rank == p2_rank:

            if check_hands(hands[:5], hands[-5:]):
                player_one += 1

            else:
                player_two += 1

        elif p1_rank > p2_rank:
            player_one += 1

        else:
            player_two += 1

    print("Player 1: " + str(player_one) + " hands")
    print("Player 2: " + str(player_two) + " hands")


if __name__ == "__main__":
    main()
