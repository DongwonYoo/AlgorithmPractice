#DFS

adj = [[0] * 13 for _ in range(13)]
adj[0][1] = adj[0][7] = 1
adj[1][2] = adj[1][5] = 1
adj[2][3] = adj[2][4] = 1

# for row in adj:
#     print (row)
def dfs(now):
    for next in range(13):
        if adj[now][next]:
            dfs(next)

dfs(0)