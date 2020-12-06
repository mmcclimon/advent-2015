import re
from collections import defaultdict

repl = defaultdict(list)
rev = {}
lines = []
start = ''

with open('day19.txt') as f:
    lines = [ line.strip() for line in f.readlines() ]
    start = lines.pop()

atoms = list(filter(lambda a: len(a) > 0, re.split(r'([A-Z][a-z]?)', start)))

for line in lines:
    if len(line) == 0:
        continue
    l, r = line.split(' => ')
    repl[l].append(r)
    rev[r] = l

# part 1
# for every atom, insert all its replacements into the set
distinct = set()
for (idx, el) in enumerate(atoms):
    head = ''.join(atoms[0:idx])
    tail = ''.join(atoms[idx+1:])

    for r in repl[el]:
        distinct.add(head + r + tail)

print('part 1:', len(distinct))


# part 2: store a reverse mapping, iteratively replace longest string
keys = list(rev.keys())
keys.sort(key=len, reverse=True)

cur = start
part2 = 0

while cur != 'e':
    for k in keys:
        if k in cur:
            cur = cur.replace(k, rev[k], 1)
            part2 += 1

print('part 2:', part2)

