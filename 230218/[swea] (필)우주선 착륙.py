T = int(input())
di = [-1,-1,-1,0,0,1,1,1]
dj = [-1,0,1,-1,1,-1,0,1]

for tc in range(1,T+1):
    n, m = map(int,input().split())
    space = [list(map(int,input().split())) for _ in range(n)]
    ans = 0

    for i in range(n):
        for j in range(m):
            cnt = 0 

            for k in range(8):
                ni, nj = i + di[k], j + dj[k]

                if 0<=ni<n and 0<=nj<m:
                    if space[i][j] > space[ni][nj]:
                        cnt+=1 
            if cnt >= 4:
                ans += 1
    print(f'#{tc} {ans}')

