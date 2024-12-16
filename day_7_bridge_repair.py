from pprint import pprint
from itertools import product

with open(f'data_7.txt') as fin:
    myfile = fin.readlines()
    myfile = [[int(num) for num in item.replace(":", "").replace("\n", "").split()] for item in myfile]
    # # Tried nested lists below:
    # myfile = [row.split(':') for row in myfile]
    # myfile = [[item.strip() for item in sublist] for sublist in myfile]
    # myfile = [[item.split() for item in sublist] for sublist in myfile]
    # myfile = [[[int(item) for item in nested_list] for nested_list in sublist] for sublist in myfile]
    # # Tried dict below:
    # myfile = {int(k.strip()): v.strip().split() for item in myfile for k, v in [item.split(':')]}
    # myfile = {k: [int(v) for v in value_list] for k, value_list in myfile.items()}

    # pprint(myfile)

# Part 1 / 2
    
def find_matches(mylist, operators):
    matches = 0
    for item in mylist:
        # print('********')
        k = item[0]
        v = item[1:]
        # print(f'evaluating {k}, {v}')
        math_combos = list(product((operators), repeat=len(v)-1))
        # print(f'num math combos: {len(math_combos)}')
        for combo in math_combos:
            # print('**')
            my_expression = v[0]
            myzip = list(zip(v[1:], combo))
            # print(f'approx eval: {my_expression} {[f"{item[1]} {item[0]}" for item in myzip]}')
            # print(f'key: {k}')
            for num in myzip:
                if num[1] == '+':
                    my_expression += num[0]
                elif num[1] == '*':
                    my_expression *= num[0]
                elif num[1] == '||':
                    my_expression = int(f'{my_expression}{num[0]}')
            # print(f'ans: {my_expression}')
            if k == my_expression:
                matches += k
                break
        # print('********')
    return matches

part_1_operators = ["+", "*"]
matches = find_matches(myfile, part_1_operators)
print(f'Part 1 matches: {matches}')

# Part 2 / 2

part_2_operators = ["+", "*", "||"]
matches = find_matches(myfile, part_2_operators)
print(f'Part 2 matches: {matches}')