#!/usr/bin/env python3
import sys
def get_suffix(filename, has_dot=False):
    '''
    Get suffix of file

    :param filename: filename
    :param has_dot: Do the returned suffix names need to be dotted
    :return: suffix
    '''
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

if __name__ == '__main__':
    print(get_suffix(sys.argv[1]))
