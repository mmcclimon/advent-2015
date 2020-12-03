from collections import defaultdict
import itertools

with open('day9.txt') as f:
    lines = [ line.strip() for line in f.readlines() ]

    # origin => { dest1 => dist, dest2 => dist }
    dists = defaultdict(dict)

    for line in lines:
        (src, _, dest, _, dist) = line.split(' ')
        dists[src][dest] = int(dist)
        dists[dest][src] = int(dist)

    shortest = None
    longest = None

    for perm in itertools.permutations(dists.keys()):
        cities = list(perm)
        dist = 0
        for i in range(0, len(cities) - 1):
            a, b = cities[i:i+2]
            dist += dists[a][b]

        if not shortest or dist < shortest:
            shortest = dist

        if not longest or dist > longest:
            longest = dist

    print(f"part 1: {shortest}")
    print(f"part 2: {longest}")
