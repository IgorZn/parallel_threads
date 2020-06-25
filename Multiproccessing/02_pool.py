import concurrent.futures
import time

"""
	в общем, тут идея в том, что вместо того чтобы городить огород как:
			for _ in range(50):
				p = multiprocessing.Process(target=do_something, args=(1,))
				p.start()
				processing.append(p)
			...
			..
			и т.д.
	можно воспользоваться "ProcessPoolExecutor" чз контекстный менеджер и как
	результат получить компактный код.
	
	ProcessPoolExecutor -- управляет процессами исходя из характеристик ПК, т.о. мы избегаем
	ситуации когда система ложиться под нагрузкой.
"""
N = 300


def do_something(sec):
	print(f'Sleeping for {sec} sec')
	time.sleep(sec)
	return 'Done sleeping.'


def run_multiprocessing():
	print('-- RUN run_multiprocessing')
	start = time.perf_counter()

	with concurrent.futures.ProcessPoolExecutor() as executor:
		results = [executor.submit(do_something, 1) for _ in range(N)]

		for f in concurrent.futures.as_completed(results):
			print(f.result())

	end = time.perf_counter()
	print(f'Finished multiprocessing in {end - start} second(s)')


def run_threads():
	print('--- RUN run_threads')
	start = time.perf_counter()

	with concurrent.futures.ThreadPoolExecutor() as executor:
		results = [executor.submit(do_something, 1) for _ in range(N)]

		for f in concurrent.futures.as_completed(results):
			print(f.result())

	end = time.perf_counter()
	print(f'Finished threads in {end - start} second(s)')


if __name__ == '__main__':

	# run_multiprocessing()2
	run_threads()