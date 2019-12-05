#!python
import itertools
import re

def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

VOWELS = set('aeiou'[:])
TABOO  = set(['ab', 'cd', 'pq', 'xy'])

def is_nice(s):
    if len(list(filter(lambda c: c in VOWELS, s))) < 3:
        return False

    has_double = False

    for tup in pairwise(s):
        if tup[0] == tup[1]:
            has_double = True

        if tup[0] + tup[1] in TABOO:
            return False

    return has_double

def is_nice_bis(s):
    has_pairs = bool(re.search(r'([a-z]{2}).*\1', s))
    has_xyx = bool(re.search(r'(.).\1', s))
    return has_pairs and has_xyx


with open('day5.txt') as f:
    lines = [ line.strip() for line in f.readlines() ]
    total1 = len([ i for i in map(lambda l: is_nice(l), lines) if i ])
    total2 = len([ i for i in map(lambda l: is_nice_bis(l), lines) if i ])
    print(f'part 1: {total1}')
    print(f'part 2: {total2}')
