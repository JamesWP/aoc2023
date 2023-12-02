import puzzle_input


def do_it(lines):
    game_total = 0
    total_power = 0
    for line in lines:
        a, b = line.split(":")
        _, a = a.strip().split(" ")
        game = int(a)
        # print("game", game)
        turns = b.split(";")
        impossible = False
        min_r = min_g = min_b = 0
        for turn in turns:
            # print("", "")
            parts = turn.split(",")
            for part in parts:
                num, color = part.strip().split(" ")

                num = int(num)

                color = color.strip()
                r = g = b = 0
                if color[0] == "r":
                    r = num
                elif color[0] == "g":
                    g = num
                else:
                    b = num

                min_r = max(min_r, r)
                min_g = max(min_g, g)
                min_b = max(min_b, b)

                if r > 12 or g > 13 or b > 14:
                    impossible = True
                # print("", "turn", color, num)
        if not impossible:
            game_total += game
        # print("mins", min_r, min_g, min_b)
        # print("power", min_r * min_g * min_b)
        total_power += min_r * min_g * min_b
    # print("total", game_total)
    # print("total_power", total_power)
    return (game_total, total_power)


def test_parse():
    inp = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
    lines = inp.strip().split("\n")

    assert (8, 2286) == do_it(lines)
    assert (2256, 74229) ==do_it(puzzle_input.lines(2))
