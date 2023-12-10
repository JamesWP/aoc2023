import collections
import puzzle_input
import heapq
from dataclasses import dataclass, field

class Cell:
    def __init__(self):
        self.left = None
        self.right = None
        self.up = None
        self.down = None

        self.c = None
        self.x = None
        self.y = None


def parse(input):
    cells = collections.defaultdict(Cell)

    def connect_left(x, y):
        cell = cells[(x,y)]
        cell.left = cells[(x-1,y)]
        # cells[(x-1,y)].right = cells[(x,y)]

    def connect_right(x, y):
        cell = cells[(x,y)]
        cell.right = cells[(x+1,y)]
        # cells[(x+1,y)].left = cells[(x,y)]

    def connect_up(x, y):
        cell = cells[(x,y)]
        cell.up = cells[(x,y-1)]
        # cells[(x,y-1)].down = cells[(x,y)]
    
    def connect_down(x, y):
        cell = cells[(x,y)]
        cell.down = cells[(x,y+1)]
        # cells[(x,y+1)].up = cells[(x,y)]

    for y,line in enumerate(input):
        for x,c in enumerate(line):
            cells[(x,y)].c = c
            cells[(x,y)].x = x
            cells[(x,y)].y = y

            if c == '.':
                continue
            if c == '-':
                connect_left(x, y)
                connect_right(x, y)
            elif c == '|':
                connect_up(x, y)
                connect_down(x, y)
            elif c == 'F':
                connect_down(x, y)
                connect_right(x, y)
            elif c == '7':
                connect_down(x, y)
                connect_left(x, y)
            elif c == 'L':
                connect_up(x, y)
                connect_right(x, y)
            elif c == 'J':
                connect_up(x, y)
                connect_left(x, y)
            elif c == 'S':
                start = (x,y)
            else:
                assert False, "Unknown cell type: %s" % c

    start_cell = cells[start]

    for (x,y) in [(start[0]-1, start[1]), (start[0]+1, start[1]), (start[0], start[1]-1), (start[0], start[1]+1)]:
        cell = cells[(x,y)]
        if cell.left == start_cell:
            connect_right(start[0], start[1])
        if cell.right == start_cell:
            connect_left(start[0], start[1])
        if cell.up == start_cell:
            connect_down(start[0], start[1])
        if cell.down == start_cell:
            connect_up(start[0], start[1])

    return cells, start_cell

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Cell=field(compare=False)

def dijkstra(start):
    dist = {start: 0}
    prev = {}

    queue = [PrioritizedItem(dist[start], start)]

    while queue:
        item = heapq.heappop(queue)
        u = item.item
        for v in [u.left, u.right, u.up, u.down]:
            if v is None:
                continue
            alt = dist[u] + 1
            if alt < dist.get(v, float('inf')):
                dist[v] = alt
                prev[v] = u
                heapq.heappush(queue, PrioritizedItem(dist[v], v))

    return dist, prev

def print_maze(cells, start, dist=None):
    min_x = min(x for x,y in cells)
    max_x = max(x for x,y in cells)
    min_y = min(y for x,y in cells)
    max_y = max(y for x,y in cells)

    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            c = cells[(x,y)]
            
            if dist is not None:
                if c in dist and dist[c] is not None:
                    print(dist[c]%10, end='')
                else:
                    print('.', end='')
            
            elif c is start:
                print('S', end='')
            elif c.right and c.down:
                print('F', end='')
            elif c.left and c.down:
                print('7', end='')
            elif c.up and c.right:
                print('L', end='')
            elif c.up and c.left:
                print('J', end='')
            elif c.left and c.right:
                print('-', end='')
            elif c.up and c.down:
                print('|', end='')
            else:
                print('.', end='')
        print()
    print("-------")

def count_inside(cells, dist):
    min_x = min(x for x,y in cells)
    max_x = max(x for x,y in cells)
    min_y = min(y for x,y in cells)
    max_y = max(y for x,y in cells)

    num_inside = 0
    for y in range(min_y, max_y+1):
        inside = False
        for x in range(min_x, max_x+1):
            c = cells[(x,y)]
            if c.up is not None and c in dist and dist[c] is not None:
                inside = not inside
                # print("U", end='')
            else:
                # print(".", end='')
                pass
            if (c.left is None and c.right is None and c.up is None and c.down is None) or (c not in dist or dist[c] is None):
                if inside:
                    num_inside += 1
                    # print('I', end='')
                else:
                    # print('.', end='')
                    pass
            else:
                # print('.', end='')
                pass
        assert not inside
        # print()
    # print("-------")

    return num_inside


def solve(input):
    cells, start = parse(input)
    dist, prev = dijkstra(start)
    # print_maze(cells, start, dist)
    path_length = max(d for d in dist.values() if d is not None)

    return path_length, count_inside(cells, dist)


def input():
    yield "....."
    yield ".S-7."
    yield ".|.|."
    yield ".L-J."
    yield "....."

def input2():
    yield "..F7."
    yield ".FJ|."
    yield "SJ.L7"
    yield "|F--J"
    yield "LJ..."

def input3():
    yield "7-F7-"
    yield ".FJ|7"
    yield "SJLL7"
    yield "|F--J"
    yield "LJ.LJ"

def larger_input():
    lines = """
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
""".strip().splitlines()
    for line in lines:
        yield line

def other_larger_input():
    lines = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
""".strip().splitlines()
    for line in lines:
        yield line


def test_solve():
    assert solve(input()) == (4, 1) 
    assert solve(input2()) == (8,1)
    assert solve(input2())[0] == solve(input3())[0]

    assert solve(larger_input())[1] == 8
    assert solve(other_larger_input())[1] == 10

    assert solve(puzzle_input.lines(10)) == (6870, 287)

def test_mini_test_solve():
    solve(input3())