#!/usr/bin/python3
for x in range(0, 8):
    for y in range(0, 10):
        if x < y:
            print("{0:02}".format(x * 10 + y), end=', ')
print("{}".format(89))
