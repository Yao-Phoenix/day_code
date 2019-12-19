#!/usr/bin/env python3

for x in range(0, 21):
    for y in range(0, 34):
        z = 100 - x - y
        if x * 5 + y * 3 + z / 3 == 100:
            print('Cock: {}, hen: {}, Chicken: {}'.format(x, y, z))
