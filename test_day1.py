from puzzle_input import lines

def valueof(thing):
  thing = thing.replace("one", "1")
  thing = thing.replace("two", "2")
  thing = thing.replace("three", "3")
  thing = thing.replace("four", "4")
  thing = thing.replace("five", "5")
  thing = thing.replace("six", "6")
  thing = thing.replace("seven", "7")
  thing = thing.replace("eight", "8")
  thing = thing.replace("nine", "9")
  return int(thing)


def calibration_value(line):
  things = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  first = (9999, "")
  last = (-1, "")

  for thing in things:
    first = min(first, (line.find(thing), thing)) if thing in line else first
    last = max(last, (line.rfind(thing), thing)) if thing in line else last
  
  first = valueof(first[1])
  last = valueof(last[1])
  print(line, first) 
  print(line, last) 
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

  assert sum(calibration_value(line) for line in lines(1)) == 56017
