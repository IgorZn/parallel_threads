import threading
import time
import random

e = threading.Event()


def flag():
	time.sleep(2)
	e.set()
	print('Event has been set, start countdown (7 sec)')
	time.sleep(7)
	print('Event has been cleaned')
	e.clear()


def start_operations():
	# Ждём, когда кто-нибудь захватит флаг
	# Если нужно задать время ожидания, его пишут в секундах, в виде числа с плавающей запятой.
	e.wait()
	i = 0
	while e.is_set():
		print(f'Now this {start_operations.__name__} (thread) is working till call "e.clear()" ', end='___ ')
		print(random.randint(1, 1000))
		i += 1
		print(f'{i/2} second')
		time.sleep(.5)


def start_operations2():
	# Ждём, когда кто-нибудь захватит флаг
	# Если нужно задать время ожидания, его пишут в секундах, в виде числа с плавающей запятой.
	e.wait()
	i = 0
	while e.is_set():
		print(f'Now this {start_operations2.__name__} (thread) is working till call "e.clear()" ', end='___ ')
		print(random.randint(1, 1000))
		print()
		i += 1
		print(f'{i/2} second')
		time.sleep(.5)


if __name__ == '__main__':

	t1 = threading.Thread(target=flag)
	t2 = threading.Thread(target=start_operations)
	t3 = threading.Thread(target=start_operations)

	t1.start()
	t2.start()
	t3.start()