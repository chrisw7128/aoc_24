def load_data():
    with open('data_11.txt') as fin:
        myfile = [int(item) for item in fin.read().split()]
    return myfile

def transform_stone(item):
    exclude = 'blank'
    if item == 0:
        item = 1
        return item, exclude
    elif len(str(item)) % 2 == 0:
        item_str = str(item)
        item_midpoint = int((len(str(item)) / 2))
        left = int(item_str[:item_midpoint])
        right = int(item_str[item_midpoint:])
        return left, right
    else:
        item = item * 2024
        return item, exclude

def blink(data):
    new_list = []
    for item in data:
        candidate1, candidate2 = transform_stone(item)
        if candidate1 != 'blank':
            new_list.append(candidate1)
        if candidate2 != 'blank':
            new_list.append(candidate2)
    return new_list

def sample_data():
    return [125, 17]

def blink_multiple_times(times):
    data = load_data()
    for time in range(times):
        data = blink(data)
        print(f'completed time: {time}')
    return data


if __name__ == '__main__':
    print(f'part 1: {len(blink_multiple_times(25))}')
    print(f'part 2: {len(blink_multiple_times(75))}')