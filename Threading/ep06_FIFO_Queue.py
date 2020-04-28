"""
FIFO -- способ организации и манипулирования данными относительно времени и приоритетов. Это выражение описывает
        принцип технической обработки очереди или обслуживания конфликтных требований путём упорядочения процесса
        по принципу: «первым пришёл — первым обслужен».

LIFO -- «последним пришёл — первым ушёл» — способ организации и манипулирования данными относительно времени и
        приоритетов. В структурированном линейном списке, организованном по принципу LIFO, элементы могут добавляться
        и выбираться только с одного конца, называемого «вершиной списка». Структура LIFO может быть проиллюстрирована
        на примере стопки тарелок: чтобы взять вторую сверху, нужно снять верхнюю, а чтобы снять последнюю, нужно
        снять все лежащие выше.

Priority
"""

import queue
import time
import threading

q = queue.Queue()


def simple_q():
    # Сложить в очередь значения от 0 до 9
    for i in range(10):
        q.put(i)

    for i in range(q.qsize()):
        print(q.get(), f'q.empty: {q.empty()}, q.size: {q.qsize()}')


def size_of_queue(q):
    while q.empty():
        print(f'The size of queue is: {q.qsize()}')
        time.sleep(0.2)


def add_val_to_q(q):
    while True:
        print('Start thread')
        time.sleep(3)
        q.put(5)


simple_q()

t = threading.Thread(target=add_val_to_q, args=(q,), daemon=True)
t.start()
t2 = threading.Thread(target=size_of_queue, args=(q,), daemon=True)
t2.start()

q.put(100)

print(q.get())

print('Now wait for new val in queue')
print(q.get())

