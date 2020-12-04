import re

MAX_CHAR = ord('z')
start = 'hxbxwxba'

bad_re = re.compile(r'[iol]')
double_re = re.compile(r'([a-z])\1.*([a-z])\2')

def pw_ok(pw):
    # 8 chars, yo
    if len(pw) != 8:
        return False

    # condition 2: no i, o, or l
    if bad_re.search(pw):
        return False

    # condition 3: pair of double letters
    if not double_re.search(pw):
        return False

    # condition 1: consecutive letters
    ords = list(map(ord, pw))
    for i in range(6):
        if ords[i+1] == ords[i] + 1 and ords[i+2] == ords[i] + 2:
            return True

    return False


def next_pw(pw):
    chars = list(map(ord, pw))
    i = len(chars) - 1
    chars[i] += 1   # bump last char

    # if it was z, bump it to a, knock back to next char
    while i > 0 and chars[i] > MAX_CHAR:
        chars[i] = ord('a')
        i -= 1
        chars[i] += 1

    if chars[i] > MAX_CHAR and i == 0:
        chars[i] = 0

    return ''.join(map(chr, chars))

def next_valid_pw(pw):
    pw = next_pw(pw)

    while not pw_ok(pw):
        pw = next_pw(pw)

    return pw


part1 = next_valid_pw(start)
print(f'part 1: {part1}')

part2 = next_valid_pw(part1)
print(f'part 2: {part2}')
