'''
예전에 풀었던 미로탐색이랑 비슷한 문제 같은데
복습도 안하고 잊고 있었더니 좀. . 그랬다. .
'''

di = [-1,-2,-2,-1,1,2,2,1]
dj = [-2,-1,1,2,-2,-1,1,2]

N = int(input())
for _ in range(N):
    l = int(input())
    sr, sc = map(int,input().split())   # 현재 위치
    er, ec = map(int,input().split())   # 이동 위치

    if sr == er and sc == ec:
        print(0)
    else:
        # bfs
        # 초기화
        visited = [[0]*l for _ in range(l)]
        q = [(sr,sc)]

        # 큐가 빌 때까지 반복
        while q:
            sr,sc = q.pop(0)
            for k in range(8):
                nr, nc = sr + di[k], sc + dj[k]
                if 0<=nr<l and 0<=nc<l and not visited[nr][nc]:
                    q.append((nr,nc))
                    visited[nr][nc] = visited[sr][sc] + 1

        print(visited[er][ec])


