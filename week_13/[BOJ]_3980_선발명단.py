'''
 모든 포지션에 선수를 배치해야 하고,
 각 선수는 능력치가 0인 포지션에 배치될 수 없다.
'''


N = int(input())
for _ in range(N):
    arr = [list(map(int,input().split())) for _ in range(11)]
    visited = [0]*11
    mx = 0


    def dfs(n,cnt):
        global mx
        # 선수 다 뽑았으면 최대값 갱신
        if n == 11:
            mx = max(mx, cnt)
            return

        for i in range(11):
            if not visited[i] and arr[n][i] != 0:
                visited[i] = 1
                dfs(n+1, cnt+arr[n][i])
                visited[i] = 0


    dfs(0, 0)
    print(mx)

