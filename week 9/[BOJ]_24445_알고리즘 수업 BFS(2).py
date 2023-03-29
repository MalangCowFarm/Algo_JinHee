'''
간선은 양방향이며, 내림차순으로 방문
'''

V,E,S = map(int,input().split()) # 노드, 간선, 출발점
adj = [[] for _ in range(V+1)]
visited = [0] * (V+1)

# 시작점 S에 대하여 q, 방문체크, 카운트 +1
q = [S]
visited[S] = 1
cnt = 1

# 양방향 간선 표시
for _ in range(E):
    start,to = map(int,input().split())
    adj[start].append(to)
    adj[to].append(start)

# 내림차순 정렬
for i in range(1,V+1):
    adj[i].sort(reverse=True)

while q:
    t = q.pop(0)
    # 인접행렬 안에 있고, 미방문 시 카운트
    for nt in adj[t]:
        if not visited[nt]:
            cnt += 1
            visited[nt] = cnt # 방문 순서를 기록하기 위함
            q.append(nt)

for k in visited[1:]:
    print(k)
