import queue
import time
import threading
from random import randint


q = queue.PriorityQueue()

for i in range(5):
    q.put(i)
    print(i, end=' ')

print(' --> ', end='  ')

for i in range(q.qsize()):
    print(q.get(), end=' ')

print("Порядок очереди был отсортирован невзирая на порядок очередности входа в очередь")

for i in range(5):
    q.put((i, f'Some data {i};'))
    print(i, end=' ')

print(' --> ', end='  ')

for i in range(q.qsize()):
    print(q.get()[1], end=' ')

print()
print("""А вот как используя картежи в очереди, можно складывать какие-нибудь данные. 
Сортировка будет идти по 0-му индексу""")