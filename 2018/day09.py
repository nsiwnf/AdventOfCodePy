from collections import deque


def part1(num_players, last_marble):
    marbles = deque()
    marbles.append(0)
    players = [0] * num_players
    p_i = 0

    for m in range(last_marble):
        if (m + 1) % 23 == 0:
            players[p_i % num_players] += (m + 1)
            marbles.rotate(-7)
            players[p_i % num_players] += marbles.pop()
        else:
            marbles.rotate(2)
            marbles.append(m + 1)
        p_i += 1
    return max(players)


# 464 players; last marble is worth 71730 points
# 380705
print "Part1: ", part1(464, 71730)

# 3171801582
print "Part2: ", part1(464, 71730 * 100)
