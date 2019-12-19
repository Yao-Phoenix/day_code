#!/usr/bin/env python3
'''
find all num of shuixianhua
'''
for num in range(100, 1000):
    number = 0
    low = num % 10 
    mid = num // 10 % 10
    high = num // 100
    number = low ** 3 + mid ** 3 + high ** 3
    if num == number:
        print(num)
