import heapq as hq

pq = []
hq.heappush(pq,6)
hq.heappush(pq,12)
hq.heappush(pq,0)
hq.heappush(pq,2)
hq.heappush(pq,1)

print(pq)

while pq:
    print(pq[0])
    hq.heappop(pq)