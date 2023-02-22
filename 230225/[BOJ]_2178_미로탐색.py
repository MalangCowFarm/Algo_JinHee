'''
1. 1은 이동, 0은 벽
2. (1,1)에서 출발해 (N,M) 로 이동할 때 지나는 최소 거리 => BFS
3. 항상 도착위치로 갈 수 있는 경우만 존재(미로 안 막혀 있음)
'''
# 델타 
dr = [-1,1,0,0]
dc = [0,0,-1,1]

N,M = map(int,input().split())
maze = [list(map(int,input())) for _ in range(N)]

r, c = 0, 0 # 현재 위치

# bfs 
# 초기화 (방문배열, 큐)
visited = [[0]*M for _ in range(N)]
visited[r][c] = 1      
q = []
q.append((r,c))

# 큐가 빌 때 까지 반복. 비었으면 탐색 완료
while q:
    r, c = q.pop(0)

    # r, c 기준 델타 탐색     
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0<=nr<N and 0<=nc<M and maze[nr][nc] ==1 and not visited[nr][nc]:
            q.append((nr,nc))
            visited[nr][nc] = visited[r][c] +1
    
print(visited[N-1][M-1])




