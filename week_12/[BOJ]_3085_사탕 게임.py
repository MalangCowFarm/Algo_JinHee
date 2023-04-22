import sys
input = sys.stdin.readline

n = int(input())
arr= [list(input().rstrip()) for _ in range(n)]
di = [1,0]
dj = [0,1]
ans = 0

# [2] 최대로 얻을 수 있는 사탕 개수 세기
def cnt():
    # 행 탐색
    row = 1
    row_mx = 0     # 적어도 하나의 사탕은 얻을 수 있음
    for i in range(n):
        for j in range(n-1):
            # 같으면 더해주고 다르면 초기화
            if arr[i][j] == arr[i][j+1]:
                row += 1
            else:
                row = 1
            row_mx = max(row_mx, row)
        row = 1 # 초기화

    # 열 탐색(전치행렬)
    arr_ = list(zip(*arr))
    col = 1
    col_mx = 0
    for i in range(n):
        for j in range(n-1):
            if arr_[i][j] == arr_[i][j + 1]:
                col += 1
            else:
                col = 1
            col_mx = max(col_mx,col)
        col = 1
    cnt = max(row_mx, col_mx)
    return cnt


# [1] 서로 다른 색의 사탕 자리 바꾸기
for i in range(n):
    for j in range(n):
        for k in range(2):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<=ni<n and 0<=nj<n:
                if arr[i][j] != arr[ni][nj]:
                    arr[i][j],arr[ni][nj] = arr[ni][nj],arr[i][j]
                    ans = max(ans,cnt())
                    arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j] # 탐색 후 초기화

print(ans)


'''
- 상하좌우는 탐색 중복이 있어서 오른쪽, 아래만 탐색
- 다른 색의 사탕이 있을 때마다 개수 세어주고 배열 초기화 
'''