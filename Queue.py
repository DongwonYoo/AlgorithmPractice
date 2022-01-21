from queue import Queue

#dequeより遅い
# thread-safe

q = Queue()
q.put(123)
q.put(456)
q.put(789)
while q:
    print(q.get())