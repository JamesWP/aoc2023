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

  def find_number(x,y,m):
    if (x,y) not in m or not m[(x,y)].isnumeric():
      return 0

    while (x,y) in m and m[(x,y)].isnumeric():
      x-=1
    x+=1
    num = 0
     
    while (x,y) in m and m[(x,y)].isnumeric():
      num = num*10 + int(m[(x,y)])
      m[(x,y)] = '.'
      x+=1
    return num

  def remove(x,y,m):
    a = []
    a.append(find_number(x+1,y,m))
    a.append(find_number(x-1,y,m))
    a.append(find_number(x,y+1,m))
    a.append(find_number(x,y-1,m))
    a.append(find_number(x+1,y+1,m))
    a.append(find_number(x-1,y+1,m))
    a.append(find_number(x-1,y-1,m))
    a.append(find_number(x+1,y-1,m))
    return [v for v in a if v != 0]

  def print_schematic(m):
    for y in range(200):
      if (0,y) not in m:
        break

      for x in range(200):
        if (x,y) not in m:
          print()
          break
        print(m[(x,y)],end='')

  #print_schematic(m)

  total=0
  gear_count=0
  
  for (x,y) in m.keys():
    if m[(x,y)] not in not_symbols:
      numbers = remove(x,y,m)
      total += sum(numbers)
      if len(numbers) == 2 and m[(x,y)] == '*':
        a,b = numbers
        gear_count += a*b 
  #print()
  #print_schematic(m)

  return total, gear_count

def test_thing():
  a, b = parse() 

  #print(b)

  assert (4361,467835) == solve(a)
  assert (525119,76504829) == solve(b)
