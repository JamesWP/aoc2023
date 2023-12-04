from collections import defaultdict
import puzzle_input

def solve(data):
    total = 0
    total_instances = 0
    copies = defaultdict(lambda: 1)
    for line in data:
        card, numbers = line.split(":")
        _, card = card.strip().split(" ", 1)
        card = int(card)
        #print(card)
        winning_numbers, my_numbers = numbers.split("|")

        winning_numbers = [int(num) for num in winning_numbers.strip().split(" ") if num]
        my_numbers = [int(num) for num in my_numbers.strip().split(" ") if num]

        winning_numbers = set(winning_numbers)
        my_numbers = set(my_numbers)

        #print(winning_numbers.intersection(my_numbers))
        matching_numbers = winning_numbers.intersection(my_numbers)
        if matching_numbers:
            points = pow(2,len(matching_numbers)-1)
            total += points
        instances = copies[card]
        total_instances += instances
        wins = len(matching_numbers)
        #print(card, "instances", instances, "total cards", total_instances, "this card wins", wins)
        for x in range(wins):
            copies[card+1+x] += instances

    return total, total_instances


def test_4():
    inp = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    data = inp.split("\n")
    assert (13,30) == solve(data)

    data = puzzle_input.lines(4)
    assert (26346,8467762) == solve(data)