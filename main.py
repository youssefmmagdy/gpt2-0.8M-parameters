from collections import deque

def bfs(n, m, edges, s):
    adjlist = [[] for _ in range(n + 1)]

    for u, v in edges:
        adjlist[u].append(v)
        adjlist[v].append(u)
        
    #print(adjlist)
    q = deque([s])
    vis = [False] * (n+1)
    vis[s] = True 
    dis = [-1] * (n+1)
    dis[s] = 0
    while(q):
        parent = q.popleft()
        for child in adjlist[parent]:
            if not vis[child]:
                vis[child] = True
                dis[child] = 6 + dis[parent]
                q.append(child)
    return [dis[i] for i in range(1, n + 1) if i != s]


print(bfs(4, 2, [[1,2], [1,3]], 1))