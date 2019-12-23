#!/usr/bin/env python3
import os, time

def main():
    content = 'Welcome to Beijing......'
    while True:
        #clear output in screen
        os.system('clear') # os.system('clear')
        print(content)
        # sleep 200ms
        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()
