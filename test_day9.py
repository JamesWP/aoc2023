import puzzle_input

def get_pattern(sequence):
    if all(value == 0 for value in sequence):
        return []
    diff = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    pattern = get_pattern(diff) + [sequence[-1]]
    return pattern
    
def get_next_value(pattern):
    if len(pattern) == 0:
        return 0
    return pattern[-1] + get_next_value(pattern[:-1])

def test_get_pattern():
    assert get_pattern((0,3,6,9,12,15)) == [3,15]
    assert get_pattern((1,3,6,10,15,21)) == [1,6,21]
    assert get_pattern((10,13,16,21,30,45)) == [2,6,15,45]

def test_get_next_value():
    assert get_next_value((3,15)) == 18
    assert get_next_value((1,6,21)) == 28
    assert get_next_value((2,6,15,45)) == 68

def parse(lines):
    return [tuple(map(int, line.split())) for line in lines]

def input():
    yield "0 3 6 9 12 15"
    yield "1 3 6 10 15 21"
    yield "10 13 16 21 30 45"

def solve(input, part2=False):
    def values():
        for sequence in input:
            if part2:
                sequence = sequence[::-1]
            pattern = get_pattern(sequence)
            yield get_next_value(pattern)

    return sum(values())

def test_solve():
    assert solve(parse(input())) == 114
    assert solve(parse(input()), True) == 2

    assert solve(parse(puzzle_input.lines(9))) == 1972648895
    assert solve(parse(puzzle_input.lines(9)), True) == 919