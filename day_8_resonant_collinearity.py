from pprint import pprint
from itertools import combinations

with open('data_8.txt') as fin:
    myfile = [row.strip() for row in fin]

# pprint(myfile)
# pprint(type(myfile))

# Part 1 / 2

# Create a mapping of antennas to same-type neighboring antennas
def find_antennas(grid: list) -> dict:
    locations = {}
    for row_index, row in enumerate(grid):
        for col_index, col in enumerate(row):
            if col != '.':
                if col in locations:
                    locations[col].append((row_index, col_index))
                else:
                    locations[col] = [(row_index, col_index)]
    return locations

antenna_locations = find_antennas(myfile)
# print(f'antenna locations: {antenna_locations}\n')

# Find pairs of antennas of the same character
def find_pairs_of_antennas(locations: dict) -> dict:
    pairs_of_antennas = []
    for k, v in locations.items():
        # print(f'locations of same antennas: {v}')
        pairs_of_antennas.append(list(combinations(v, 2)))
    flattened_list = []
    for sublist in pairs_of_antennas:
        for nested_tuple in sublist:
            flattened_list.append(nested_tuple)
    return flattened_list

pairs_of_antennas = find_pairs_of_antennas(antenna_locations)
# print(f'pairs of same antennas: {pairs_of_antennas}')

# Find the distance between each pair of antennas of the same character
def find_delta_in_locations_between_pairs_of_antennas(pairs):
    pairs_with_differences = []
    for pair_of_locations in pairs:
        difference1 = (pair_of_locations[0][0]-pair_of_locations[1][0], pair_of_locations[0][1]-pair_of_locations[1][1])
        difference2 = (pair_of_locations[1][0]-pair_of_locations[0][0], pair_of_locations[1][1]-pair_of_locations[0][1])
        pairs_with_differences.append((pair_of_locations, (difference1, difference2)))
    return pairs_with_differences

pairs_with_differences = find_delta_in_locations_between_pairs_of_antennas(pairs_of_antennas)
# print('pairs of antennas with differences:')
# pprint(pairs_with_differences)

# Flip each difference identified for each item in each pair to find the antinode
def find_antinodes(pairs_with_difs):
    antinode_locations = []
    for full_pair_info in pairs_with_difs:
        # print(full_pair_info)
        # print(full_pair_info[0])
        # print(full_pair_info[0][0][0])
        # print(full_pair_info[0][0][1])
        # print(full_pair_info[0][1][0])
        # print(full_pair_info[0][1][1])
        # print(full_pair_info[1][0][0])
        # print(full_pair_info[1][0][1])
        # print(full_pair_info[1][1][0])
        # print(full_pair_info[1][1][1])
        # # Antinodes: (1+7),(2+8)
        # # Antinodes (3+5),(4+6)

        antinode1 = ((full_pair_info[0][0][0]+full_pair_info[1][0][0]),(full_pair_info[0][0][1]+full_pair_info[1][0][1]))
        # print(f'node1: {(full_pair_info[0][1][0]+full_pair_info[1][0][0]), (full_pair_info[0][1][1]+full_pair_info[1][0][1])} antinode 1: {antinode1}')
        antinode_locations.append(antinode1)
        antinode2 = ((full_pair_info[0][1][0]+full_pair_info[1][1][0]),(full_pair_info[0][1][1]+full_pair_info[1][1][1]))
        # print(f'node2: {(full_pair_info[0][0][0]+full_pair_info[1][1][0],full_pair_info[0][0][1]+full_pair_info[1][1][1])} antinode 2: {antinode2}')
        antinode_locations.append(antinode2)
    return antinode_locations

antinode_locations = set(find_antinodes(pairs_with_differences))

def apply_antinode_locations(grid, locations):
    new_grid = []
    for row in grid:
        new_grid.append(list(row))
    new_grid_rows = len(new_grid)
    print(f'new grid rows: {new_grid_rows}')
    new_grid_cols = len(new_grid[0])
    print(f'new grid cols: {new_grid_cols}')
    for location in locations:
        if location[0] >= 0 and location[0] <= (new_grid_rows - 1) and location[1] >= 0 and location[1] <= (new_grid_cols - 1):
            # print(f'location: {location[0], location[1]}')
            new_grid[location[0]][location[1]] = '#'
    return new_grid

# print(f'antinode locations: {antinode_locations}')
print(f'number of antinodes: {len(antinode_locations)}')

antinode_grid = apply_antinode_locations(myfile, antinode_locations)
# print('original grid:')
# pprint(myfile)
# print('antinode grid:')
# pprint(antinode_grid)

def count_total_antinodes(grid):
    count = 0
    for row in grid:
        for col in row:
            if col == '#':
                count += 1
    return count

total_count = count_total_antinodes(antinode_grid)
print(f'total count: {total_count}')

# Part 2 / 2

