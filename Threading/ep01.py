import threading
import time


def sleeper(N, name):
    print(f'Hello, {name}. I\'m going to sleep for {N} seconds.')
    time.sleep(N)
    print(f'I\'ve woken. I\'ve spleept for {N}')


t = threading.Thread(target=sleeper, args=(5, 'Thread_1'), name='Thread_1')

if __name__ == '__main__':
    # t.start()
    # print(f'I\'m running immediately after t, I DO not wait end of t')

    """
    Главный поток main НЕ ждет завершения потока 't'
        |
        |______
        |       |
        main    sleeper
        |       |
        |-------
        |
        end
    
    """

    # Дождаться завершения потока
    t.start()
    print(f'I\'m running immediately after t, I DO not wait end of t')
    
    t.join()
    print('After join')
