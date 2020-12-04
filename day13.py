from collections import defaultdict
import itertools
import re

# alice => { bob => 54, carol => -79 }
parser = re.compile(r'(\w+) would (gain|lose) (\d+).* next to (\w+)')

def calc(data):
    happiest = None

    for perm in itertools.permutations(data.keys()):
        people = list(perm)
        people.append(people[0])

        total = 0
        for i in range(0, len(people) - 1):
            a, b = people[i:i+2]
            total += data[a][b]
            total += data[b][a]

        if not happiest or total > happiest:
            happiest = total

    return happiest

with open('day13.txt') as f:
    lines = [ line.strip() for line in f.readlines() ]

    happiness = defaultdict(dict)

    for line in lines:
        match = parser.match(line)
        who, what, count, other = match.groups()
        val = int(count) if what == 'gain' else -1 * int(count)
        happiness[who][other] = val

    print(f'part 1: {calc(happiness)}')

    happiness['me'] = {}

    for k in happiness.keys():
        happiness[k]['me'] = 0
        happiness['me'][k] = 0

    print(f'part 2: {calc(happiness)}')
