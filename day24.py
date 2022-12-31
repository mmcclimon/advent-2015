from functools import reduce
from itertools import combinations
import operator


with open('day24.txt') as f:
    weights = [int(line.strip()) for line in f.readlines()]


def do_groups(num_groups):
    need = sum(weights) // num_groups

    for i in range(2, len(weights)):
        qes = [reduce(operator.mul, c) for c in combinations(weights, i)
               if sum(c) == need]

        if qes:
            return min(qes)


print(f"part 1: {do_groups(3)}")
print(f"part 2: {do_groups(4)}")
