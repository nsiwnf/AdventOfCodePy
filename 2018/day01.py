filename = "inputs/2018_day1.input"
file = open(filename, "r")

frequencies = list()
f = 0
for line in file:
    l = int(line)
    frequencies.append(l)
    f += l
print "Part1 :", f

f = 0
seen = set()
i = 0
while f not in seen:
    seen.add(f)
    f += frequencies[i]
    i = (i + 1)% len(frequencies)
print "Part2 :", f
