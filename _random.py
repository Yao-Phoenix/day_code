#!/usr/bin/env python3
import random 

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('Please enter a number: '))
    if number < answer:
        print('Please enter bigger number.')
    elif number > answer:
        print('Please enter smaller number.')
    else:
        print('Congratulations!')
        break
print('You guessed {} times in total'.format(counter))
if counter > 7:
    print('Your IQ balance is clearly insufficient')
