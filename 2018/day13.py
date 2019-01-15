filename = "inputs/2018_day13.input"
file = open(filename, "r")

north = (0, -1)
south = (0, 1)
east = (1, 0)
west = (-1, 0)

left = 0
straight = 1
right = 2

moves = {
    (north, '+', left): (west, straight), (north, '+', straight): (north, right), (north, '+', right): (east, left),
    (north, '\\', left): (west, left), (north, '\\', straight): (west, straight), (north, '\\', right): (west, right),
    (north, '/', left): (east, left), (north, '/', straight): (east, straight), (north, '/', right): (east, right),

    (south, '+', left): (east, straight), (south, '+', straight): (south, right), (south, '+', right): (west, left),
    (south, '\\', left): (east, left), (south, '\\', straight): (east, straight), (south, '\\', right): (east, right),
    (south, '/', left): (west, left), (south, '/', straight): (west, straight), (south, '/', right): (west, right),

    (east, '+', left): (north, straight), (east, '+', straight): (east, right), (east, '+', right): (south, left),
    (east, '\\', left): (south, left), (east, '\\', straight): (south, straight), (east, '\\', right): (south, right),
    (east, '/', left): (north, left), (east, '/', straight): (north, straight), (east, '/', right): (north, right),

    (west, '+', left): (south, straight), (west, '+', straight): (west, right), (west, '+', right): (north, left),
    (west, '\\', left): (north, left), (west, '\\', straight): (north, straight), (west, '\\', right): (north, right),
    (west, '/', left): (south, left), (west, '/', straight): (south, straight), (west, '/', right): (south, right)
}

track = []
# y, x, direction, turn
carts = {}
y = 0
for line in file:
    row = list(line.replace('\n', ''))
    for x, c in enumerate(row):
        if c == '<':
            row[x] = '-'
            carts[(y, x)] = (west, left)
        elif c == '>':
            row[x] = '-'
            carts[(y, x)] = (east, left)
        elif c == '^':
            row[x] = '|'
            carts[(y, x)] = (north, left)
        elif c == 'v':
            row[x] = '|'
            carts[(y, x)] = (south, left)
    y += 1
    track.append(row)

first_crash = True
while len(carts) > 1:
    new_carts = {}
    for (y, x) in sorted(carts):
        cur_cart = carts[(y, x)]
        ny = y + cur_cart[0][1]
        nx = x + cur_cart[0][0]
        if carts.get((ny, nx)) is not None or new_carts.get((ny, nx)) is not None:
            if first_crash:
                print "Part1:", nx, ny
                first_crash = False
        else:
            cur_location = track[y][x]
            new_location = track[ny][nx]
            next_cart = moves.get((cur_cart[0], new_location, cur_cart[1]))
            if next_cart is None:
                next_cart = carts[(y, x)]
            new_carts[(ny, nx)] = next_cart
    carts = new_carts

print "Part2:", carts.keys()[0]

# Part 1 : 108,60
# Part 2 : 92,42
