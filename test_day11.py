import bisect
import puzzle_input

def parse(lines):
    galactic_map = set()
    for y, line in enumerate(lines):
        for x, cell in enumerate(line):
            if cell == '#':
                galactic_map.add((x, y))
    return galactic_map

def expanding_space(galactic_map):
    min_x = min(x for x,y in galactic_map)
    max_x = max(x for x,y in galactic_map)
    min_y = min(y for x,y in galactic_map)
    max_y = max(y for x,y in galactic_map)


    expands_x = [x for x in range(min_x, max_x+1) if not any((x,y) in galactic_map for y in range(min_y, max_y+1))]
    expands_y = [y for y in range(min_y, max_y+1) if not any((x,y) in galactic_map for x in range(min_x, max_x+1))]

    return expands_x, expands_y

def distance(g1, g2, expands_x, expands_y, mult):
    def d(v1,v2,expands):
        v1,v2 = (min(v1,v2), max(v1,v2))

        left = bisect.bisect_left(expands, v1)
        right = bisect.bisect_right(expands, v2)

        expands = right-left
        dist = (v2-v1) - expands
        expands *= mult

        return expands + dist

    g1_x, g1_y = g1
    g2_x, g2_y = g2

    dx = d(g1_x, g2_x, expands_x)
    dy = d(g1_y, g2_y, expands_y)

    return dx+dy 

def input():
    yield from """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
    """.strip().splitlines()

def test_expanding_space():
    assert ([2,5,8],[3,7]) == expanding_space(parse(input()))

def solve(galactic_map, mult=2):
    ex, ey = expanding_space(galactic_map)
    total_distance = 0
    count = 0
    for g1 in galactic_map:
        for g2 in galactic_map:
            if g1 is g2:
                continue
            total_distance += distance(g1,g2,ex,ey, mult)
            count += 1

    return total_distance // 2


def test_distance():
    ex, ey = expanding_space(parse(input()))
    assert distance((1, 5), (4, 9), ex, ey, 2) == 9
    assert distance((3,0), (7, 8), ex, ey, 2) == 15

    assert 374 == solve(parse(input()))
    assert 1030 == solve(parse(input()), 10)

    assert 9521550 == solve(parse(puzzle_input.lines(11)))
    assert 298932923702 == solve(parse(puzzle_input.lines(11)), 1000000)
