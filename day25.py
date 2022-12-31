val = 20151125
max_row = 1
row = 1
col = 1

while True:
    if row == 3010 and col == 3019:
        print(f"at 3010,3019: {val}")
        break

    val = (val * 252533) % 33554393
    col += 1
    row -= 1

    if row == 0:
        col = 1
        max_row += 1
        row = max_row
