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

    for (x,y) in [(start[0]-1, start[1]), (start[0]+1, start[1]), (start[0], start[1]-1), (start[0], start[1]+1)]:
        cell = cells[(x,y)]
        start_cell = cells[start]
        if cell.left == cells[start]:
            start_cell.right = cell
        if cell.right == cells[start]:
            start_cell.left = cell
        if cell.up == cells[start]:
            start_cell.down = cell
        if cell.down == cells[start]:
            start_cell.up = cell

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

    for y in range(min_y-4, max_y+4):
        for x in range(min_x-4, max_x+4):
            c = cells[(x,y)]
            
            if dist is not None:
                if c in dist and dist[c] is not None:
                    print(dist[c], end='')
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

def solve(input):
    cells, start = parse(input)
    dist, prev = dijkstra(start)
    # print_maze(cells, start, dist)
    return max(d for d in dist.values() if d is not None)


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

def test_solve():
    assert solve(input()) == 4
    assert solve(input2()) == 8
    assert solve(input2()) == solve(input3())

    assert solve(puzzle_input.lines(10)) == 6870
