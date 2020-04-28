import threading
import time

lock = threading.Lock()
x = 0

COUNT = 10000


def use_lock(func):
    with lock:
        return func()


@use_lock
def adding_2():
    global x
    for i in range(COUNT):
        x+=2


@use_lock
def adding_3():
    global x
    for i in range(COUNT):
        x+=3


@use_lock
def substracting_4():
    global x
    for i in range(COUNT):
        x-=4


@use_lock
def substracting_1():
    global x
    for i in range(COUNT):
        x-=1


if __name__ == '__main__':
    start = time.time()

    thread_list = [adding_2, adding_3, substracting_4, substracting_1]

    for _ in range(100):
        for i in range(10000):
            for thread in thread_list:
                th = threading.Thread(target=thread)
                th.start()
                th.join()

            if x != 0:
                print(x)
                break
        print(_, x)
