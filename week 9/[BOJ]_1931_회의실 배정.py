'''
그리디 알고리즘 : 현재 상황에서 최선만 고르는 방법 (미래 고려 x)

람다가 익숙하지 않다. . 가르쳐 줄 사람. .
종료, 시작시간 바꿔서 조금 헷갈리게 코드를 짰다.
시간이 오래 걸렸다.
'''

N = int(input())
lst = []
for _ in range(N):
    s, e = map(int,input().split())
    lst.append((e,s)) # 종료시간, 시작시간

# 종료시간 빠른 기준으로 정렬
lst.sort()
# print(lst)

end = 0
cnt = 0

for e, s in lst:
    # 현재 시작시간이 이전 종료시간보다 늦으면 유효함 !
    if s >= end:
        cnt += 1
        end = e
print(cnt)