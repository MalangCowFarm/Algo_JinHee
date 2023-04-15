# 델타 검색(우상향, 우, 하, 우하향
di = [-1,0,1,1]
dj = [1,1,0,1]

def omok(n,i,j): # 돌의 색과 첫 돌 좌표
    cnt = 0
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]

        # 연속한 돌의 개수 세기 위해 while
        while 0<=ni<19 and 0<=nj<19:
            if arr[ni][nj]==n:
                cnt += 1
                if cnt > 5:                 # 육목은 인정 X
                    return False
                ni += di[k]
                nj += dj[k]
            else:
                break
    return True


arr = [list(map(int,input().split())) for _ in range(19)]

for i in range(19):
    for j in range(19):
        if arr[i][j] != 0:
            n = arr[i][j]
            if omok(n,i,j):
                print(n)
                print(i+1,j+1)
            else:
                print(0)



