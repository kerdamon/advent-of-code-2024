from common import parse_input_lines
import re

def parse_input(input_lines: list[str]):
  return ''.join(input_lines)

def solve(input) -> int:
  result = 0
  matches = re.findall(r'mul\(\d+,\d+\)', input)
  for match in matches:
    numbers = re.findall(r'\d+', match)
    result += int(numbers[0]) * int(numbers[1])
  return result

if __name__ == '__main__':
  input_lines = parse_input_lines()
  input = parse_input(input_lines)
  result = solve(input)
  print(f'Result: {result}')
