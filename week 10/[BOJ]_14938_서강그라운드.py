
n,m,r = map(int,input().split())
items = [0]+list(map(int,input().split()))
INF = 1e8

distance = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    distance[i][i] = 0

for _ in range(r):
    a,b,l = map(int,input().split())
    distance[a][b] = l
    distance[b][a] = l


for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
