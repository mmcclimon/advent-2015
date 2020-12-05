import re

want = {
    'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
    'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1,
}

def parse(data):
    ret = {}
    for hunk in data.split(', '):
        k, v = hunk.split(': ')
        ret[k] = int(v)

    return ret

def is_match_part_1(data):
    for (k, v) in data.items():
        if v != want[k]:
            return False

    return True

def is_match_part_2(data):
    for k in want.keys():
        if k not in data:
            continue

        val = data[k]
        if k == 'cats' or k == 'trees':
            if val <= want[k]:
                return False
        elif k == 'pomeranians' or k == 'goldfish':
            if val >= want[k]:
                return False
        else:
            if val != want[k]:
                return False

    return True

with open('day16.txt') as f:
    part1 = None
    part2 = None
    parser = re.compile(r'Sue (\d+): (.*)')
    lines = [ line.strip() for line in f.readlines() ]

    for line in lines:
        match = parser.match(line)
        (sue, rest) = match.groups()
        data = parse(rest)

        if is_match_part_1(data):
            part1 = sue

        if is_match_part_2(data):
            part2 = sue

    print(f'part1: {part1}')
    print(f'part2: {part2}')
