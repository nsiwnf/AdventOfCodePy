filename = "inputs/2018_day12.input"
file = open(filename, "r")

import re


def count_pots(state, zero_idx):
    sum_of_pots = 0
    for k, v in enumerate(state):
        if v == '#':
            sum_of_pots += k - zero_idx
    return sum_of_pots


regex = "(.....) => (.)"
conversions = {}

initial_state = "##....#.#.#...#.#..#.#####.#.#.##.#.#.#######...#.##....#..##....#.#..##.####.#..........#..#...#"

for line in file:
    m = re.search(regex, line)
    x = m.group(1)
    y = m.group(2)
    conversions[x] = y

state = initial_state
zero_index = 0
for i in range(20):
    # pad with empty pots
    if not state.startswith("....."):
        state = "..." + state
        zero_index += 3
    if not state.endswith("....."):
        state = state + "..."

    new_state = ""
    for s in range(2, len(state) - 2):
        section = state[s - 2:s + 3]
        if section in conversions:
            new_state += conversions[section]
        else:
            new_state += '.'
    state = new_state
    zero_index -= 2

# 2349
print "Part 1: ", count_pots(state, zero_index)

# 98005
