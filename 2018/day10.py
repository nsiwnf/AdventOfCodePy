filename = "inputs/2018_day10.input"
file = open(filename, "r")

import re

import numpy

regex = "position=<([\\- ]\\d+), ([- ]\\d+)> velocity=<([- ]\\d+), ([- ]\\d+)"
xs = list()
ys = list()
vxs = list()
vys = list()
maxX = -1
minX = 1000000
maxY = -1
minY = 1000000
for line in file:
    m = re.search(regex, line)
    x = int(m.group(1))
    y = int(m.group(2))
    xs.append(x)
    ys.append(y)
    maxX = max(maxX, x)
    maxY = max(maxY, y)
    minX = min(minX, x)
    minY = min(minY, y)

    vx = int(m.group(3))
    vy = int(m.group(4))
    vxs.append(vx)
    vys.append(vy)

xs = numpy.array(xs)
ys = numpy.array(ys)
vxs = numpy.array(vxs)
vys = numpy.array(vys)
area = 549
minArea = (maxX - minX) * (maxY - minY)
while (maxX - minX) * (maxY - minY) > area:
    xs = xs + vxs
    ys = ys + vys
    maxX = max(xs)
    maxY = max(ys)
    minX = min(xs)
    minY = min(ys)
    minArea = min(minArea, (maxX - minX) * (maxY - minY))



print minArea

# 98005
print "Part 1: "
