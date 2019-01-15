filename = "inputs/2018_day18.input"
file = open(filename, "r")


def set_next_value(set_y, set_x, ngrid, ogrid):
    new_val = ngrid[set_y][set_x]
    old_val = ogrid[set_y][set_x]
    if old_val == '.' and new_val % 100 >= 30:
        ngrid[set_y][set_x] = '|'
    elif old_val == '|' and new_val >= 300:
        ngrid[set_y][set_x] = '#'
    elif old_val == '#':
        if new_val / 100 > 0 and (new_val % 100) / 10 > 0:
            ngrid[set_y][set_x] = '#'
        else:
            ngrid[set_y][set_x] = '.'
    else:
        ngrid[set_y][set_x] = old_val

def count_wood_lumber(grid):
    w_count = 0
    l_count = 0
    for row in grid:
        w_count += row.count('|')
        l_count += row.count('#')
    return w_count * l_count

multiplier = {'.': 1, '|': 10, '#': 100}

grid = list()
for line in file:
    row = list(line.replace('\n', ''))
    grid.append(row)


minute = 10000
for m in range(minute):
    new_grid = [[0] * len(grid) for i in range(len(grid[0]))]
    if m == 10:
        # 763804
        print "Part1:", count_wood_lumber(grid)
    if m == 1028:
        # 188400
        print "Part2:", count_wood_lumber(grid)
        break
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            mult = multiplier[val]
            if y < len(grid) - 1:
                new_grid[y + 1][x] += mult
                if x > 0:
                    new_grid[y + 1][x - 1] += mult
                if x < len(row) - 1:
                    new_grid[y + 1][x + 1] += mult
            if x < len(row) - 1:
                new_grid[y][x + 1] += mult
            if x > 0:
                new_grid[y][x - 1] += mult
            if y > 0:
                new_grid[y - 1][x] += mult
                if x < len(row) - 1:
                    new_grid[y - 1][x + 1] += mult
                if x > 0:
                    new_grid[y - 1][x - 1] += mult
                    set_next_value(y - 1, x - 1, new_grid, grid)
                    if y == len(grid) - 1:
                        set_next_value(y, x - 1, new_grid, grid)
                    if x == len(row) - 1:
                        set_next_value(y - 1, x, new_grid, grid)
                        if y == len(row) - 1:
                            set_next_value(y, x, new_grid, grid)
    grid = new_grid
