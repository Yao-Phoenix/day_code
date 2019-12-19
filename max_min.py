#!/usr/bin/env python3

x = int(input('x=: '))
y = int(input('y=: '))
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('{} and {} of max is {}'.format(x, y, factor))
        print('{} and {} of min is {}'.format(x, y, x * y // factor))
        break
