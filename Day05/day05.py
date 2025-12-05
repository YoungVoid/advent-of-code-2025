from rich import print
import bisect

def get_data(file_path: str) -> tuple[list[list[int]], list[int]]:
    with open(file_path, 'r') as f:
        data = f.readlines()

    blank_line_position = data.index('\n')

    fresh_range_data = [[int(num) for num in line.strip().split('-')] for line in data[0:blank_line_position]]
    ingredient_id_list = [int(line.strip()) for line in data[blank_line_position+1:]]

    return fresh_range_data, ingredient_id_list


def main(file_path: str):

    fresh_range_data, ingredient_id_list = get_data(file_path)
    ingredient_id_list = sorted(ingredient_id_list)

    total = 0
    fresh_list = []
    fresh_ingredient_list = []

    for fresh_from, fresh_to  in fresh_range_data:
        lowPos = bisect.bisect_left(ingredient_id_list, fresh_from)
        highPos = bisect.bisect_right(ingredient_id_list, fresh_to)


        for fresh_ingredient in ingredient_id_list[lowPos:highPos]:
            if fresh_ingredient not in fresh_ingredient_list:
                fresh_ingredient_list.append(fresh_ingredient)
        

    print(len(fresh_ingredient_list))
        
        



if __name__ == '__main__':
    file_path = str(input('File Path:\n>>> '))
    main(file_path)
