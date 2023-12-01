#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv

    argc = len(argv) - 1
    sum = 0
    for i in range(argc):
        sum += int(argv[i + 1])
    print("{}".format(sum))
