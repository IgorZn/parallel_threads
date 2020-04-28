import queue
import time
import threading


q = queue.LifoQueue()


for i in range(5):
    q.put(i)
    print(i, end=' ')

print(' --> ', end='  ')

for i in range(q.qsize()):
    print(q.get(), end=' ')

print("""
как видно 4ка вошла последний и первой вышла.
""")
