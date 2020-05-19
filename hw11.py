from threading import Thread, Semaphore, RLock

import time

s = Semaphore(2)
lock = RLock()

book = []
book_len = len(book)


def Writer1(interval):
    global book
    while True:
        with lock:
            book.append('Something to be written!')
        time.sleep(interval)


def Writer2(interval):
    global book
    global book_len
    while True:
        with lock:
            book.append('Something to be written by other writer!')
        time.sleep(interval)


def Readers(interval):
    global book
    while True:
        s.acquire()
        print(book)
        time.sleep(interval)
        s.release()


if __name__ == '__main__':
    wr1 = (Thread(target=Writer1, args=(1,)))
    wr2 = (Thread(target=Writer2, args=(3,)))

    r = (Thread(target=Readers, args=(5,)) for _ in range(3))
    wr1.start()
    wr2.start()
    for a in r:
        a.start()
