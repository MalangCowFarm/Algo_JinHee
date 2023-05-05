# '''
# 단순 구현인줄 알았는데 .......... O<-<
# '''
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
di = [1,-1,0,0,0]
dj = [0,0,0,-1,1]
mn = 3000

# 꽃을 심을 수 있는 조건인지 확인
def check(i,j):
    for k in range(5):
        ni, nj = i + di[k], j + dj[k]
        # 범위 밖이거나 미방문 시 False
        if not (0 <= ni < n and 0 <= nj < n and not visited[ni][nj]):
            return False
    return True

# 꽃 심기 (방문처리)
def plant(i,j,seed):
    for k in range(5):
        ni, nj = i + di[k], j + dj[k]
        visited[ni][nj] = seed

def dfs(cnt, tot):
    global mn
    # 꽃 3개 심었으면 최소 비용 갱신
    if cnt == 3:
        mn = min(mn, tot)
        return

    for i in range(1,n-1):
        for j in range(1,n-1):
            if check(i,j):
                plant(i,j,True) # 꽃 심고
                dfs(cnt+1, tot+sum([arr[i+di[k]][j+dj[k]] for k in range(5)]))
                plant(i,j,False) # 다시 초기화 

dfs(0,0)
print(mn)









# import sys
# input = sys.stdin.readline
#
# n = int(input())
# arr = [list(map(int,input().split())) for _ in range(n)]
# visited = [[False]*n for _ in range(n)]
# di = [1,-1,0,0,0]
# dj = [0,0,0,-1,1]
# mn = 3000
#
# def check(i,j):
#     for k in range(5):
#         ni, nj = i + di[k], j + dj[k]
#         if visited[ni][nj]:
#             return False
#     return True
#
# def plant(i,j,seed):
#     for k in range(5):
#         ni, nj = i + di[k], j + dj[k]
#         visited[ni][nj] = seed
#
#
# def dfs(cnt):
#     global mn
#     if cnt == 3:
#         tot = 0
#         for i in range(n):
#             for j in range(n):
#                 if visited[i][j]:
#                     tot += arr[i][j]
#         mn = min(mn, tot)
#
#     for i in range(1,n-1):
#         for j in range(1,n-1):
#             if check(i,j):
#                 plant(i,j,True)
#                 dfs(cnt+1)
#                 plant(i,j, False)
#
# dfs(0)
# print(mn)





# mn = []
# for i in range(1,n-1):
#     for j in range(1,n-1):
#         cnt = 0
#         for k in range(5):
#             ni, nj = i + di[k], j+dj[k]
#             if not visited[ni][nj]:
#                 visited[ni][nj] = 1
#                 cnt += arr[ni][nj]
#             else:
#                 continue





