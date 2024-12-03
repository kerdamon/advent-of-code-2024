from common import parse_input_lines

def parse_input(input_lines: list[str]):
  left = []
  right = []
  for line in input_lines:
    numbers = line.split(' ')
    left.append(int(numbers[0].strip()))
    right.append(int(numbers[-1].strip()))
  return left, right

def solve(left, right) -> int:
  left = sorted(left)
  right = sorted(right)
  distance = 0
  for l, r in zip(left, right):
    distance += abs(r - l)
  return distance

if __name__ == '__main__':
  input_lines = parse_input_lines()
  left, right = parse_input(input_lines)
  result = solve(left, right)
  print(f'Result: {result}')
