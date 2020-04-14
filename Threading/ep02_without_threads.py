import threading
import time


def sleeper(N, name):
    print(f'{name}. I\'m going to sleep for {N} seconds.')
    time.sleep(N)
    print(f'I\'ve woken. I\'ve slept for {N}')


def run_sleeper():
    for i in range(0,5):
        sleeper(1, i)


if __name__ == '__main__':
    start = time.time()
    run_sleeper()
    end = time.time()

    print(f'The end. Time taken {end-start}')
