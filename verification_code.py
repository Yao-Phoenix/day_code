#!/usr/bin/env python3
import random

def generate_code(code_len=4):
    '''
    Generate verification code of specified length
    
    :param code_len: Verification code length (default 4 characters)

    :return: Random verification code composed of uppercase and lowercase \
            English letters and numbers
    '''
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code
if __name__ == '__main__':
    generate_code()

