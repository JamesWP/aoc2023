import pytest
import puzzle_input


def parse(lines):
    data = {}

    seeds = lines[0].split(": ")[1].split(" ")
    seeds = [int(a) for a in seeds]
    # print(seeds)
    lines.pop(0)

    data["seeds"] = seeds

    while lines:
        while lines[0] != "":
            lines.pop(0)
        lines.pop(0)

        map_name = lines[0].split(" ")[0]
        # print(map_name)
        lines.pop(0)

        data[map_name] = []
        while lines and lines[0] != "":
            m = lines[0]
            lines.pop(0)
            destination_range_start, source_range_start, length = m.split(" ")
            source_range_start = int(source_range_start)
            destination_range_start = int(destination_range_start)
            length = int(length)
            data[map_name].append((destination_range_start, source_range_start, length))
        data[map_name].sort(key=lambda x: x[1])

    return data


def map_range(curent_range, map):
    range_start, range_length = curent_range

    while range_length > 0:
        found = False
        for destination_range_start, source_range_start, length in map:
            if source_range_start <= range_start and source_range_start + length > range_start:
                mapped_range_offset = range_start - source_range_start
                mapped_range_length = min(length - mapped_range_offset, range_length)
                range_offset = 0 - source_range_start + destination_range_start 

                yield (range_start + range_offset, mapped_range_length)

                range_length -= mapped_range_length
                range_start += mapped_range_length
                found = True
                break
        if not found:
            yield (range_start, range_length)
            range_length = 0



def map_ranges(curent_ranges, map):
    new_ranges = [range for curent_range in curent_ranges for range in map_range(curent_range, map)]

    return new_ranges

def test_map_ranges():
    map = [(49, 53, 8), (0, 11, 42), (42, 0, 7), (57, 7, 4)]
    curent_ranges = [(53, 1), (1000,10)]

    assert map_ranges(curent_ranges, map) == [(49, 1),(1000,10)]

def solve(data):
    seeds = data["seeds"]

    curent_ranges = [(seed, 1) for seed in seeds]

    for map_name in [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]:
        curent_ranges = map_ranges(curent_ranges, data[map_name])

    part1 = min(curent_ranges)[0]

    seeds = data["seeds"]
    curent_ranges = [seed_range for seed_range in zip(seeds[::2], seeds[1::2])]

    for map_name in [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
    ]:
        curent_ranges = map_ranges(curent_ranges, data[map_name])

    part2 = min(curent_ranges)[0]

    return part1, part2

def test_gogogo():
    test_data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
    data = parse(test_data.split("\n"))
    assert (35,46) == solve(data)

    data = parse(list(puzzle_input.lines(5)))
    assert (388071289, 84206669) == solve(data)
    assert 219974726 > solve(data)[1], "part 2 is too high"

