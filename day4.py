#!python
import hashlib
import itertools

secret = b'iwrupvqb'
foundFirst = False

for n in itertools.count():
    k = hashlib.md5(secret + str(n).encode())

    if not foundFirst and k.hexdigest()[0:5] == '00000':
        foundFirst = True
        print(f'part 1: {n}')

    if k.hexdigest()[0:6] == '000000':
        print(f'part 2: {n}')
        break

