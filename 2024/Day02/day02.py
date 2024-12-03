#https://adventofcode.com/2024/day/2

l1 = list()
with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.split()
        l = list()
        for li in line:
            l.append(int(li))
        l1.append(l)


def is_safe(report):
    ctr1 = 0
    ctr2 = 0
    ctr3 = 0
    for i in range(len(report)-1):
        if report[i] > report[i+1]:
            ctr1+=1
        if report[i] < report[i+1]:
            ctr2+=1
        if abs(report[i] - report[i+1]) <= 3:
            ctr3+=1
    increasing = ctr1 == len(report)-1
    decreasing = ctr2 == len(report)-1
    safe_differences = ctr3 == len(report)-1

    return (increasing or decreasing) and safe_differences


def w_dampener(report):
    ret = False
    for i in range(len(report)):
        new_rep = report[:i] + report[i+1:]
        if is_safe(new_rep):
            ret = True
            break

    return ret


sum1 = 0
sum2 = 0
for li in l1:
    if is_safe(li):
        sum1+=1
    if w_dampener(li):
        sum2+=1

print(f"Safe: {sum1}")
print(f"Safe w. Dampener: {sum2}")


