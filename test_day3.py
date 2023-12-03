from puzzle_input import lines

def parse():
  len1 = list(lines(3)).index('')
  test = list(lines(3))[:len1]
  real = list(lines(3))[len1+1:]

  return test, real

def solve(inp):
  m = {}
  for y, line in enumerate(inp):
    for x, cell in enumerate(line):
      if cell == '\n':
        break
      m[(x,y)] = cell

  not_symbols = list("0123456789.")
  numbers = list("0123456789")  

  def remove(x,y,m):
    if (x,y) not in m:
      return
    if m[(x,y)] == '.':
      return

    m[(x,y)] = '.'
    remove(x+1,y,m)
    remove(x-1,y,m)
    remove(x,y+1,m)
    remove(x,y-1,m)
    remove(x+1,y+1,m)
    remove(x-1,y+1,m)
    remove(x-1,y-1,m)
    remove(x+1,y-1,m) 

  def do_total(m):
    total = 0
    for y in range(200):
      if (0,y) not in m:
        break

      num = 0
      for x in range(200):
        if (x,y) not in m:
          # print()
          # print(num)
          total += num
          num = 0
          break
        if m[(x,y)].isnumeric():
          num *= 10
          num += int(m[(x,y)])
        else:
          # print(num)
          total += num
          num  = 0

        # print(m[(x,y)],end='')
    #print(total) 
    return total

  a = do_total(m)
  for (x,y) in m.keys():
    if m[(x,y)] not in not_symbols:
      remove(x,y,m)
  b = do_total(m)

  print(a-b)
  return a-b

def test_thing():
  a, b = parse() 

  #print(b)

  assert 4361 == solve(a)
  assert 525119 == solve(b)
