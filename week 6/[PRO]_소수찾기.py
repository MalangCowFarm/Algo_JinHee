'''
- 가능한 문자열 속 숫자를 조합한다
- 조합한 수가 소수라면 리스트에 추가 후 중복 제거한다

알게된 개념
=> 에라토스테네스의 체 : 2부터 시작하여 배수들을 지워나가면서 소수 판별
=> permutations 모듈 : 문자열에서 만들 수 있는 모든 숫자 조합
   from itertools import permutations
=> set : 중복값 제외

다 내가 모르는 개념이었다 ㅜ.ㅜ
'''
from itertools import permutations

def sosu(n):
    if n < 2:                         # 소수는 2 이상이므로 그 이하는 False
        return False
    for i in range(2,int(n**0.5)+1):  # 2부터 순회하여 n의 배수라면 False
        if n % i == 0:
            return False
    return True

def solution(numbers):
    num_lst = [] # 한 문자씩 가져와 조합 생성

    for i in range(1,len(numbers)+1):
        for j in permutations(numbers,i):
            num = int(''.join(j))
            if sosu(num):
                num_lst.append(num)

    num_lst = set(num_lst)
    answer = len(num_lst)

    return answer



