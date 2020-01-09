from threading import Thread
from random import randint
from time import time, sleep

def download_task(filename):
    print('开始下载{}...'.format(filename))
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('{}下载完成! 总共耗费了{}s'.format(filename, time_to_download))

def main():
    start = time()
    t1 = Thread(target=download_task, args=('Python从入门到住院.pdf', ))
    t1.start()
    t2 = Thread(target=download_task, args=('Peking Hot.avi', ))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了{:.2f}s'.format(end - start))

if __name__ == '__main__':
    main()
