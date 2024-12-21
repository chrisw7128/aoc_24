from pprint import pprint

with open (f'data_9_2.txt') as fin:
    myfile = [int(item) for item in fin.read()]

# Part 1 / 2

def convert_input_to_visualization(myfile):
    output = []
    file_count = 0
    for index, number in enumerate(myfile):
        if index % 2 == 0:
            for _ in range(number):
                output.append(file_count)
            file_count += 1
        elif index % 2 != 0:
            for _ in range(number):
                output.append('.')
    return output

visualized_input = convert_input_to_visualization(myfile)
print(f'visualized input: {visualized_input}')

def reorder_list(visualized_list):
    new_list = visualized_list.copy()
    # print(f'new list: {new_list}')
    thing = 1
    while thing:
        if '.' in new_list:
            if new_list[-1] != '.':
                last = new_list.pop(-1)
                for index in range(len(new_list)):
                    if new_list[index] == '.':
                        new_list[index] = last
                        break
            elif new_list[-1] == '.':
                new_list.pop(-1)
        elif '.' not in new_list:
            thing = 0
    return new_list

rearranged_input = reorder_list(visualized_input)
# print(f'rearranged input: {rearranged_input}')

def find_checksum(arranged_input):
    ans = 0
    for index, number in enumerate(arranged_input):
        ans += (index*number)
    return ans

part_1_ans = find_checksum(rearranged_input)
print(f'part 1 ans: {part_1_ans}')

# Part 2 / 2

# Use 'visualized_input' from Part 1

def get_file_names_and_sizes(visual_input):
    new_dict = {}
    for item in visual_input:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    del(new_dict['.'])
    new_list = []
    for k, v in new_dict.items():
        new_list.append((int(k), v))
    return new_list

# def get_file_names_and_sizes(visual_input):
#     new_dict = {}
#     for i in range(len(visual_input)):
#         if (i, visual_input[i]) in new_dict:
#             new_dict[(i, visual_input[i])] += 1
#         else:
#             new_dict[(i, visual_input[i])] = 1
#     # del(new_dict['.'])
#     new_list = []
#     for k, v in new_dict.items():
#         new_list.append(((int(k[0]), '.' if '.' else (int(k[1]))), v))
#     return new_dict

file_name_file_len = get_file_names_and_sizes(visualized_input)
print(f'(file name, file len):')
pprint(file_name_file_len)

def find_len_of_period_seqs(visual_input):
    periods_dict = {}
    new_list = []
    for i in range(len(visual_input)):
        if visual_input[i] == '.' and visual_input[i-1] != '.':
            new_start = i
            if new_start in periods_dict:
                periods_dict[i].append[i]
            else:
                periods_dict[i] = [i]
        if visual_input[i] == '.' and visual_input[i-1] == '.':
            periods_dict[new_start].append(i)
    for k, v in periods_dict.items():
        new_list.append((k, len(v)))
    return new_list

period_start_period_len = find_len_of_period_seqs(visualized_input)
print(f'(period start, period len):')
pprint(period_start_period_len)

def create_new_seq(file_name_file_len, period_start_period_len):
    new_list = []
    
def different_approach(visual_input):
    new_list = reversed(visual_input)
    return new_list

reversed_list = list(different_approach(visualized_input))
print(f'reversed list: ')
print(f'{reversed_list}')

def find_last_file_num(reversed_list):
    for item in reversed_list:
        if item != '.':
            largest = item
            break
    return largest

largest_file = find_last_file_num(reversed_list)
print(f'largest file: {largest_file}')

def find_new_location_for_files(visual_input, largest_file, file_name_file_len):
    end_of_list = list(reversed(file_name_file_len))
    print(end_of_list)
    # for i in range(len(visual_input)):

find_new_location_for_files(visualized_input, largest_file, file_name_file_len)

