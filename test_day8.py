import puzzle_input
import collections
import math

r=1
l=0

class Node:
    def __init__(self, name):
        self.name = name
        self.edges = (None, None)
    def __hash__(self) -> int:
        return hash(self.name)
    def __eq__(self, __value: object) -> bool:
        return self is __value
    
def input():
    directions = [1,0]

    AAA = Node("AAA")
    BBB = Node("BBB")
    CCC = Node("CCC")
    DDD = Node("DDD")
    EEE = Node("EEE")
    GGG = Node("GGG")
    ZZZ = Node("ZZZ")

    AAA.edges = (BBB, CCC)
    BBB.edges = (DDD, EEE)
    CCC.edges = (ZZZ, GGG)
    DDD.edges = (DDD, DDD)
    EEE.edges = (EEE, EEE)
    GGG.edges = (GGG, GGG)
    ZZZ.edges = (ZZZ, ZZZ)

    return [AAA], [ZZZ], directions

def input2():
    """
    LLR

    AAA = (BBB, BBB)
    BBB = (AAA, ZZZ)
    ZZZ = (ZZZ, ZZZ)
    """
    directions = [0,0,1]

    AAA = Node("AAA")
    BBB = Node("BBB")
    ZZZ = Node("ZZZ")

    AAA.edges = (BBB, BBB)
    BBB.edges = (AAA, ZZZ)
    ZZZ.edges = (ZZZ, ZZZ)

    return [AAA], [ZZZ], directions

def input_real(part1 = True):
    lines = puzzle_input.lines(8)

    directions = next(lines)

    directions = [ 0 if x == "L" else 1 for x in directions]

    next(lines)

    nodes = {}

    def get_node(name):
        if name not in nodes:
            nodes[name] = Node(name)
        return nodes[name]

    for line in lines:
        node_name, edges = line.split(" = ")

        node_name = get_node(node_name)
        
        left_node, right_node = edges[1:-1].split(", ")

        left_node = get_node(left_node)
        right_node = get_node(right_node)

        node_name.edges = (left_node, right_node)

    if part1:
        return [nodes["AAA"]], [nodes["ZZZ"]], directions
    else:
        return [ n for n in nodes.values() if n.name.endswith("A")], [ n for n in nodes.values() if n.name.endswith("Z")], directions

def input3():
    """
    LR

    11A = (11B, XXX)
    11B = (XXX, 11Z)
    11Z = (11B, XXX)
    22A = (22B, XXX)
    22B = (22C, 22C)
    22C = (22Z, 22Z)
    22Z = (22B, 22B)
    XXX = (XXX, XXX)
    """
    directions = [0,1]

    _11A = Node("11A")
    _11B = Node("11B")
    _11Z = Node("11Z")
    _22A = Node("22A")
    _22B = Node("22B")
    _22C = Node("22C")
    _22Z = Node("22Z")
    XXX = Node("XXX")

    _11A.edges = (_11B, XXX)
    _11B.edges = (XXX, _11Z)
    _11Z.edges = (_11B, XXX)
    _22A.edges = (_22B, XXX)
    _22B.edges = (_22C, _22C)
    _22C.edges = (_22Z, _22Z)
    _22Z.edges = (_22B, _22B)
    XXX.edges = (XXX, XXX)

    return [_11A, _22A], [_11Z, _22Z], directions


def get_length_loop(start, goals, directions):
    goals = set(goals)

    steps = 0
    current = start
    while current not in goals:
        current = current.edges[directions[steps%len(directions)]]
        steps += 1
    return steps

def lcm(a,b):
    return abs(a*b) // math.gcd(a, b)

def solve(starts, goals, directions):
    least_steps = 1
    for start in starts:
        length = get_length_loop(start, goals, directions)
        least_steps = lcm(least_steps, length)

    return least_steps

def test_solve():
    start, goal, directions = input()
    assert solve(start, goal, directions) == 2

    start, goal, directions = input2()
    assert solve(start, goal, directions) == 6

    start, goal, directions = input_real()
    assert solve(start, goal, directions) == 18023

    start, goal, directions = input3()
    assert solve(start, goal, directions) == 6

    start, goal, directions = input_real(False)
    assert solve(start, goal, directions) == 14449445933179
