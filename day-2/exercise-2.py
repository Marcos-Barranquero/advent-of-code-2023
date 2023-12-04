from dataclasses import dataclass

@dataclass
class Handful:
  blue: int
  green: int
  red: int

  def __str__(self) -> str:
    return f'blue: {self.blue}, green: {self.green}, red: {self.red}'

@dataclass
class Result:
  handfuls: list[Handful]

  def get_max_blue(self) -> int:
    return max([handful.blue for handful in self.handfuls])

  def get_max_green(self) -> int:
    return max([handful.green for handful in self.handfuls])

  def get_max_red(self) -> int:
    return max([handful.red for handful in self.handfuls])

  def is_possible(self, handful: Handful) -> bool:
    return handful.blue >= self.get_max_blue() and handful.green >= self.get_max_green() and handful.red >= self.get_max_red()

  def fewest_needed(self) -> Handful:
    min_needed_blue = self.get_max_blue()
    min_needed_green = self.get_max_green()
    min_needed_red = self.get_max_red()
    return Handful(blue=min_needed_blue, green=min_needed_green, red=min_needed_red)


def power(handful: Handful) -> int:
  return handful.blue * handful.green * handful.red

# Description: Day 1, Exercise 1
def get_test_input() -> list[str]:
  return ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

def get_input() -> list[str]:
  with open('day-2/input-exercise-2.txt', 'r') as f:
    return f.readlines()

def to_result(line: str) -> Result:
  handfuls: list[Handful] = []
  line = line.split(':')[1]
  for handful in line.split(';'):
    blue = 0
    green = 0
    red = 0
    colors = handful.split(',')
    for color in colors:
      fixed_color: list[str] = color.strip().split(' ')
      if ('blue' in fixed_color):
        blue = int(fixed_color[0])
      if ('green' in fixed_color):
        green = int(fixed_color[0])
      if ('red' in fixed_color):
        red = int(fixed_color[0])
    handfuls.append(Handful(blue=blue, green=green, red=red))
  return Result(handfuls=handfuls)



if __name__ == '__main__':
  # lines: list[str] = get_test_input()
  lines: list[str] = get_input()
  results = []
  for line in lines:
    result = to_result(line=line)
    results.append(result)

  # Checker 12 red cubes, 13 green cubes, and 14 blue cubes
  checker = Handful(blue=14, green=13, red=12)

  counter_adder = 0
  power_adder = 0
  counter = 1
  for result in results:
    print(f'Game result: {counter}')
    print(f'The max blue is:  {result.get_max_blue()}, the max green is: {result.get_max_green()}, the max red is: {result.get_max_red()}')
    print(f'Game {counter} result is possible: {result.is_possible(checker)}')
    if(result.is_possible(checker)):
      counter_adder += counter

    fewest_needed = result.fewest_needed()
    handful_power = power(fewest_needed)
    power_adder += handful_power
    print(f'The fewest needed for game {counter} is: {fewest_needed}')
    print(f'The power of the fewest needed for game {counter} is: {handful_power}')
    counter += 1
  print(f'The sum of the possible games is: {counter_adder}')
  print(f'The sum of the handful power is: {power_adder}')