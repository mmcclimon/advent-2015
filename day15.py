lines = [
    'Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5',
    'PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1',
    'Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6',
    'Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8',
]

attrs = set(['capacity', 'durability', 'flavor', 'texture'])
ingredients = {}

for line in lines:
    (ing, rest) = line.split(': ')
    d = {}
    for s in rest.split(', '):
        (k, v) = s.split(' ')
        d[k] = int(v)

    ingredients[ing] = d

def attr_for(ing, key, amt):
    return ingredients[ing][key] * amt

def cookie_val(sp, pb, fr, su):
    total = 1
    for attr in attrs:
        attr_total = 0
        attr_total += attr_for('Sprinkles', attr, sp)
        attr_total += attr_for('PeanutButter', attr, pb)
        attr_total += attr_for('Frosting', attr, fr)
        attr_total += attr_for('Sugar', attr, su)

        total *= max(attr_total, 0)

    # calorie total
    calories = 0
    calories += attr_for('Sprinkles', 'calories', sp)
    calories += attr_for('PeanutButter', 'calories', pb)
    calories += attr_for('Frosting', 'calories', fr)
    calories += attr_for('Sugar', 'calories', su)

    return (total, calories)

# generate all combinations of 1-100 in groups of 4
part1 = 0
part2 = 0
for sp in range(101):
    for pb in range(101 - sp):
        for fr in range(101 - sp - pb):
            su = 100 - sp - pb - fr
            (this_val, cals) = cookie_val(sp, pb, fr, su)
            part1 = max(part1, this_val)
            if cals == 500:
                part2 = max(part2, this_val)

print(f'part 1: {part1}')
print(f'part 2: {part2}')
