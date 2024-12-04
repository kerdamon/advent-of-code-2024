from common import parse_input_lines

def parse_input(input_lines: list[str]):
  return input_lines

def solve(input) -> int:
  xmas_count = 0

  def next_index(i, times, backwards=False):
    next_index = 0
    if backwards:
      next_index = i - times
    else:
      next_index = i + times
    if next_index < 0:
      raise IndexError
    return next_index

  def check_vertically(x, y, backwards=False):
    try:
      if input[y][next_index(x, 1, backwards)] == "M" and input[y][next_index(x, 2, backwards)] == "A" and input[y][next_index(x, 3, backwards)] == "S":
        return True
    except IndexError:
      pass
    return False

  def check_horizontally(x, y, backwards=False):
    try:
      if input[next_index(y, 1, backwards)][x] == "M" and input[next_index(y, 2, backwards)][x] == "A" and input[next_index(y, 3, backwards)][x] == "S":
        return True
    except IndexError:
      pass
    return False

  def check_diagonally_slash(x, y, backwards=False):
    try:
      if input[next_index(y, -1, backwards)][next_index(x, 1, backwards)] == "M" and input[next_index(y, -2, backwards)][next_index(x, 2, backwards)]  == "A" and input[next_index(y, -3, backwards)][next_index(x, 3, backwards)]  == "S":
        return True
    except IndexError:
      pass
    return False

  def check_diagonally_backslash(x, y, backwards=False):
    try:
      if input[next_index(y, 1, backwards)][next_index(x, 1, backwards)] == "M" and input[next_index(y, 2, backwards)][next_index(x, 2, backwards)]  == "A" and input[next_index(y, 3, backwards)][next_index(x, 3, backwards)]  == "S":
        return True
    except IndexError:
      pass
    return False

  for y in range(len(input)):
    for x in range(len(input[y])):
      if input[y][x] == "X":
        if check_vertically(x, y):
          xmas_count += 1
        if check_vertically(x, y, backwards=True):
          xmas_count += 1
        if check_horizontally(x, y):
          xmas_count += 1
        if check_horizontally(x, y, backwards=True):
          xmas_count += 1
        if check_diagonally_slash(x, y):
          xmas_count += 1
        if check_diagonally_slash(x, y, backwards=True):
          xmas_count += 1
        if check_diagonally_backslash(x, y):
          xmas_count += 1
        if check_diagonally_backslash(x, y, backwards=True):
          xmas_count += 1

  return xmas_count

if __name__ == '__main__':
  input_lines = parse_input_lines()
  input = parse_input(input_lines)
  result = solve(input)
  print(f'Result: {result}')
