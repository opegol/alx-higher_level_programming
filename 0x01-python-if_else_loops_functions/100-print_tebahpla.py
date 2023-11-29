#!/usr/bin/python3
n = 0
for c in range(122, 96, -1):
    print("{}".format(chr(c - n)), end='')
    if n == 0:
        n += 32
    else:
        n = 0
