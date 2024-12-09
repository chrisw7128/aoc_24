from pprint import pprint

with open('day_2_input.txt') as fin:
    myfile = fin.readlines()

# Part 1/2

def refactor_reports(reports):
    for i in range(len(reports)):
        reports[i] = reports[i].split()
    for report in reports:
        for i in range(len(report)):
            report[i] = int(report[i])
    return reports

reports = refactor_reports(myfile)

def check_ascending(report):
    return all(report[i] < report[i+1] for i in range(len(report) - 1))

def check_descending(report):
    return all(report[i] > report[i+1] for i in range(len(report) - 1))

def check_step(report):
    return all(abs(report[i] - report[i+1]) <= 3 for i in range(len(report) - 1))

def find_num_of_correct_reports(reports):
    part_1_correct_reports = 0
    part_2_correct_reports = 0
    for report in reports:
        ascending = check_ascending(report)
        descending = check_descending(report)
        step_3 = check_step(report)
        if (ascending and step_3) or (descending and step_3):
            part_1_correct_reports += 1
        # Part 2/2 - if a report was unsafe in part 1, see if it can become safe via the Problem Dampener
        else:
            for i in range(len(report)):
                step_2_report = report[:i] + report[i + 1:]
                ascending_2 = check_ascending(step_2_report)
                descending_2 = check_descending(step_2_report)
                step_3_2 = check_step(step_2_report)
                if (ascending_2 and step_3_2) or (descending_2 and step_3_2):
                    part_2_correct_reports += 1
                    break
    return part_1_correct_reports, part_2_correct_reports

part_1_correct_reports, part_2_correct_reports = find_num_of_correct_reports(reports)

print(f'Part 1 correct reports: {part_1_correct_reports}')
print(f'Part 2 correct reports: {part_2_correct_reports}')
print(f'Total correct reports: {part_1_correct_reports + part_2_correct_reports}')