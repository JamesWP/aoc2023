import puzzle_input

def parse(lines):
    data = {}

    seeds = lines[0].split(': ')[1].split(' ')
    seeds = [int(a) for a in seeds]
    # print(seeds)
    lines.pop(0)

    data['seeds']  = seeds


    while lines:
        while lines[0] != '':
            lines.pop(0)
        lines.pop(0)
    
        map_name = lines[0].split(' ')[0]
        # print(map_name)
        lines.pop(0)

        data[map_name] = []
        while lines and lines[0] != '':
            m = lines[0]
            lines.pop(0)
            destination_range_start, source_range_start, length = m.split(' ')
            source_range_start = int(source_range_start)
            destination_range_start = int(destination_range_start)
            length = int(length)
            # print(source_range_start, destination_range_start, length)
            data[map_name].append((source_range_start, destination_range_start, length))

    return data

def solve(data):
    maps = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']

    seeds = data['seeds']

    lowest_value = None

    for seed in seeds:
        value = seed
        
        for map_name in maps:
            map = data[map_name]
            # print(seed, map_name, value,end=' ')
            for source_range_start, destination_range_start, length in map:
                if value >= source_range_start and value < source_range_start + length:
                    offset = 0-source_range_start + destination_range_start
                    value = value + offset
                    # print()
                    # print("broke", source_range_start, destination_range_start, length, value)
                    # print("b(", source_range_start, offset, ")", end=' ')
                    break
            # print(value)

        lowest_value = value if lowest_value is None else min(lowest_value, value)  
        print(seed, value)
    return lowest_value


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
    data = parse(test_data.split('\n'))
    assert 35 == solve(data)

    assert 388071289 == solve(parse(list(puzzle_input.lines(5))))