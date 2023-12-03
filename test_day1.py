from puzzle_input import lines
import re

reg = re.compile(
    "(?=()(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|()(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine))"
)


def calibration_value(line):

    results = list(reg.finditer(line))

    def group_index(match):
        return [True if group else False for group in match.groups()].index(True)

    first = group_index(results[0]) % 10
    last = group_index(results[-1]) % 10

    #print(line, first)
    #print(line, last)

    return first * 10 + last


def test_numbers():
    assert calibration_value("1abc2") == 12
    assert calibration_value("pqr3stu8vwx") == 38
    assert calibration_value("a1b2c3d4e5f") == 15
    assert calibration_value("treb7uchet") == 77

    assert 29 == calibration_value("two1nine")
    assert 83 == calibration_value("eightwothree")
    assert 13 == calibration_value("abcone2threexyz")
    assert 24 == calibration_value("xtwone3four")
    assert 42 == calibration_value("4nineeightseven2")
    assert 14 == calibration_value("zoneight234")
    assert 76 == calibration_value("7pqrstsixteen")

    assert 18 == calibration_value("crvhlfone7xsqhkshpsix2nine73oneighttq")

    assert sum(calibration_value(line) for line in lines(1)) == 56017
