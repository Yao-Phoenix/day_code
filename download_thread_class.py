from threading import Thread
from random import randint
from time import time, sleep

class download_task(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename
    def run(self):
        print('开始下载{}...'.format(self._filename))
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('{}下载完成! 总共耗费了{}s'.format(self._filename, time_to_download))

def main():
    start = time()
    t1 = download_task('Python从入门到住院.pdf')
    t1.start()
    t2 = download_task('Peking Hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了{:.2f}s'.format(end - start))

if __name__ == '__main__':
    main()
