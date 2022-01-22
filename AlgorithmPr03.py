#boj.kr/11286
import sys
import heapq as hq

input = sys.stdin.readline #早い入力

pq = []
N = int(input())

for _ in range(N):
    x =int(input())#
    if x: #x!=0
        hq.heappush(pq, (abs(x), x)) #絶対値、元本値
        
    else: #x==0
        print(hq.heappop(pq)[1] if pq else 0) #下のIF文と一緒

        # if pq:
        #     print(hq.heappop(pq))
        # else:
        #     print(0)

