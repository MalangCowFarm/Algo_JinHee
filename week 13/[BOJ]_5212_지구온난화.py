r, c = map(int,input().split())
island = [list(input()) for _ in range(r)]
ans = [['.']*c for _ in range(r)]

di = [-1,1,0,0]
dj = [0,0,-1,1]
r_lst = []
c_lst = []

for i in range(r):
    for j in range(c):
        if island[i][j] == 'X':
            cnt = 0
            for k in range(4):
                ni, nj = i + di[k], j + dj[k]
                if 0<=ni<r and 0<=nj<c and island[ni][nj] == 'X':
                    cnt += 1

            if cnt >= 2:
                r_lst.append(i)
                c_lst.append(j)
                ans[i][j] = 'X'

for i in range(min(r_lst),max(r_lst)+1):
    for j in range(min(c_lst),max(c_lst)+1):
        print(ans[i][j],end='')
    print()

'''
시간초과 날 줄 알았는데 . . 기뻐요 
'''