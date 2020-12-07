# it feels totally absurd there's not a more clever way to do this
def part1(target):
    houses = [0] * (target // 10)
    for elf in range(1, target // 10):
        for house in range(elf, target // 10, elf):
            houses[house] += elf * 10

        if houses[elf] >= target:
            return elf

def part2(target):
    top = target // 10
    houses = [0] * top

    def do_elf(elfnum):
        for house in range(elfnum, elfnum * 50 + 1, elfnum):
            if house >= top:
                return

            houses[house] += elfnum * 11

    for elf in range(1, top):
        do_elf(elf)

        if houses[elf] >= target:
            return elf

target = 34000000
print('part 1:', part1(target))
print('part 2:', part2(target))
