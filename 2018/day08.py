filename = "inputs/2018_day8.input"
file = open(filename, "r")
data = file.read().replace('\n', '')
data = map(int, data.split(' '))


def get_meta(i, license):
    num_c = license[i]
    num_m = license[i + 1]
    if num_c == 0:
        i += 2
        meta = 0
        for m in license[i:i + num_m]:
            meta += m
        return meta, i + num_m
    else:
        total_meta = 0
        # index of first child
        next_index = i + 2
        for j in range(num_c):
            c_meta, next_index = get_meta(next_index, license)
            total_meta += c_meta
        for j in range(num_m):
            total_meta += license[next_index + j]

        return total_meta, next_index


def get_meta_non_recursive(license):
    # keep track of indices
    children = [0]
    meta = [1]
    meta_index = 2
    values = {0: license[0], 1: license[1]}

    total_meta = 0
    while len(children) > 0:
        c_i = children.pop()
        m_i = meta.pop()
        num_c = values[c_i]
        num_m = values[m_i]
        if num_c == 0:
            meta_index = m_i + 1 + num_m
            for m in license[m_i + 1:meta_index]:
                total_meta += m
        else:
            children.append(c_i)
            children.append(m_i)

            for j in range(num_m):
                total_meta += license[meta_index + j]


def part1(license):
    # return get_meta(0, license)[0]
    return get_meta_non_recursive(license)


data = map(int, "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split(' '))
print "Part1: ", part1(data)
