#!python
import re

grid1 = { (x,y): False for x in range(1000) for y in range(1000) }
grid2 = { (x,y): 0 for x in range(1000) for y in range(1000) }

def parse_line(line):
    m = re.match(r'(.*?) (\d+),(\d+) through (\d+),(\d+)', line)
    action = m.group(1)
    x1 = int(m.group(2))
    y1 = int(m.group(3))
    x2 = int(m.group(4))
    y2 = int(m.group(5))

    return (action, x1, y1, x2, y2)

def run_line_1(line):
    (action, x1, y1, x2, y2) = parse_line(line)

    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if action == 'turn on':
                grid1[(x, y)] = True
            elif action == 'toggle':
                grid1[(x, y)] = not grid1[(x,y)]
            elif action == 'turn off':
                grid1[(x, y)] = False

def run_line_2(line):
    (action, x1, y1, x2, y2) = parse_line(line)

    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if action == 'turn on':
                grid2[(x, y)] += 1
            elif action == 'toggle':
                grid2[(x, y)] += 2
            elif action == 'turn off':
                grid2[(x, y)] = max(grid2[(x,y)] - 1, 0)

with open('day6.txt') as f:
    lines = [ line.strip() for line in f.readlines() ]

    for line in lines:
        run_line_1(line)
        run_line_2(line)

    print(list(grid1.values()).count(True))
    print(sum(grid2.values()))
