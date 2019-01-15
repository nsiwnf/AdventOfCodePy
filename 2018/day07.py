filename = "inputs/2018_day7.input"
file = open(filename, "r")

import re
from collections import defaultdict

regex = "Step (.) must be finished before step (.) can begin"
nodes = {}
edges = list()
vertices = set()
for line in file:
    m = re.search(regex, line)
    n = m.group(1)
    c = m.group(2)

    vertices.add(n)
    vertices.add(c)
    edges.append((c, n))

waiting_on = defaultdict(list)
for k, v in edges:
    waiting_on[k].append(v)
roots = list(vertices.difference(waiting_on.keys()))

blocking_for = defaultdict(list)
for k, v in edges:
    blocking_for[v].append(k)

res = ""
completed = set()
while len(roots) != 0:
    roots.sort()
    current = roots[0]

    roots.remove(current)
    res += current
    completed.add(current)

    for p in blocking_for[current]:
        waiting_on[p] = filter(lambda x: x not in completed, waiting_on[p])
        if len(waiting_on[p]) == 0:
            roots.extend(p)

# OUGLTKDJVBRMIXSACWYPEQNHZF
print "Part1:", res
