from common import parse_input_lines

def parse_input(input_lines: list[str]):
  reports = []
  for line in input_lines:
    reports.append([int(level) for level in line.split(' ')])
  return reports

def solve(reports) -> int:
  number_of_safe_reports = 0

  def is_report_safe(report):
    if report[1] > report[0]: # this should be increasing
      for i in range(len(report) - 1):
        if (report[i+1] <= report[i]): # levels not increasing - unsafe
          return False
        if (report[i+1] > (report[i] + 3)): # levels increasing too fast - unsafe
          return False
    elif report[1] < report[0]: # this should be decreasing
      for i in range(len(report) - 1):
        if (report[i+1] >= report[i]):  # levels not decreasing - unsafe
          return False
        if (report[i+1] < (report[i] - 3)): # levels decreasing too fast - unsafe
          return False
    else: # levels not changing - unsafe
      return False
    return True

  for report in reports:
    if is_report_safe(report):
      number_of_safe_reports += 1
  
  return number_of_safe_reports

if __name__ == '__main__':
  input_lines = parse_input_lines()
  reports = parse_input(input_lines)
  result = solve(reports)
  print(f'Result: {result}')
