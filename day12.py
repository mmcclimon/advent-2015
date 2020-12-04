import functools
import json

def sum_nums(data, acc, ignore_red=False):
    if isinstance(data, dict):
        old_acc = acc
        for val in data.values():
            if ignore_red and val == 'red':
                return old_acc

            acc = sum_nums(val, acc, ignore_red)

        return acc

    elif isinstance(data, list):
        for elem in data:
            acc = sum_nums(elem, acc, ignore_red)
        return acc

    elif isinstance(data, str):
        return acc  # nothing to do

    elif isinstance(data, int):
        return acc + data

    raise RuntimeError('wat')

with open('day12.txt') as f:
    data = json.load(f)
    print('part 1:', sum_nums(data, 0))
    print('part 2:', sum_nums(data, 0, True))

