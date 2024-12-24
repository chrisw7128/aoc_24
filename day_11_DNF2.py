import time

# Attempt 1 / 2 (solved part 1, failed on part 2)

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

def blink_multiple_times(num_blinks):
    data = load_data()
    for blink_num in range(num_blinks):
        start_time = time.perf_counter()
        data = blink(data)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f'completed blink: {blink_num} time taken: {elapsed_time:.6f}')
    return data


if __name__ == '__main__':
    print(f'part 1: {len(blink_multiple_times(25))}')
    print(f'part 1 ans: 233050')
    print(f'part 2: {len(blink_multiple_times(75))}')

# # Attempt 2 / 2 (did not work)

# from collections import defaultdict
    
# def load_data():
#     with open('data_11.txt') as fin:
#         mylist = [int(item) for item in fin.read().split()]
#         mydict = defaultdict(int)
#         for item in mylist:
#             mydict[item] += 1
#     return mydict
    
# def transform_stone(item):
#     exclude = 'blank'
#     if item == 0:
#         item = 1
#         return item, exclude
#     elif len(str(item)) % 2 == 0:
#         item_str = str(item)
#         item_midpoint = int((len(str(item)) / 2))
#         left = int(item_str[:item_midpoint])
#         right = int(item_str[item_midpoint:])
#         return left, right
#     else:
#         item = item * 2024
#         return item, exclude

# def blink(data):
#     new_dict = defaultdict(int)
#     for k, v in data.items():
#         for i in range(v):
#             candidate1, candidate2 = transform_stone(k)
#             if candidate1 != 'blank':
#                 new_dict[candidate1] += 1
#             if candidate2 != 'blank':
#                 new_dict[candidate2] += 1
#     return new_dict

# def sample_data():
#     return [125, 17]

# def blink_multiple_times(num_blinks):
#     data = load_data()
#     for blink_num in range(num_blinks):
#         start_time = time.perf_counter()
#         data = blink(data)
#         end_time = time.perf_counter()
#         elapsed_time = end_time - start_time
#         print(f'completed blink: {blink_num} time taken: {elapsed_time:.6f}')
#     return data


# if __name__ == '__main__':
#     print(f'part 1: {len(blink_multiple_times(25))}')
#     print(f'part 2: {len(blink_multiple_times(75))}')