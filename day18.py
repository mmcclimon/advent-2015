class Grid:
    def __init__(self, lines):
        char = lambda c: c == '#'
        self.grid = [ [ char(c) for c in line] for line in lines]

    def __str__(self):
        unchar = lambda b: '#' if b else '.'
        lines = [''.join(map(unchar, line)) for line in self.grid]

        return "\n".join(lines)

    def _neighbors_on(self, row, col):
        total = 0
        for x in range(row - 1, row + 2):
            for y in range(col - 1, col + 2):
                if x < 0 or y < 0:
                    continue
                if x == row and y == col:
                    continue

                try:
                    point = self.grid[x][y]
                    if point:
                        total += 1
                except IndexError:
                    pass

        return total

    def num_on(self):
        return len(list(filter(bool, [el for row in self.grid for el in row])))


    def step(self, part2=False):
        to_falsify = []
        to_truthify = []
        for (i, row) in enumerate(self.grid):
            for (j, is_on) in enumerate(row):
                num = self._neighbors_on(i, j)
                if is_on and (num < 2 or num > 3):
                    to_falsify.append((i, j))
                elif not is_on and num == 3:
                    to_truthify.append((i, j))

        if part2:
            x = len(self.grid) - 1
            y = len(self.grid[0]) - 1
            to_truthify.extend([(0, 0), (0, y), (x, 0), (x, y)])

        for (i, j) in to_falsify:
            self.grid[i][j] = False
        for (i, j) in to_truthify:
            self.grid[i][j] = True

with open('day18.txt') as f:
    lines = [ line.strip() for line in f.readlines() ]

    for part2 in [False, True]:
        g = Grid(lines)
        for _ in range(100):
            g.step(part2)

        part = 2 if part2 else 1
        print(f'part {part}: {g.num_on()}')
