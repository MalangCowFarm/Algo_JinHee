R, C = map(int,input().split())
arr = [list(input()) for _ in range(R)]
tot = []

for n in range(R-7):
    for m in range(C-7):
        cnt1 = 0    # 흰 - 검 순서
        cnt2 = 0    # 검 - 흰 순서
        for i in range(n,n+8):
            cnt = 0
            for j in range(m,m+8):
                if (i+j)%2 == 0:
                    if arr[i][j] != 'W':
                        cnt1 += 1
                    else:
                        cnt2 += 1
                else:
                    if arr[i][j] != 'B':
                        cnt1 += 1
                    else:
                        cnt2 += 1

        tot.append(cnt1)
        tot.append(cnt2)

mn = min(tot)
print(mn)

'''
첫 시도
4중 for문까지 범위는 잘 설정 했는데 무작정 색이 같은 영역을 세어 주고 
토탈 변수에 2로 나눈 몫만큼 추가하며 비교하려 했으나 실패 . '''





