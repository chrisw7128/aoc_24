import time

with open('data_6_2.txt') as fin:
    myfile = [list(line.strip()) for line in fin]

# Part 1 / 2
    
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
        time.sleep(0.01) # Pause for 0.05 seconds to view the print illustration
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
        print('**********')
        print(f'Current position: {current_row},{current_col}')
        print(f'Current character: {current_character}')
        print(f'Moves: {moves}')
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


# Part 2 / 2

# def get_list_of_places_visited(grid_state):
#     locations_visited = []
#     for row in range(len(grid_state)):
#         for col in range(len(grid_state[row])):
#             if grid_state[row][col] == 'X' or grid_state[row][col] == '^' or grid_state[row][col] == '>' or grid_state[row][col] == 'v' or grid_state[row][col] == '<':
#                 locations_visited.append((row, col))
#     return locations_visited

# locations_visited = get_list_of_places_visited(final_grid)

# def change_location_visited_to_obstacle(grid, location):
#     updated_grid = grid.copy()
#     updated_grid[location[0]][location[1]] = '#'
#     return updated_grid

# def move_positions_2(current_row: int, current_col: int, current_character: str, grid_state: list):
#     moves = 0
#     myloop = True
#     while myloop == True:
#         # time.sleep(0.01) # Pause for 0.05 seconds to view the print illustration
#         if current_character == '^':
#                 try:
#                     if grid_state[current_row - 1][current_col] != '#':
#                         grid_state[current_row - 1][current_col] = '^'
#                         grid_state[current_row][current_col] = 'X'
#                         current_row = current_row - 1
#                     else:
#                         current_character = '>'
#                 except IndexError:
#                      myloop = False
#                      continue
#         elif current_character == '>':
#                 try:
#                     if grid_state[current_row][current_col + 1] != '#':
#                         grid_state[current_row][current_col + 1] = '>'
#                         grid_state[current_row][current_col] = 'X'
#                         current_col = current_col + 1
#                     else:
#                         current_character = 'v'
#                 except IndexError:
#                      myloop = False
#                      continue
#         elif current_character == 'v':
#                 try:
#                     if grid_state[current_row + 1][current_col] != '#':
#                         grid_state[current_row + 1][current_col] = 'v'
#                         grid_state[current_row][current_col] = 'X'
#                         current_row = current_row + 1
#                     else:
#                         current_character = '<'
#                 except IndexError:
#                      myloop = False
#                      continue
#         elif current_character == '<':
#                 try:
#                     if grid_state[current_row][current_col - 1] != '#':
#                         grid_state[current_row][current_col - 1] = '<'
#                         grid_state[current_row][current_col] = 'X'
#                         current_col = current_col - 1
#                     else:
#                         current_character = '^'
#                 except IndexError:
#                      myloop = False
#                      continue
#         moves += 1
#         print('**********')
#         print(f'Current position: {current_row},{current_col}')
#         print(f'Current character: {current_character}')
#         print(f'Moves: {moves}')
#     return grid_state


# def run_simulation_with_each_obstacle(grid, locations_visited, starting_row, starting_col, starting_character):
#     loops_found = 0
#     for location in locations_visited:
#         new_grid = change_location_visited_to_obstacle(grid, location)
#         checked_grid, loop = move_positions(starting_row, starting_col, starting_character, new_grid)
#         loops_found += loop
#     return loops_found

# total_loops = run_simulation_with_each_obstacle(myfile, locations_visited, starting_row, starting_col, starting_character)
# print(f'Total loops found: {total_loops}')
