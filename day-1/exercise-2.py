# Description: Day 1, Exercise 2

# This is defined as a global constant so it's not redefined every time the function is called

map_numbers = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9'
}
written_numbers = list(map_numbers.keys())
numbers = list(map_numbers.values())

def get_test_input() -> list[str]:
  return ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']

# Unnecessary function, but I wanted to try it out
def contains_number(line: str) -> bool:
    return any(written_number in line for written_number in written_numbers)


def get_number(line: str, start: int, direction: str = 'left') -> str:
    """Returns the first number or written number in a window of the line based on the direction"""

    if(direction not in ['left', 'right']):
      raise Exception('Direction must be either "left" or "right"')

    window = line[:start]
    next_start = start + 1
    if direction == 'right':
        window = line[start:]
        next_start = start - 1


    for number in numbers:
        if number in window:
            return number

    for written_number in written_numbers:
        if written_number in window:
            return map_numbers[written_number]

    return get_number(line, next_start, direction)


def get_code(line) -> str:
  first_number_in_line: int = int(get_number(line, 0, 'left'))
  last_number_in_line: int = int(get_number(line, len(line), 'right'))
  return f'{first_number_in_line}{last_number_in_line}'

def get_puzzle_input() -> str:
  with open('./day-1/input-exercise-1.txt', 'r') as file:
    return file.read().strip()


if __name__ == '__main__':
  # lines: list[str] = get_test_input()

  lines: list[str] = get_puzzle_input().split('\n')
  codes = []
  for line in lines:
    code = get_code(line)
    codes.append(code)

  # Anwser
  print(f'Final answer: {sum([int(code) for code in codes])}')