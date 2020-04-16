import threading
import time


class MyThread(threading.Thread):
    def __init__(self, number, style, *args, **kwargs):
        self.number = number
        self.style = style
        super().__init__(*args, **kwargs)

    def run(self):
        print(f'has started')
        super().run()
        print(f'has finished')

def run_sleeper(num, style):
    print(f'sleep for {num} and style is {style}')
    time.sleep(num)


t = MyThread(number=3, style=run_sleeper.__name__, args=[3, run_sleeper.__name__], target=run_sleeper)

start = time.time()
t.start()
end = time.time()
print(f'The end. Time taken {end - start}')
