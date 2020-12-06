import itertools
from collections import defaultdict

target = 150
sizes = [ 33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42 ]

totals = defaultdict(int)

for i in range(len(sizes)):
    for combo in itertools.combinations(sizes, i):
        if sum(combo) == target:
            totals[len(combo)] += 1

key = min(totals.keys())

part1 = sum(totals.values())
part2 = totals[key]
print(f'part 1: {part1}')
print(f'part 2: {part2}')
