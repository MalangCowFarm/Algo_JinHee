arr = [list(map(int,input().split())) for _ in range(19)]
player = 0
location= 0


def omok(n):
    global player,location
    for i in range(19):
        for j in range(19):
            for di, dj in ((-1, 1), (0, 1), (1, 0),(1, 1)):
                for mul in range(5):  # 0인 경우 i, j
                    ni, nj = i + di * mul, j + dj * mul
                    #  범위를 벗어났거나 범위내 지만 돌이 아닌 경우
                    if 0 <= ni < 19 and 0 <= nj < 19 and arr[ni][nj] == n:
                        if ni != 0 and nj !=0:
                            pass  # 오목 성공
                    else:
                        break  # 다음 방향으로
                else:  # for문 다섯 번 다 돌았을 경우. 즉 5개가 돌인 경우
                    player += n
                    location = (i+1,j+1)
    return

omok(1)
omok(2)

if player == 0 or player == 3:
    print(0)
else:
    print(player)
    print(*location)

'''
1번, 2번 돌을 함수에 하나씩 돌려서 확인하고 싶었는데 틀렸습니다.
'''