# Read input-exercise-1.txt file

def get_test_input() -> list[str]:
  return ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']

def get_code(line) -> str:
  first_number_in_line: int = [int(char) for char in line if char.isdigit()][0]
  last_number_in_line: int = [int(char) for char in line if char.isdigit()][-1]
  return f'{first_number_in_line}{last_number_in_line}'

def get_puzzle_input() -> str:
  with open('./day-1/input-exercise-1.txt', 'r') as file:
    return file.read()


if __name__ == '__main__':
  lines: list[str] = get_puzzle_input().split('\n')
  lines.remove('')
  print(lines)
  codes = []
  for line in lines:
    codes.append(get_code(line))

  # Anwser
  print(sum([int(code) for code in codes]))
