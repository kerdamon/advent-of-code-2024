from common import parse_input_lines
import re

def parse_input(input_lines: list[str]):
  return ''.join(input_lines)

def solve(input) -> int:
  result = 0
  beginning_pattern = r"^(.*?(?=don't\(\)))"
  middle_patern = r"(?<=do\(\)).*?(?=don\'t\(\))"
  end_part = input.split('do()')[-1] # for some reason I can't figure out how to match the end of the string using regexes
  enabled_instructions = ''.join(re.findall(beginning_pattern, input) + re.findall(middle_patern, input) + [end_part])
  matches = re.findall(r'mul\(\d+,\d+\)', enabled_instructions)
  for match in matches:
    numbers = re.findall(r'\d+', match)
    result += int(numbers[0]) * int(numbers[1])
  return result

if __name__ == '__main__':
  input_lines = parse_input_lines()
  input = parse_input(input_lines)
  result = solve(input)
  print(f'Result: {result}')
