#Python:min-heap
#pythonではpopしたら
# root nodeが min-heapなので一番小さい値が出る
from  queue import PriorityQueue
#thread-safe

pq = PriorityQueue()
pq.put(2)
pq.put(4)
pq.put(6)
pq.put(9)
pq.put(0)
while not pq.empty():
    print(pq.get())