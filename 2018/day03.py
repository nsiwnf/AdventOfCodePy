filename = "inputs/2018_day3.input"
file = open(filename, "r")

import re

regex = "#\\d+ @ (\\d+),(\\d+): (\\d+)x(\\d+)"
n = 1000
grid = [[0] * n for i in range(n)]
for line in file:
    m = re.search(regex, line)
    x = int(m.group(1))
    y = int(m.group(2))

    w = int(m.group(3))
    h = int(m.group(4))

    for i in range(w):
        for j in range(h):
            grid[x + i][y + j] += 1

sum = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] > 1:
            sum += 1

# 98005
print "Part 1: ", sum

file.seek(0)
id = 0
for line in file:
    id += 1
    m = re.search(regex, line)
    x = int(m.group(1))
    y = int(m.group(2))
    endX = x + int(m.group(3))
    endY = y + int(m.group(4))
    isSingle = True
    for a in grid[x:endX]:
        isSingle &= len(filter(lambda c: c != 1, a[y:endY])) == 0
    if isSingle:
        # 331
        print "Part 2: ", id
        break
