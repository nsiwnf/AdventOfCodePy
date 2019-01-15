filename = "inputs/2018_day23.input"
file = open(filename, "r")

lines = list()
for line in file:
    lines.append(line)

lines = sorted(lines)

import re
import matplotlib.pyplot as plt
import numpy as np

regex = "pos=<(-*\\d+),(-*\\d+),(-*\\d+)>, r=(\\d+)"
xs = list()
ys = list()
zs = list()
rs = list()

for line in lines:
    m = re.search(regex, line)
    x = int(m.group(1))
    y = int(m.group(2))
    z = int(m.group(3))
    r = int(m.group(4))

    xs.append(x)
    ys.append(y)
    zs.append(z)
    rs.append(r/10000000.0)
    # rs.append(r)

area = [2.2**n for n in rs]
plt.scatter(xs,ys,s=area, c=zs, alpha=0.25)
plt.plot(xs, ys, 'ko')
plt.plot([15300000], [24800000], 'wo')

# plt.axis([-50, 250, -50, 250])

plt.show()

