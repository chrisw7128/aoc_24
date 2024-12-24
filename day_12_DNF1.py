def load_data():
    with open('data_12.txt') as fin:
        myfile = [list(map(str, item.strip())) for item in fin.readlines()]
    return myfile

def load_test_data():
    return [
        ['A', 'A', 'A', 'A'],
        ['B', 'B', 'C', 'D'],
        ['B', 'B', 'C', 'C'],
        ['E', 'E', 'E', 'C']
    ]

garden = load_data()
test_garden = load_test_data()
print(garden)
print(len(garden))
print(len(garden[0]))

print(test_garden)
print(len(test_garden))
print(len(test_garden[0]))

def define_sections(data):
    # search for connecting horizontal or vertical indexes
    pass

