
def get_data(file_path: str) -> list[str]:
  data = []
  with open(file_path) as f:
    data = f.readlines()

  return data




def get_new_position(current_position: int, instruction: str) -> int:
    direction = str(instruction[0])
    distance = int(instruction [1:])
    new_position = current_position

    if distance >= 100:
      distance = distance % 100 

    if direction == 'L':
      new_position -= distance
    else: 
      new_position += distance

    if new_position < 0:
      new_position += 100
    elif new_position > 99:
      new_position -= 100

    return new_position




def main():
  file_path = str(input('File Path:\n>>> '))
  print(file_path)

  data = get_data(file_path)

  password = 0
  current_position = 50

  for instruction in data:
    direction = str(instruction[0])
    distance = int(instruction [1:])

    current_position = get_new_position(current_position, instruction)

    if current_position == 0:
      password += 1

  print(f"Password: {password}")
    





if __name__ == '__main__':
  main()