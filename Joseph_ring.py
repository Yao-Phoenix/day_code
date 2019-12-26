#!/usr/bin/env python3
'''
<幸运的基督徒>
有15个基督徒和15个非基督徒在海上遇险, 必须扔15人才能存活,围成圈, 由某人开始报1, 报9扔,
之后循环直至剩15人, 基督徒全活, 问他们如何站, 哪些是基督徒, 哪些不是
'''

def main():
    persons = [True] * 30
    counter, number, index = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end = '')

if __name__ == '__main__':
    main()
