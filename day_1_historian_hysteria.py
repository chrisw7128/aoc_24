with open('day_1_input.txt') as fin:
    myfile = fin.readlines()

# Part 1/2

all_coords = [pair.split() for pair in myfile]
[first_list] = [sorted(int(coord[0]) for coord in all_coords)]
[second_list] = [sorted(int(coord[1]) for coord in all_coords)]


def find_total_distance(list1, list2):
    total_distance = 0
    for i in range(1000):
        distance = abs(list1[i] - list2[i])
        total_distance += distance
    return total_distance

total_distance = find_total_distance(first_list, second_list)
print(f'The total distance is {total_distance}')

# Part 2/2

from collections import Counter

count_in_second_list = Counter(second_list)

def find_similarity_score(list1, counter1):
    similarity_score = 0
    for coord in list1:
        if counter1[coord]:
            similarity_score += coord*counter1[coord]
    return similarity_score

similarity_score = find_similarity_score(first_list, count_in_second_list)
print(f'The similarity score is {similarity_score}')