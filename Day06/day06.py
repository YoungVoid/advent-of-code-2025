from rich import print

def get_data(file_path: str) -> tuple[list[tuple[int]], list[str]]:
    with open(file_path, 'r') as f:
        file_data = f.readlines()

    stripped_data = [line.strip() for line in file_data]

    valid_calcs = {'*','+'}

    numbers = [[int(num) for num in line.split(' ') if num != ''] for line in stripped_data[:-1]]
    formatted_numbers = list(zip(*numbers))
    operators = [op for op in stripped_data[-1].split(' ') if op in valid_calcs]

    return formatted_numbers, operators


def calculate(number_list: tuple[int], operator: str) -> int:
    if operator == '*':
        total = 1
    else:
        total = 0

    for number in number_list:
        if operator == '*':
            total *= number
        elif operator == '+':
            total += number
    return total

def main(file_path: str):

    numbers, operators = get_data(file_path)

    total = 0

    for num_list_i in range(len(numbers)):
        number_list = numbers[num_list_i]
        operator = operators[num_list_i]
        
        total += calculate(number_list, operator)


    print(total)



if __name__ == '__main__':
    file_path = str(input('File Path:\n>>> '))
    main(file_path)
