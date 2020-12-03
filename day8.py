#!python
import re

with open('day8.txt') as f:
    lines = [ line.strip() for line in f.readlines() ]

    part1 = 0
    part2 = 0

    for line in lines:
        code_chars = len(line)

        # janky; we don't actually care what this evals to
        new = line[:]
        new = new.replace(r'\\', '/')
        new = new.replace(r'\"', '"')
        new = re.sub(r'\\x[0-9a-fA-F]{2}', '?', new)
        new = re.sub(r'^"|"$', '', new)

        s_chars = len(new)

        # part 2, a bit easier
        enc = line[:]
        enc = enc.replace('\\', '\\\\')
        enc = enc.replace(r'"', '\\"')
        enc_chars = len(enc)

        part1 += code_chars - s_chars
        part2 += enc_chars - code_chars + 2  # open/close quote

    print(f"part 1: {part1}")
    print(f"part 2: {part2}")
