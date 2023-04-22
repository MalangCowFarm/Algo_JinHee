import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]

di = [-1,1,0,0]
dj = [0,0,-1,1]

q = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            q.append((i,j))

day = 0
while q:
    i,j = q.pop(0)
    for k in range(4):
        ni, nj = i + di[k], j+dj[k]
        # 범위 내에 있고, 안익은 토마토라면
        if 0<=ni<m and 0<=nj<n and arr[ni][nj] == 0:
            q.append((ni,nj))
            arr[ni][nj] = arr[i][j] + 1
            day = max(day, arr[ni][nj])

for lst in arr:
    # 순회를 다 해도 안익은 토마토가 있다면 -1 출력 되도록
    if 0 in lst:
        day = -1
        break

print(day)

'''
시간초과 
'''