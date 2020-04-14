import threading
import time


def sleeper(N, name):
    print(f'{name}. I\'m going to sleep for {N} seconds.')
    time.sleep(N)
    print(f'I\'ve woken. I\'ve slept for {N}')


t = threading.Thread(target=sleeper, args=(5, 'Thread_1'), name='Thread_1')

thread_list = []


def run_threads():
    for i in range(0,5):
        t = threading.Thread(target=sleeper, args=(1, f'Thread_{i}'), name=f'Thread_{i}')
        thread_list.append(t)
        t.start()
        print(f'{t.name} has started')


def wait_end_threads():
    for t in thread_list:
        t.join()


if __name__ == '__main__':
    start = time.time()

    run_threads()
    wait_end_threads()

    end = time.time()

    print(f'The end. Time taken {end-start}')
