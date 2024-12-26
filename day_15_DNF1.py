from pprint import pprint
# from pydantic import BaseModel
# import re

def load_data():
    with open('data_15.py') as fin:
        myfile = fin.readlines()
        data1 = [item.strip() for item in myfile[:50]]
        data2 = list(''.join(myfile[51:]))
        pprint(f'data1: {data1}')
        # pprint(f"data2: {data2}")
    return data1, data2

def find_current_position():
    grid, moves = load_data()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                current_position = (i, j)
                print(f'current position: {current_position}')
    return current_position

def try_to_move():
    grid, moves = load_data()
    current_position = find_current_position()
    for move in moves:
        if move == '<':
            if '.' in grid[:current_position[0]]:
                pass
            elif '.' not in grid[:current_position[0]]:
                break
        elif move == '^':
            if '.' in grid[:current_position[1]]:
                pass
            elif '.' not in grid[:current_position[1]]:
                pass
        elif move == '>':
            if '.' in grid[current_position[0]:]:
                pass
            elif '.' not in grid[current_position[0]:]:
                pass
        elif move == 'v':
            if '.' in grid[current_position[1]:]:
                pass
            elif '.' not in grid[current_position[1]:]:
                pass

try_to_move()
