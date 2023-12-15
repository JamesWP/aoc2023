import puzzle_input

def input():
    for i in """
#.##..##.
..#.##.#. 
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
""".strip().split("\n\n"):
        yield i.split("\n")

def bad_input():
    return """
#..##.###..
.##....#.#.
......##.#.
#..#.###.##
######.....
######.....
#..#.######""".strip().split("\n")

def mirror(center, width):    
    smaller = list(range(0, center+1))
    larger = list(range(center+1, width))

    smaller.reverse()

    return list(zip(smaller, larger))

def mirrors(width):
    for center in range(0, width-1):
        yield center+1, mirror(center, width)

x= 0
def solve(lines):
    width = len(lines[0])
    coords = { (x,y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "#" }

    height = len(lines)
    coords_inverted = { (y,x) for x,y in coords }

    def is_mirror(line_no, mirror, coords, length):
        # print("is_mirror", line_no, mirror, length)
        
        for y in range(length):
            for coorda, coordb in mirror:
                left = (coorda,y) in coords
                right = (coordb,y) in coords
                if left != right:
                    # print("nope")
                    return False
        # print("yep")
        return True
    

    vertical_lines = sum(vertical_line for vertical_line, mirror in mirrors(width) if is_mirror(vertical_line, mirror, coords, height))
    horizontal_lines = sum(horizontal_line for horizontal_line, mirror in mirrors(height) if is_mirror(horizontal_line, mirror, coords_inverted, width))
    

    if vertical_lines > 0:
        assert horizontal_lines == 0, "vertical_lines: %s, horizontal_lines: %s" % (vertical_lines, horizontal_lines)

    if horizontal_lines > 0:
        assert vertical_lines == 0, "vertical_lines: %s, horizontal_lines: %s" % (vertical_lines, horizontal_lines)

    global x
    x+=1
    # print("v",x,vertical_lines)
    # print("h",x,horizontal_lines)

    return vertical_lines + 100 * horizontal_lines

def test_solve():
    # assert 405 == sum(solve(lines) for lines in input())
    assert 2 == solve(bad_input())
    assert 34918 == sum(solve(lines) for lines in puzzle_input.blocks_of_lines(13))