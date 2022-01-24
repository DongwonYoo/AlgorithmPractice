#BFS　Queueを使う
#DFSと探索順番が違う
from collections import deque
adj = [[0] * 13 for _ in range(13)]
adj[0][1] = adj[0][2] = 1
adj[1][3] = adj[1][4] = 1

def bfs():
    dq = deque()
    dq.append(0)
    while  dq:
        now = dq.popleft()
        for next in range(13):
            if adj[now][next]:
                dq.append(next)

bfs()

