import collections
import puzzle_input

def calculate_rank(hand, jokers):
    hand_counts = collections.Counter([card for card in hand])

    if jokers:
        num_jokers = hand_counts["J"]
        del hand_counts["J"]
    else:
        num_jokers = 0



    hand_counts = sorted(hand_counts.values(), reverse=True)

    if len(hand_counts) > 0:
        hand_counts[0] += num_jokers
    else:
        hand_counts = [5]

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

def get_hand_value(hand, jokers):
    """cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. The relative strength of each card follows this order, where A is the highest and 2 is the lowest."""
    values = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11 if not jokers else 1,
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
    assert calculate_rank("AAAAA", False) == 7
    assert calculate_rank("AA8AA", False) == 6
    assert calculate_rank("23332", False) == 5
    assert calculate_rank("TTT98", False) == 4
    assert calculate_rank("23432", False) == 3
    assert calculate_rank("A23A4", False) == 2
    assert calculate_rank("23456", False) == 1

    assert calculate_rank("KTJJT", True) == 6

def sort_key(hand, jokers):
    return (calculate_rank(hand, jokers), get_hand_value(hand, jokers))

def test_sort_key():
    assert sort_key("AA8AA", False) == (6, (14,14,8,14,14))

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

def solve(hands, jokers):
    sorted_hands = sorted(list(hands), key=lambda hand: sort_key(hand[0], jokers))

    value = 0
    for i, (hand, bid) in enumerate(sorted_hands):
        value += (i +1) * bid
        print(hand, bid, i+1, bid * (i+1))
    return value

def test_solve():

    #assert sort_key("QQQJA") > sort_key("T55J5")
    assert solve(input(), False) == 6440
    assert solve(input(), True) == 5905
    assert solve(real_input(), False) == 248396258
    assert solve(real_input(), True) == 246436046