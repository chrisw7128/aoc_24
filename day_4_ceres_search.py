with open('data_4.txt') as fin:
    myfile = fin.readlines()

# Part 1 / 2

# Find horizontal matches
def generate_horizontal(grid):
    matches = 0
    for line in grid:
        for i in range(len(line) - 3):
            try:
                word = line[i]+line[i+1]+line[i+2]+line[i+3]
                if word == "XMAS" or word == "SAMX":
                    matches += 1
            except Exception as e:
                continue
    return matches

# Find vertical matches
def generate_vertical(grid):
    matches = 0
    for i in range(len(grid) - 3):
        line1, line2, line3, line4 = grid[i], grid[i+1], grid[i+2], grid[i+3]
        for i in range(len(line1)):
            try:
                word = line1[i]+line2[i]+line3[i]+line4[i]
                if word == "XMAS" or word == "SAMX":
                    matches += 1
            except Exception as e:
                continue
    return matches

# Find diagonal nw_to_se matches
def generate_diagonal_nw_to_se(grid):
    matches = 0
    for i in range(len(grid) - 3):
        line1, line2, line3, line4 = grid[i], grid[i+1], grid[i+2], grid[i+3]
        for i in range(len(line1) - 3):
            try:
                word = line1[i]+line2[i+1]+line3[i+2]+line4[i+3]
                if word == "XMAS" or word == "SAMX":
                    matches += 1
            except Exception as e:
                continue
    return matches

# Find diagonal ne_to_sw matches
def generate_diagonal_ne_to_sw(grid):
    matches = 0
    for i in range(len(grid) - 3):
        line1, line2, line3, line4 = grid[i], grid[i+1], grid[i+2], grid[i+3]
        line1, line2, line3, line4 = list(reversed(line1)), list(reversed(line2)), list(reversed(line3)), list(reversed(line4))
        for i in range(len(line1) - 3):
            try:
                word = line1[i]+line2[i+1]+line3[i+2]+line4[i+3]
                if word == "XMAS" or word == "SAMX":
                    matches += 1
            except Exception as e:
                continue
    return matches

horizontal_matches = generate_horizontal(myfile)
print(f'Horizontal matches: {horizontal_matches}')

vertical_matches = generate_vertical(myfile)
print(f'Vertical matches: {vertical_matches}')

diagonal_nw_to_se_matches = generate_diagonal_nw_to_se(myfile)
print(f'Diagonal nw_to_se matches: {diagonal_nw_to_se_matches}')

diagonal_ne_to_sw_matches = generate_diagonal_nw_to_se(myfile)
print(f'Diagonal ne_to_sw matches: {diagonal_ne_to_sw_matches}')

total_matches = horizontal_matches + vertical_matches + diagonal_nw_to_se_matches + diagonal_ne_to_sw_matches
print(f'Total matches Part 1: {total_matches}')

print('************')

# Part 2 / 2

def find_matrix_match(matrix):
    #M S
    # A
    #M S
    if matrix[0][0] == 'M' and matrix[0][2] == 'S' and matrix[1][1] ==  'A' and matrix[2][0] == 'M' and matrix[2][2] == 'S':
        return True
    #S S
    # A
    #M M
    elif matrix[0][0] == 'S' and matrix[0][2] == 'S' and matrix[1][1] ==  'A' and matrix[2][0] == 'M' and matrix[2][2] == 'M':
        return True
    #M M
    # A
    #S S
    elif matrix[0][0] == 'M' and matrix[0][2] == 'M' and matrix[1][1] ==  'A' and matrix[2][0] == 'S' and matrix[2][2] == 'S':
        return True
    #S M
    # A
    #S M
    elif matrix[0][0] == 'S' and matrix[0][2] == 'M' and matrix[1][1] ==  'A' and matrix[2][0] == 'S' and matrix[2][2] == 'M':
        return True
    else:
        return False
    
def create_matrices_and_find_matches(grid):
    matches = 0
    for i in range(len(grid) - 2):
        line1, line2, line3 = grid[i], grid[i+1], grid[i+2]
        for i in range(len(line1) - 2):
            matrix = [list(line1[i:i+3]), list(line2[i:i+3]), list(line3[i:i+3])]
            if find_matrix_match(matrix):
                matches += 1
    return matches

print(f'Total matches part 2: {create_matrices_and_find_matches(myfile)}')