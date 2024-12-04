from common import parse_input_lines

def parse_input(input_lines: list[str]):
  return input_lines

def solve(input) -> int:
  xmas_count = 0

  def check_m_left(x, y):
    try:
      if input[y-1][x-1] == "M" and input[y+1][x-1]  == "M" and input[y-1][x+1]  == "S" and input[y+1][x+1]  == "S":
        return True
    except IndexError:
      pass
    return False
  
  def check_m_up(x, y):
    try:
      if input[y-1][x-1] == "M" and input[y-1][x+1]  == "M" and input[y+1][x-1]  == "S" and input[y+1][x+1]  == "S":
        return True
    except IndexError:
      pass
    return False
  
  def check_m_right(x, y):
    try:
      if input[y-1][x+1] == "M" and input[y+1][x+1]  == "M" and input[y-1][x-1]  == "S" and input[y+1][x-1]  == "S":
        return True
    except IndexError:
      pass
    return False
  
  def check_m_down(x, y):
    try:
      if input[y+1][x-1] == "M" and input[y+1][x+1]  == "M" and input[y-1][x-1]  == "S" and input[y-1][x+1]  == "S":
        return True
    except IndexError:
      pass
    return False

  for y in range(1, len(input) - 1):
    for x in range(1, len(input[y]) - 1):
      if input[y][x] == "A":
        if check_m_left(x, y):
          xmas_count += 1
        if check_m_up(x, y):
          xmas_count += 1
        if check_m_right(x, y):
          xmas_count += 1
        if check_m_down(x, y):
          xmas_count += 1

  return xmas_count

if __name__ == '__main__':
  input_lines = parse_input_lines()
  input = parse_input(input_lines)
  result = solve(input)
  print(f'Result: {result}')
