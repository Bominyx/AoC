#https://adventofcode.com/2024/day/1

l1 = list()
l2 = list()

with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        li1, li2 = line.split()
        l1.append(int(li1))
        l2.append(int(li2))

l1.sort()
l2.sort()

sum1 = 0
for li1, li2 in zip(l1,l2):
    if li1 > li2:
        sum1 += li1 - li2
    else:
        sum1 += li2 - li1

print(f"Distance:  {sum1}")


sum2 = 0
for li1 in l1:
    ctr = 0
    for li2 in l2:
        if li1 == li2:
            ctr += 1
    sum2 += (ctr * li1)

print(f"Similarity:  {sum2}")
