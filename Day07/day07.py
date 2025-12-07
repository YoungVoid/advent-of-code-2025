from rich import print

def get_data(file_path: str) -> list[str]:
    data = []
    with open(file_path, 'r') as f:
        data = f.readlines()

    return [line.strip() for line in data]

def run_timeline_and_get_splits_at_end(data: list[str], start_line, start_column) -> int:
    '''
    run main timeline:


    get map
    get column
    run beam down until end of loop
    if hit splitter
        create left timeline
        create right timeline
        break out of loop since this one wont end at bottom
    '''

    timeline_data = data.copy()
    total_splits_at_end = 0

    for i in range(start_line, len(timeline_data)):
        if data[i][start_column] == '.':
            data[i] = data[i][0:start_column] + '|' + data[i][start_column+1:]
        elif data[i][start_column] == '^':
            total_splits_at_end += run_timeline_and_get_splits_at_end(timeline_data, i+1, start_column-1) # left timeline
            total_splits_at_end += run_timeline_and_get_splits_at_end(timeline_data, i+1, start_column+1) # right timeline
            return total_splits_at_end



    total_splits_at_end = 1
    return total_splits_at_end


def main(file_path: str):

    data = get_data(file_path)

    total_splits = 0
    beam_columns = []

    start_column_position = data[0].index('S')
    start_line_position = 1

    total_splits = run_timeline_and_get_splits_at_end(data, start_line_position, start_column_position)

    print(total_splits)
    



if __name__ == '__main__':
    file_path = str(input('File Path:\n>>> '))
    main(file_path)
