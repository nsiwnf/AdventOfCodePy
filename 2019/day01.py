filename = "inputs/2019_01.input"
file = open(filename, "r")

masses = list()
for line in file:
    masses.append(int(line))

fuel = 0
for mass in masses:
    fuel += int(mass / 3) - 2
print('Part 1:', fuel)

fuel = 0
for mass in masses:
    while mass > 8:
        mass = int(mass / 3) - 2
        fuel += mass
print('Part 2:', fuel)
