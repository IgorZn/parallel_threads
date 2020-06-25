import multiprocessing
import time


def do_something(sec):
	print(f'Sleeping for {sec} sec')
	time.sleep(sec)
	print('Done sleeping.')


def run_multiprocessing():
	start = time.perf_counter()
	processing = []

	for _ in range(50):
		p = multiprocessing.Process(target=do_something, args=(1,))
		p.start()
		processing.append(p)

	for _ in processing:
		_.join()

	end = time.perf_counter()
	print(f'Finished in {end - start} second(s)')


if __name__ == '__main__':

	run_multiprocessing()