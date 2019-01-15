n = 300
serial = 4151

grid = [[0] * n for i in range(n)]
for x in range(n):
    rack_id = x + 1 + 10
    for y in range(n):
        pl = rack_id * (y + 1) + serial
        pl *= rack_id
        pl = pl / 100
        pl = pl % 10 - 5
        grid[y][x] = pl


def part1():
    max_sum = 0
    for y in range(n - 3):
        for x in range(n - 3):
            sum = grid[y][x] + grid[y + 1][x] + grid[y + 2][x]
            sum += grid[y][x + 1] + grid[y + 1][x + 1] + grid[y + 2][x + 1]
            sum += grid[y][x + 2] + grid[y + 1][x + 2] + grid[y + 2][x + 2]
            if max_sum < sum:
                max_sum = sum
    return max_sum


def part2():
    agg_array = [[0] * n for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(0, n):
            agg_array[i][j] = agg_array[i - 1][j] + grid[i - 1][j]

    res = (-1, -1, -1)

    max_so_far = -1
    for y in range(0, n):
        for bottom in range(y + 1, n + 1):
            sums = list()
            for i in range(n):
                sums.append(agg_array[bottom][i] - agg_array[y][i])

            # Find max square grid of this height (h) on this row (y)
            max_ending_here = 0
            h = bottom - y
            for x in range(h):
                max_ending_here += sums[x]
            for x in range(h, n):
                max_ending_here = max_ending_here - sums[x - h] + sums[x]

                if max_ending_here > max_so_far:
                    max_so_far = max_ending_here
                    res = ((x - h + 1) + 1, y + 1, h)
    return res


# Input (serial) : 4151
# 30
print "Part 1:", part1()

# 231,65,14
print "Part 2:", part2()
