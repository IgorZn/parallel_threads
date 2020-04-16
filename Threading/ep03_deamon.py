import threading
import time

total = 4


def create_items_1():
    global total

    for i in range(10):
        time.sleep(2)
        print(f'iteration №1 {i}')
        total += 1

    print('iteration №1 done')


def create_items_2():
    global total

    for i in range(7):
        time.sleep(1)
        print(f'iteration №2 {i}')
        total += 1

    print('iteration №2 done')


def limit_items():
    global total
    while True:
        if total > 5:
            print('== Overload ==')
            total -= 3
            print('TOTAL subtracted by 3')
        else:
            time.sleep(1)
            print('\twaiting', )


if __name__ == '__main__':
    start = time.time()

    creates1 = threading.Thread(target=create_items_1)
    creates2 = threading.Thread(target=create_items_2)
    """
    при выходе из потока main все потоки будут остановлены, даже если они
    работают, в данном случае выход наступит стразу после
    >>> print(f'The end. Time taken {end-start}')
    в этом случае потоки с ключом deamond=True будут принудительно
    закрыты, чего не произойдет если использовать limiter.join(),
    т.е. если поток устрон так, что он бесконечный, как впримере, то
    будет завершен.
    """

    limiter = threading.Thread(target=limit_items, daemon=True)

    creates1.start()
    creates2.start()
    limiter.start()

    creates1.join()
    creates2.join()
    # limiter.join()

    end = time.time()

    print(f'The end. Time taken {end-start}')