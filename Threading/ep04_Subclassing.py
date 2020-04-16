import threading
import time

class MyThread(threading.Thread):

    def run(self):
        print(f'{self.getName()} has started')
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs

        print(f'{self.getName()} has finished')


def sleeper(N, name):
    print(f'Hello, {name}. I\'m going to sleep for {N} seconds.')
    time.sleep(N)
    print(f':{name}\t I\'ve woken up. I\'ve slept for {N} \n')



def run_sleeper():


    for i in range(0,5):
        name = f'thread {i}'
        t = MyThread(target=sleeper, name=name, args=(3, name))

        t.start()



start = time.time()
run_sleeper()
end = time.time()
print(f'The end. Time taken {end - start}')
