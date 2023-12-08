import puzzle_input
import collections

r=1
l=0

class Node:
    def __init__(self, name):
        self.name = name
        self.edges = (None, None)
    
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

    return AAA, ZZZ, directions

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

    return AAA, ZZZ, directions

def input_real():
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

    return nodes["AAA"], nodes["ZZZ"], directions

def solve(start, goal, directions):
    steps = 0
    current = start
    while current is not goal:
        current = current.edges[directions[steps%len(directions)]]
        steps += 1
    return steps

def test_solve():
    start, goal, directions = input()
    assert solve(start, goal, directions) == 2

    start, goal, directions = input2()
    assert solve(start, goal, directions) == 6

    start, goal, directions = input_real()
    assert solve(start, goal, directions) == 18023