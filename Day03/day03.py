
def get_data(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        data = f.readlines()
    return data

def get_highest_number_position(line: str) -> int:
    highest_number_position = -1
    highest_number = 0
    for i in range(len(line)-1):
        number = int(line[i])
        if number > highest_number:
            highest_number = number
            highest_number_position = i

    return highest_number_position if highest_number_position > -1 else 0


def main(file_path: str):

    data = get_data(file_path)

    for line in data:
        i = get_highest_number_position(line)
        
        



if __name__ == '__main__':
    # file_path = str(input('File Path:\n>>> '))
    # main(file_path)
    a = '132'
    print(a.index('3'))
