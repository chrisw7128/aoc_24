import time

with open('data_6.txt') as fin:
    myfile = [list(line.strip()) for line in fin]

def find_starting_position(grid):
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == '^' or value == '>' or value == '<' or value == 'v':
                starting_row = int(i)
                starting_col = int(j)
                starting_character = value
    return starting_row, starting_col, starting_character

starting_row, starting_col, starting_character = find_starting_position(myfile)
print(f'Starting row: {starting_row}\nStarting col: {starting_col}\nStarting character: {starting_character}')

def move_positions(current_row: int, current_col: int, current_character: str, grid_state: list):
    moves = 0
    myloop = True
    while myloop == True:
        # time.sleep(0.05) # Pause for 0.05 seconds to view the print illustration
        if current_character == '^':
                try:
                    if grid_state[current_row - 1][current_col] != '#':
                        grid_state[current_row - 1][current_col] = '^'
                        grid_state[current_row][current_col] = 'X'
                        current_row = current_row - 1
                    else:
                        current_character = '>'
                except IndexError:
                     myloop = False
                     continue
        elif current_character == '>':
                try:
                    if grid_state[current_row][current_col + 1] != '#':
                        grid_state[current_row][current_col + 1] = '>'
                        grid_state[current_row][current_col] = 'X'
                        current_col = current_col + 1
                    else:
                        current_character = 'v'
                except IndexError:
                     myloop = False
                     continue
        elif current_character == 'v':
                try:
                    if grid_state[current_row + 1][current_col] != '#':
                        grid_state[current_row + 1][current_col] = 'v'
                        grid_state[current_row][current_col] = 'X'
                        current_row = current_row + 1
                    else:
                        current_character = '<'
                except IndexError:
                     myloop = False
                     continue
        elif current_character == '<':
                try:
                    if grid_state[current_row][current_col - 1] != '#':
                        grid_state[current_row][current_col - 1] = '<'
                        grid_state[current_row][current_col] = 'X'
                        current_col = current_col - 1
                    else:
                        current_character = '^'
                except IndexError:
                     myloop = False
                     continue
        moves += 1
        print('\n**********\n')
        print(f'Current position: {current_row},{current_col}')
        print(f'Current character: {current_character}')
        print(f'Moves: {moves}')
        for line in grid_state:
            print(line)
    return grid_state

def get_spaces_touched(grid):
    spaces_touched = 0
    for row in grid:
            for position in row:
                if position == 'X':
                    spaces_touched += 1
    spaces_touched += 1 # Add one more space touched for the final location that ran into the IndexError
    return spaces_touched

final_grid = move_positions(starting_row, starting_col, starting_character, myfile)
spaces_touched = get_spaces_touched(final_grid)
print(f'Spaces touched: {spaces_touched}')

