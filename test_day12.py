import puzzle_input

def parse(lines):
    for line in lines:
        spring_condition, rle = line.split(" ") 
        yield [c for c in spring_condition], tuple(int(length) for length in rle.split(","))

def parse_complicated(lines):
    for spring_condition, rle in parse(lines):
        yield (spring_condition 
            + ["?"] + spring_condition
            + ["?"] + spring_condition
            + ["?"] + spring_condition
            + ["?"] + spring_condition,
            rle + rle + rle + rle + rle) 

def combinations(condition, rle):
    if "?" not in condition:
        return 1 if get_rle(condition)[0] == rle else 0

    maybe_rle, maybe = get_rle(condition)
    assert maybe 

    if rle[0:len(maybe_rle)] != maybe_rle:
        return 0

    first_unknown = condition.index("?")
    condition[first_unknown] = "#"
    good =  combinations(condition, rle)
    condition[first_unknown] = "."
    bad = combinations(condition, rle)
    condition[first_unknown] = "?"

    return good+bad
    
def test_combinations():
    assert 1 == combinations(list(c for c in "###"), (3,))
    assert 1 == combinations(list(c for c in "?##"), (2,))
    assert 1 == combinations(list(c for c in "?.#"), (1,1))
    assert 3 == combinations(list(c for c in "???"), (1,))
    assert 5 == combinations(list(c for c in "??????"), (2,))

def get_rle(combination):
    rle = []
    count = 0

    for c in combination:
        if c == '?':
            return tuple(rle), True

        if c == '#':
            count += 1
        elif c=='.' and count > 0:
            rle.append(count)
            count = 0

    if count > 0:
        rle.append(count)

    return tuple(rle), False

def test_get_rle():
    assert ((3,2,1), False) == get_rle("###.##.#")
    assert ((1,1,1,1,1,1,1), False) == get_rle(".#.#.#.#.#.#.#.")
    assert ((5,2), True) == get_rle("...#####...##...#?...#")

def solve(lines):
    possibilities = 0
    for spring_condition, rle in lines:
        possibilities += combinations(spring_condition, rle)
    return possibilities     

def test_solve():
    assert 21 == solve(parse(input()))
    assert 525152 == solve(parse_complicated(input()))
    assert 6981 == solve(parse(puzzle_input.lines(12)))
    
def input():
    return """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".strip().split("\n")