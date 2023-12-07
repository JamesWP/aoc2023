import collections
import puzzle_input

def calculate_rank(hand):
    hand_counts = collections.Counter([card for card in hand])
    hand_counts = sorted(hand_counts.values(), reverse=True)
    ranks = {
        (5,): 7,
        (4,1): 6,
        (3,2): 5,
        (3,1,1): 4,
        (2,2,1): 3,
        (2,1,1,1): 2,
        (1,1,1,1,1): 1,
    }
    return ranks[tuple(hand_counts)]

def get_hand_value(hand):
    """cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. The relative strength of each card follows this order, where A is the highest and 2 is the lowest."""
    values = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
    }
    return tuple([values[card] for card in hand])

def test_calculate_rank():
    assert calculate_rank("AAAAA") == 7
    assert calculate_rank("AA8AA") == 6
    assert calculate_rank("23332") == 5
    assert calculate_rank("TTT98") == 4
    assert calculate_rank("23432") == 3
    assert calculate_rank("A23A4") == 2
    assert calculate_rank("23456") == 1

def sort_key(hand):
    return (calculate_rank(hand), get_hand_value(hand))

def test_sort_key():
    assert sort_key("AA8AA") == (6, (14,14,8,14,14))

def input():
    yield ("32T3K", 765)
    yield ("T55J5", 684)
    yield ("KK677", 28)
    yield ("KTJJT", 220)
    yield ("QQQJA", 483)

def real_input():
    for line in puzzle_input.lines(7):
        hand, bid = line.split()
        yield hand, int(bid)

def solve(hands):
    sorted_hands = sorted(list(hands), key=lambda hand: sort_key(hand[0]))

    value = 0
    for i, (hand, bid) in enumerate(sorted_hands):
        value += (i +1) * bid
        print(hand, bid, i+1, bid * (i+1))
    return value

def test_solve():

    assert sort_key("QQQJA") > sort_key("T55J5")
    assert solve(input()) == 6440

    assert solve(real_input()) == 248396258