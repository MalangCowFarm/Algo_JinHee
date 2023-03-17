'''
- 문제가 너무 길어서 잠시 정신이 아득해졌습니다..

- dungeons = [(탐험 시작 : 최소 필요 피로도  / 탐험에 소모되는 피로도 : 소모 피로도),,]
- 현재 피로도(k)가 주어졌을 때, 가능한 던전 루트 조합 중 최대 던전 수를 구해야 함

- 알게된 점
=> 또 .. 가능한 조합을 구하기 위해 순열(permutations) 모듈을 사용하였다

'''
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    num = len(dungeons)

    for route in permutations(dungeons,num): #dungeons에서 num개 선택
        cnt = 0
        kk = k              # 왜 따로 변수 선언해야 하지?
        for n in route:
            if kk >= n[0]: # 필요 피로도
                kk -= n[1] # 소모 피로도
                cnt += 1
            if cnt > answer:
                answer = cnt
    return answer



