from rich import print

def get_data(file_path: str) -> list[str]:
    data = []
    with open(file_path, 'r') as f:
        data = f.readlines()

    return [line.strip() for line in data]




def main(file_path: str):

    data = get_data(file_path)

    total_splits = 0
    beam_columns = []

    start_column_position = data[0].index('S')
    beam_columns.append(start_column_position)

    for i in range(1, len(data)):
        beam_columns_snapshot = beam_columns.copy() # Just ensure that we dont add a column and then process it in the same for
        for column in beam_columns_snapshot:
            if data[i][column] == '.':
                data[i] = data[i][0:column] + '|' + data[i][column+1:]
            elif data[i][column] == '^':
                total_splits += 1
                beam_columns.remove(column)
                if column-1 not in beam_columns:
                    beam_columns.append(column-1)
                if column+1 not in beam_columns:
                    beam_columns.append(column+1)



if __name__ == '__main__':
    file_path = str(input('File Path:\n>>> '))
    main(file_path)
