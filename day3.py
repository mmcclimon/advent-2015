#!python

def visit_route(route):
    visited = set()
    visited.add((0,0)) # always one to start

    x = y = 0

    for c in route:
        if   c == '>': x += 1
        elif c == '<': x -= 1
        elif c == '^': y += 1
        elif c == 'v': y -= 1
        else: raise Exception('wtf')

        visited.add((x, y))

    return len(visited)

def robo_visit(route):
    seen = set()

    santa_pos = [0,0]
    robo_pos = [0,0]

    seen.add(tuple(santa_pos))

    for (idx, c) in enumerate(route):
        which = santa_pos if idx % 2 == 0 else robo_pos

        if   c == '>': which[0] += 1
        elif c == '<': which[0] -= 1
        elif c == '^': which[1] += 1
        elif c == 'v': which[1] -= 1
        else: raise Exception('wtf')

        seen.add(tuple(which))

    return len(seen)

tests = ['^v', '^>v<', '^v^v^v^v^v']

# for t in tests:
#     print(robo_visit(t))

with open('day3.txt') as f:
    route = f.readline().strip()
    print(visit_route(route))
    print(robo_visit(route))
