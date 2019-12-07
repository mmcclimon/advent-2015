#!python
from collections import deque

def resolve(raw, w):
    return int(raw) if raw.isdigit() else w[raw]

def resolve_instruction(inst, w):
    words = inst.split(' ')

    if len(words) == 1:
        return resolve(words[0], w)

    # NOT
    if len(words) == 2:
        return (~resolve(words[1], w)) % 2**16

    (x, op, y) = resolve(words[0], w), words[1], resolve(words[2], w)

    if op == 'AND':
        return (x & y) % 2**16
    if op == 'OR':
        return (x | y) % 2**16
    if op == 'LSHIFT':
        return (x << y) % 2**16
    if op == 'RSHIFT':
        return (x >> y) % 2**16

def run(instructions, wires):
    while len(instructions):
        (instruction, output) = instructions[0].split(' -> ')
        try:
            wires[output] = resolve_instruction(instruction, wires)
            instructions.popleft()
        except KeyError:
            # dumb solution: if we can't resolve this instruction, push it
            # onto the end and deal with later
            instructions.rotate()

    return wires


with open('day7.txt') as f:
    lines = [ line.strip() for line in f.readlines() ]

    d1 = deque(lines)
    w1 = run(d1, {})
    print(w1['a'])

    d2 = deque(lines)
    w2 = run(d2, {'b': w1['a']})
    print(w2['a'])
