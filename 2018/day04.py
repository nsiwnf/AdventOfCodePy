filename = "inputs/2018_day4.input"
file = open(filename, "r")

import re

regex = "\\[\\d+-\\d+-\\d+ \\d+:(\\d+)] .\\w+ .(\\d*)"
sched = {}

lines = []
for line in file:
    lines.append(line)
lines = sorted(lines)

id = -1
minFalls = -1
for line in lines:
    m = re.search(regex, line)
    if "Guard" in line:
        id = int(m.group(2))
    elif "falls" in line:
        minFalls = int(m.group(1))
    else:
        minWakes = int(m.group(1))
        if id not in sched:
            sched[id] = [0]*60
        minutesAsleep = sched[id]
        for i in range(minFalls, minWakes):
            minutesAsleep[i] += 1

maxAsleepOnMinute = 0
maxTotaTimeAsleep = 0
maxAOMGuard = -1
maxAOMMin = -1
maxTTAGuard = -1
maxTTAMin = -1
for guardId in sched:
    minutesAsleep = sched[guardId]
    sum = 0
    maxTTAminValue = -1
    maxTTAminKey = -1
    for minute, minuteValue in enumerate(minutesAsleep):
        sum += minuteValue
        if minuteValue > maxAsleepOnMinute:
            maxAsleepOnMinute = minuteValue
            maxAOMMin = minute
            maxAOMGuard = guardId
        if minuteValue > maxTTAminValue:
            maxTTAminValue = minuteValue
            maxTTAminKey = minute
    if sum > maxTotaTimeAsleep:
        maxTotaTimeAsleep = sum
        maxTTAMin = maxTTAminKey
        maxTTAGuard = guardId

# 36898
print "Part 1 : ", maxTTAGuard * maxTTAMin
# 80711
print "Part 2 : ", maxAOMGuard * maxAOMMin


