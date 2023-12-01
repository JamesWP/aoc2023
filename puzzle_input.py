def lines(day):
  with open(f"input/day{day}.txt", "r") as inp:
    for line in inp:
      yield line
