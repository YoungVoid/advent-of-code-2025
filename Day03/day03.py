
def get_data(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        data = f.readlines()
    return data


def main(file_path: str):

    data = get_data(file_path)

    total = 0

    for line in data:
        line_list = list(line)

        first_number = max(line_list[:-2])
        first_number_pos = list(line).index(first_number)

        second_number = max(line_list[first_number_pos+1:])
        
        number = int(first_number + second_number)
        total += number
    
    print(total)
        
        



if __name__ == '__main__':
    file_path = str(input('File Path:\n>>> '))
    main(file_path)
