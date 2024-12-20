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
print(visualized_input)

def reorder_list(visualized_list):
    new_list = visualized_list.copy()
    print(f'new list: {new_list}')
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
print(rearranged_input)

def find_checksum(arranged_input):
    ans = 0
    for index, number in enumerate(arranged_input):
        ans += (index*number)
    return ans

part_1_ans = find_checksum(rearranged_input)
print(f'part 1 ans: {part_1_ans}')

# Part 2 / 2

# Use 'rearranged_input' from Part 1

