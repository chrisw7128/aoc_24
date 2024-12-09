import re
from pprint import pprint

with open('day_3_input.txt') as fin:
    myfile = fin.read()

# Part 1/2

matches = re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', myfile)

total = 0

for match in matches:
    ans = int(match.group(1)) * int(match.group(2))
    total += ans

print(f'Part 1 total: {total}')

# Part 2/2

matches = re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)', myfile)

mylist = []

for match in matches:
    mylist.append(match.group())

def filter_muls(list_of_matches):
    muls_to_keep = []
    switch = 'on'
    for item in mylist:
        if item == "don't()":
            switch = 'off'
        elif item == "do()":
            switch = 'on'
        if switch == 'on' and 'mul' in item:
            muls_to_keep.append(item)
    return muls_to_keep

muls_to_keep = filter_muls(mylist)

muls_to_keep_2 = []
for item in muls_to_keep:
    item = item.strip('mul')
    muls_to_keep_2.append(item)

muls_to_keep_3 = []
for item in muls_to_keep_2:
    item = tuple(map(int, item.strip('()').split(',')))
    muls_to_keep_3.append(item)

total = 0
for item in muls_to_keep_3:
    product = item[0]*item[1]
    total += product

print(f'Part 2 total: {total}')
