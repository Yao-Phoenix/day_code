#!/usr/bin/env python3
'''
Craps
Initial bet: 1000
Game over: 0 bet
'''

from random import randint

money = 1000
while money > 0:
    print('Your total assets: ', money)
    needs_go_on = True
    while True:
        debt = int(input('Please bet: '))
        if 0 < debt <= money:
            break
    while needs_go_on:
        needs_go_on = False
        first = randint(1, 6) + randint(1, 6)
        print('The player shakes out {} points.'.format(first))

        """
    if first == 7 or first == 11:
        print('Winner')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('Loser')
        money -+ debt
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('The player shakes out {} points.'.format(current))
        if current == 7:
            print('Loser')
            money -= debt
        elif current == first:
            print('Winner')
            money += debt
        else:
            needs_go_on = True
        """
        second = randint(1, 6) + randint(1, 6)
        print('The Bookmaker shakes out {} points'.format(second))
        if first > second:
            print('Winner')
            money += debt
        elif first < second:
            print('Loser')
            money -= debt
        else:
            needs_go_on = True
print('You are broke. Game Over!')
