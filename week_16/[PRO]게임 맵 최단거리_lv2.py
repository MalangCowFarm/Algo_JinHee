from collections import deque
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1            # 출발점 방문
    q = deque([(0,0)])

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0<=nr<n and 0<=nc<m and maps[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                q.append([nr,nc])

    answer = -1
    if visited[-1][-1]:
        return visited[-1][-1]

    return answer