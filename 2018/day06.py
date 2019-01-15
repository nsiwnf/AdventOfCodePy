filename = "inputs/2018_day6.input"
file = open(filename, "r")

import re

regex = "(\\d+), (\\d+)"


def find_closest(y, x, distances):
    distance = -1
    c = -1
    for i, d in enumerate(distances):
        dc = abs(x - d[0]) + abs(y - d[1])
        if dc < distance or distance == -1:
            c = i
            distance = dc
        elif dc == distance:
            c = -1
    return c


top = -1
bottom = -1
left = -1
right = -1

distances = list()
for line in file:
    m = re.search(regex, line)
    x = int(m.group(1))
    y = int(m.group(2))
    distances.append((x, y))

    if top > y or top == -1:
        top = y
    if bottom < y:
        bottom = y
    if right < x:
        right = x
    if left > x or left == -1:
        left = x

area = [0] * len(distances)
for row in range(top, bottom):
    for col in range(left, right):
        c = find_closest(row, col, distances)
        if c != -1:
            area[c] += 1

# Check unchanged
area2 = [0] * len(distances)
for row in range(bottom * 2):
    for col in range(right * 2):
        c = find_closest(row, col, distances)
        if c != -1:
            area2[c] += 1
            if area2[c] > area[c]:
                area[c] = 0

# 4284
print "Part1: ", max(area)

total = 0
for row in range(top, bottom):
    for col in range(left, right):
        t = reduce(lambda a, b: a + b, map(lambda (r, c): abs(col - c) + abs(row - r), distances))
        if t < 10000:
            total += 1

# 35490
print "Part2: ", total
