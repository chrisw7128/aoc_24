from pprint import pprint

with open('data_5.txt') as fin:
    myfile = fin.readlines()

# Clean the data to make a dict of the rules
def clean_rules(list_of_rules):
    # rules = [rule.strip('\n').split('|') for rule in list_of_rules[0:1176]]
    rules = [rule.strip('\n').split('|') for rule in list_of_rules[0:21]]
    for i in range(len(rules)):
        for j in range(len(rules[i])):
            rules[i][j] = int(rules[i][j])
    rules_dict = {}
    for rule in rules:
        if rule[0] in rules_dict:
            rules_dict[rule[0]].append(rule[1])
        else:
            rules_dict[rule[0]] = [rule[1]]
    return rules_dict

rules_dict = clean_rules(myfile)


# Clean the data to make a list of the proposed updates
# updates = [update.strip('\n').split(',') for update in myfile[1177:]]
updates = [update.strip('\n').split(',') for update in myfile[22:]]
for i in range(len(updates)):
    for j in range(len(updates[i])):
        updates[i][j] = int(updates[i][j])


pprint(rules_dict)
pprint(updates)


for update in updates:
    for page in update:
        if page in rules_dict:
            pass
        else:
            continue


# def format_rules(list_of_rules):
#     rules = [rule.strip('\n').split('|') for rule in list_of_rules[0:21]]
#     for i in range(len(rules)):
#         for j in range(len(rules[i])):
#             rules[i][j] = int(rules[i][j])
#     return rules

# formatted_rules = format_rules(myfile)

# def sort_rules(list_of_formatted_rules):
#     sorted_rules = []
#     for rule in list_of_formatted_rules:
#         index = list_of_formatted_rules.index(rule)
#         if rule[0] not in sorted_rules and rule[1] not in sorted_rules:
#             sorted_rules.append(rule[0], rule[1])
#         elif rule[0] in sorted_rules and rule[1] not in sorted_rules:
#             sorted_rules.insert(index, rule[1])
#         elif rule[0] not in sorted_rules and rule[1] in sorted_rules:
#             sorted_rules.insert(index, rule[0])
#         elif rule[0] not in sorted_rules and rule[1] not in sorted_rules:
#             sorted_rules.append(rule[0], rule[1])
#     return sorted_rules

# sorted_rules = sort_rules(formatted_rules)
# print(sorted_rules)