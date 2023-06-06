#!/usr/bin/python3
for a in range(10):
    for b in range(a + 1, 10):
        print("{}".format(a) + "{}".format(b), end=(', ' if (a < 8 or (a == 8 and b < 9)) else '\n'))
