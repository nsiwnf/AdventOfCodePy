filename = "inputs/2018_day2.input"
file = open(filename, "r")

import collections

def reduce_my_chars(x, y):
    if x == y:
        return x
    else:
        return ''

cntr = collections.Counter()
two_ct = 0
tre_ct = 0
lines = []
for line in file:
    lines.append(line)
    cntr.update(line)
    values = cntr.values()
    if 2 in values:
        two_ct += 1
    if 3 in values:
        tre_ct += 1
    cntr.clear()

# 4980
print "Part 1: ", (tre_ct * two_ct)

# qysdtrkloagnfozuwujmhrbvx
for ai in range(len(lines)):
    a = lines[ai]
    for b in lines[ai+1:]:
        c = ''.join(map(reduce_my_chars, a, b))
        odd_ct = len(a) - len(c)
        if odd_ct == 1:
            print "Part 2: ", c

