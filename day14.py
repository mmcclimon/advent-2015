from collections import defaultdict
import functools
import re

class Reindeer:
    def __init__(self, name, speed, move_t, rest_t):
        self.name = name
        self.speed = int(speed)
        self.move_t = int(move_t)
        self.rest_t = int(rest_t)
        self.points = 0

    @property
    def cycle_len(self):
        return self.move_t + self.rest_t

    def cycle_dist(self):
        return self.speed * self.move_t

    def pos_at_time(self, time):
        pos = (time // self.cycle_len) * self.cycle_dist()
        remaining = time % self.cycle_len
        if remaining >= self.move_t:
            pos += self.cycle_dist()
        else:
            pos += remaining * self.speed

        return pos

# lines = [
#     'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
#     'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.',
# ]

parser = re.compile(r'(\w+).*can fly (\d+) km/s for (\d+).*rest for (\d+)')
deer = []
lines = []

with open('day14.txt') as f:
    lines = [ line.strip() for line in f.readlines() ]

for line in lines:
    match = parser.match(line)
    who, speed, move_t, rest_t = match.groups()
    r = Reindeer(who, speed, move_t, rest_t)
    deer.append(r)

# part 1
part1 = functools.reduce(max, map(lambda d: d.pos_at_time(2503), deer))
print(f"part 1: {part1}")

# part 2: for every second, figure out who's in the lead, give them a point
for t in range(1, 2504):
    times = defaultdict(list)
    for d in deer:
        times[d.pos_at_time(t)].append(d)

    lead = max(times.keys())
    for d in times[lead]:
        d.points += 1

part2 = functools.reduce(max, map(lambda d: d.points, deer))
print(f"part 2: {part2}")
