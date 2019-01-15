filename = "inputs/2018_day5.input"
file = open(filename, "r")

data = file.read().replace('\n', '')

# matches = [(chr(i) + chr(i - 32)) for i in range(ord('a'), ord('z') + 1)]
delta = ord('a') - ord('A')


def reducedata(string, skip):
    result = list()
    for c in string:
        if len(result) == 0:
            result.append(c)
        elif c not in skip:
            p = result.pop()
            if ord(c) - ord(p) != delta and ord(p) - ord(c) != delta:
                result.append(p)
                result.append(c)
    return result


# 9704
reduce_data = reducedata(data, "")
print "Part1 :", len(reduce_data)

smallest = len(reduce_data)
for i in range(ord('a'), ord('z') + 1):
    reduce_data = reducedata(data, chr(i) + chr(i - 32))
    if len(reduce_data) < smallest:
        smallest = len(reduce_data)

# 6942
print "Part2 :", smallest
