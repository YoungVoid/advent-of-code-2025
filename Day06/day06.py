from rich import print

def get_data(file_path: str) -> tuple[list[tuple[int]], list[str]]:
    with open(file_path, 'r') as f:
        file_data = f.readlines()

    stripped_data = [line for line in file_data]

    valid_calcs = {'*','+'}

    numbers = [[num.strip() if num not in ['','\n'] else '0' for num in line.split(' ')] for line in stripped_data[:-1]]
    #sized_numbers = list(zip(*numbers))
    operators = [op for op in stripped_data[-1].split(' ') if op in valid_calcs]
    reversed_operators = operators[::-1]
    number_of_columns = len(operators)

    number_of_digits_per_line = 0
    for number_list in numbers:
        print(''.join(number_list))
        number_of_digits_per_line = max(number_of_digits_per_line, len(''.join(number_list)))
    # number_of_digits_per_line = len(''.join(numbers[0]))

    number_of_digits_per_number = number_of_digits_per_line // number_of_columns
    sized_numbers = []
    for number_list in numbers:
        number = ''.join(number_list)
        new_list = []
        pos = 0
        for i in range(number_of_columns):
            new_list.append(number[pos:pos+number_of_digits_per_number])
            pos+=number_of_digits_per_number
        sized_numbers.append(new_list)

    zipped_numbers = list(zip(*sized_numbers))

    reverse_numbers_and_list = []
    for number_list in zipped_numbers:
        new_list = [num[::-1] for num in number_list]
        reverse_numbers_and_list.append(new_list)
    reverse_numbers_and_list = reverse_numbers_and_list[::-1]

    # from_up_to_down_list = []
    # for number_list in reverse_numbers_and_list:
    #     new_list = []
    #     for i in range(number_of_digits_per_number):
    #         new_list.append(''.join)

    exploded_numbers = []
    for number_list in reverse_numbers_and_list:
        new_list = []
        for num in number_list:
            new_list.append(list(num))
        exploded_numbers.append(new_list)

    zipped_exploded_numbers = []
    for number_list in exploded_numbers:
        # for numbers in number_list:
        #     print(numbers)
        zipped_exploded_numbers.append(list(zip(*number_list)))

    formatted_numbers = []
    for number_list in zipped_exploded_numbers:
        new_list = []
        for num in number_list:
            new_list.append(int(''.join(num)))
        formatted_numbers.append(new_list)
        


    print(numbers)
    print(f'digits(line): {number_of_digits_per_line}')
    print(f'digits(number): {number_of_digits_per_number}')
    print(f'cols: {number_of_columns}')
    print(f'sized: {sized_numbers}')
    print(f'zipped: {zipped_numbers}')
    print(f'reversed: {reverse_numbers_and_list}')
    print(f'exploded: {exploded_numbers}')
    print(f'zip exp: {zipped_exploded_numbers}')
    print(f'formatted: {formatted_numbers}')
    print(f'operators: {reversed_operators}')

    return formatted_numbers, reversed_operators


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
