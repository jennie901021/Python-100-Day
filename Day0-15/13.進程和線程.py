"""
Python中的多進程
Unix和Linux操作系統上提供了fork()系統調用來創建進程，調用fork()函數的是父進程，創建出的是子進程，子進程是父進程的一個拷貝，但是子進程擁有自己的PID。 
fork()函數非常特殊它會返回兩次，父進程中可以通過fork()函數的返回值得到子進程的PID，而子進程中的返回值永遠都是0。 Python的os模塊提供了fork()函數。由於Windows系統
沒有fork()調用，因此要實現跨平台的多進程編程，可以使用multiprocessing模塊的Process類來創建子進程，而且該模塊還提供了更高級的封裝，例如批量啟動進程的進程池（Pool）、用於進程間通信的隊列（Queue）和管道（Pipe）等

"""
from random import randint
from time import time, sleep


def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    download_task('Python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()

"""
Python中的多線程
在Python早期的版本中就引入了thread模塊（現在名為_thread）來實現多線程編程，然而該模塊過於底層，而且很多功能都沒有提供，因此目前的
多線程開發我們推薦使用threading模塊，該模塊對多線程編程提供了更好的面向對象的封裝。我們把剛才下載文件的例子用多線程的方式來實現一遍
"""

from random import randint
from threading import Thread
from time import time, sleep


def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    t1 = Thread(target=download, args=('Python从入门到住院.pdf',))
    t1.start()
    t2 = Thread(target=download, args=('Peking Hot.avi',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))


if __name__ == '__main__':
    main()