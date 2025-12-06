from numpy import equal
from rich import print

def get_number_of_digits_per_line(list_of_number_list: list[list[str]]) -> int:
    number_of_digits_per_line = 0
    for list_of_numbers in list_of_number_list:
        print(''.join(list_of_numbers))
        number_of_digits_per_line = max(number_of_digits_per_line, len(''.join(list_of_numbers)))
    # number_of_digits_per_line = len(''.join(numbers[0]))
    return number_of_digits_per_line

def get_list_with_numbers_equal_size(list_of_number_list: list[list[str]], number_of_digits_per_number: int, number_of_columns: int) -> list[list[str]]:
    equal_size_numbers = []
    for list_of_numbers in list_of_number_list:
        number = ''.join(list_of_numbers)
        new_list = []
        pos = 0
        for i in range(number_of_columns):
            new_list.append(number[pos:pos+number_of_digits_per_number])
            pos+=number_of_digits_per_number
        equal_size_numbers.append(new_list)
    
    return equal_size_numbers

def get_reversed_numbers_and_list(list_of_number_list: list[list[str]]) -> list[list[str]]:
    reversed_numbers_and_list = []
    for list_of_numbers in list_of_number_list:
        new_list = [num[::-1] for num in list_of_numbers]
        reversed_numbers_and_list.append(new_list)
    reversed_numbers_and_list = reversed_numbers_and_list[::-1]

    return reversed_numbers_and_list

def get_exploded_numbers(list_of_number_list: list[list[str]]) -> list[list[str]]:
    exploded_numbers = []
    for list_of_numbers in list_of_number_list:
        new_list = []
        for num in list_of_numbers:
            new_list.append(list(num))
        exploded_numbers.append(new_list)

    return exploded_numbers

def get_zipped_exploded_numbers(list_of_number_list: list[list[str]]) -> list[list[str]]:
    zipped_exploded_numbers = []
    for list_of_numbers in list_of_number_list:
        # for numbers in list_of_number_list:
        #     print(numbers)
        zipped_exploded_numbers.append(list(zip(*list_of_numbers)))

    return zipped_exploded_numbers

def get_formatted_numbers(list_of_number_list: list[list[str]]) -> list[list[int]]:
    formatted_numbers = []
    for list_of_numbers in list_of_number_list:
        new_list = []
        for num in list_of_numbers:
            new_list.append(int(''.join(num).replace('-','')))
        formatted_numbers.append(new_list)

    return formatted_numbers

def get_data(file_path: str) -> tuple[list[list[int]], list[str]]:
    with open(file_path, 'r') as f:
        file_data = f.readlines()

    valid_calcs = {'*','+'}

    numbers = [[num.strip() if num not in ['','\n'] else '-' for num in line.split(' ')] for line in file_data[:-1]]
    #sized_numbers = list(zip(*numbers))
    operators = [op for op in file_data[-1].split(' ') if op in valid_calcs]
    reversed_operators = operators[::-1]
    number_of_columns = len(operators)

    number_of_digits_per_line = get_number_of_digits_per_line(numbers)

    number_of_digits_per_number = number_of_digits_per_line // number_of_columns

    #
    # List Formatting starts here
    #
    equal_size_numbers = get_list_with_numbers_equal_size(numbers,number_of_digits_per_number,number_of_columns)

    zipped_numbers = list(zip(*equal_size_numbers))

    reversed_numbers_and_list = get_reversed_numbers_and_list(zipped_numbers)

    # from_up_to_down_list = []
    # for list_of_number_list in reversed_numbers_and_list:
    #     new_list = []
    #     for i in range(number_of_digits_per_number):
    #         new_list.append(''.join)

    exploded_numbers = get_exploded_numbers(reversed_numbers_and_list)

    zipped_exploded_numbers = get_zipped_exploded_numbers(exploded_numbers)

    formatted_numbers = get_formatted_numbers(zipped_exploded_numbers)

    # print(numbers)
    # print(f'digits(line): {number_of_digits_per_line}')
    # print(f'digits(number): {number_of_digits_per_number}')
    # print(f'cols: {number_of_columns}')
    # print(f'sized: {equal_size_numbers}')
    # print(f'zipped: {zipped_numbers}')
    # print(f'reversed: {reversed_numbers_and_list}')
    # print(f'exploded: {exploded_numbers}')
    # print(f'zip exp: {zipped_exploded_numbers}')
    # print(f'formatted: {formatted_numbers}')
    # print(f'operators: {reversed_operators}')

    return formatted_numbers, reversed_operators


def calculate(list_of_number_list: tuple[int], operator: str) -> int:
    if operator == '*':
        total = 1
    else:
        total = 0

    for number in list_of_number_list:
        print(number, operator, total)
        if operator == '*':
            total *= number
        elif operator == '+':
            total += number
    print(total)
    return total

def main(file_path: str):

    numbers, operators = get_data(file_path)

    total = 0

    for num_list_i in range(len(numbers)):
        list_of_number_list = numbers[num_list_i]
        operator = operators[num_list_i]

        total += calculate(list_of_number_list, operator)


    print(total)



if __name__ == '__main__':
    file_path = str(input('File Path:\n>>> '))
    main(file_path)
