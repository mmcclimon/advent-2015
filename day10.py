import functools

def hunkify(acc, elem):
    if len(acc) == 0 or acc[-1][0] != elem:
        acc.append(elem)
    else:
        acc[-1] = acc[-1] + elem
    return acc

def look_and_say(s):
    hunks = functools.reduce(hunkify, s, [])
    ret = []
    for hunk in hunks:
        ret.append(str(len(hunk)))
        ret.append(hunk[0])
    return ''.join(ret)

s = '1321131112'
for i in range(40):
    s = look_and_say(s)

print('part 1:', len(s))

for i in range(10):
    s = look_and_say(s)

print('part 2:', len(s))
