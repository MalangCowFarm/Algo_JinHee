N, K = map(int,input().split())
visited = [0]*100001

def bfs(n):
    q = [n]

    while q:
        t = q.pop(0)
        if t == K:
            return visited[t]
        for nt in (t-1,t+1,t*2):
            if 0<=nt<=100000 and not visited[nt]:
                visited[nt] = visited[t]+1
                q.append(nt)

print(bfs(N))
