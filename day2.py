#!python
from functools import reduce


def calc(dimensions):
    (l, w, h) = sorted(map(lambda n: int(n), dimensions.split("x")))

    # by convention, l*w will be the smallest, so add that again as slack
    paper = 2*l*w + 2*w*h + 2*h*l + (l*w)
    ribbon = 2*l + 2*w + (l*w*h)

    return (paper, ribbon)

with open("day2.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    (paper, ribbon) = reduce(
        lambda acc, pair: (acc[0] + pair[0], acc[1] + pair[1]),
        (map(lambda s: calc(s), lines)),
    )
    print(f'part 1: {paper}')
    print(f'part 2: {ribbon}')
