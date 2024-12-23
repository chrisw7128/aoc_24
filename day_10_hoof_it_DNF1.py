from pprint import pprint

def load_data():
    with open('data_10_2.txt') as fin:
        myfile = [list(map(int, line.strip())) for line in fin.readlines()]
    return myfile

topo = load_data()

def get_topo_shape():
    topo = load_data()
    data_rows = len(topo)
    data_cols = len(topo[0])
    return data_rows, data_cols

data_rows, data_cols = get_topo_shape()
print(f'data rows: {len(topo)}')
print(f'data cols: {len(topo[0])}')

pprint(topo)

def find_trailheads():
    topo = load_data()
    trailheads = []
    for i in range(len(topo)):
        for j in range(len(topo[i])):
            if topo[i][j] == 0:
                trailheads.append((i, j))
    return trailheads

trailheads = find_trailheads()
print(f'trailheads (topo value = 0): {trailheads}')

def check_locations(current_location, current_value):
    places_to_explore = {
        'up': (current_location[0] - 1, current_location[1]),
        'down': (current_location[0] + 1, current_location[1]),
        'left': (current_location[0], current_location[1] - 1),
        'right': (current_location[0], current_location[1] + 1)
        }
    explored_locations = []
    matched_locations = []
    for item in places_to_explore:
        new_location = topo[places_to_explore[item][0]][places_to_explore[item][1]]
        print(f'new location: {new_location}')
        if new_location != (current_value + 1) and new_location[0] <= len(data_rows - 1) and new_location[1] <= len(data_cols - 1):
            explored_locations.append(places_to_explore[item])
        else:
            matched_locations.append(places_to_explore[item])
    print(f'{current_location} explored locations: {explored_locations}')
    print(f'{current_location} matched locations: {matched_locations}')
    return explored_locations, matched_locations

for trailhead in trailheads:
    explored_locations, matched_locations = check_locations(trailhead, 0)