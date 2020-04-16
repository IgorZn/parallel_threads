import threading
import time


class MyThread(threading.Thread):
    def __init__(self, number, func, args):
        super().__init__()
        self.number = number
        self.func = func
        self.args = args

    def run(self):
        print('*self.args:', *self.args)
        print(f'{self.number} has started')
        self.func(*self.args)
        print(f'{self.number} has finished')


def double(number, cycles):
    for i in range(cycles):
        number += number
    print(number)


thread_list = []

for i in range(0, 50):
    name = f'thread {i}'
    t = MyThread(number=i+1, func=double, args=[i, 3])
    t.start()

print(__name__)

for t in thread_list:
    t.join()

start = time.time()
end = time.time()
print(f'The end. Time taken {end - start}')
