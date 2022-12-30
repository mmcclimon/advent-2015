from collections import defaultdict


def do_it(instructions, a=0):
    registers = defaultdict(int)
    ptr = 0

    registers['a'] = a

    while True:
        if ptr >= len(instructions) or ptr < 0:
            break

        line = instructions[ptr]

        match line[0:3]:
            case 'hlf':
                reg = line[4]
                registers[reg] //= 2
                ptr += 1

            case 'tpl':
                reg = line[4]
                registers[reg] *= 3
                ptr += 1

            case 'inc':
                reg = line[4]
                registers[reg] += 1
                ptr += 1

            case 'jmp':
                offset = int(line[4:])
                ptr += offset

            case 'jie':
                reg = line[4]
                if registers[reg] % 2 == 0:
                    offset = int(line[7:])
                    ptr += offset
                else:
                    ptr += 1

            case 'jio':
                reg = line[4]
                if registers[reg] == 1:
                    offset = int(line[7:])
                    ptr += offset
                else:
                    ptr += 1

            case _:
                raise NotImplementedError(f"wat: {line}")

    return registers.get('b')


with open('day23.txt') as f:
    instructions = [line.strip() for line in f.readlines()]

print('part 1: ' + str(do_it(instructions, a=0)))
print('part 2: ' + str(do_it(instructions, a=1)))
