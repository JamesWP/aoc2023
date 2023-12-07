import math

def input():
    times = [7, 15, 30]
    distances = [9, 40, 200]
    onebigtime = 71530
    onebigdistance = 940200
    return times, distances, onebigtime, onebigdistance


def input_real():
    times = [48, 93, 84, 66]
    distances = [261, 1192, 1019, 1063]
    onebigtime = 48938466
    onebigdistance = 261119210191063
    return times, distances, onebigtime, onebigdistance

def evaluate(race_duration, button_duration):
    assert button_duration < race_duration

    speed = button_duration
    remaining_duration = race_duration - button_duration
    distance = speed * remaining_duration

    return distance

def test_evaluate():
    assert 12 == evaluate(7, 3)
    assert 6 == evaluate(7, 6)

def find_optimum(distance):
    half = (distance +1) //2

    button_press = distance - half
    return button_press

def test_find_optimum():
    assert find_optimum(7) == 3

def find_roots(duration, value):
    """ b = 1/2 (d +/- sqrt(d^2 - 4 v)) """

    discriminant = duration**2 - 4 * value

    assert discriminant >= 0

    b1 = 1/2 * (duration - math.sqrt(discriminant))
    b2 = 1/2 * (duration + math.sqrt(discriminant))

    #print("raw", b1, b2)
    return [math.ceil(b1), math.floor(b2)]

def num_ways(time, distance):
    button_press1, button_press2 = find_roots(time, distance+1)

    b1 = evaluate(time, button_press1)
    b2 = evaluate(time, button_press2)

    n_ways = 1+button_press2-button_press1
    #print(f"time: {time} distance_to_beat: {distance} button_press: {button_press1}={b1} or {button_press2}={b2}")

    return n_ways

def solve(input):
    prod = 1
    times, distances, onebigtime, onebigdistance = input
    for time, distance in zip(times, distances):
        prod *= num_ways(time, distance)

    big = num_ways(onebigtime, onebigdistance)

    return prod, big


def test_solve():
    assert (288, 71503) == solve(input())
    assert (1312850, 36749103) == solve(input_real())

        
"""
          .
        .
      .
......


         ........
.........

            .....

............


optimum:
duration - button = button

(duration - button) * button = value
(d-b)*b = v
d*b - b*b = v


b = 1/2 (d +/- sqrt(d^2 - 4 v))

"""
