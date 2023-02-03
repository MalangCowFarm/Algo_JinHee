T = int(input())
for tc in range(T):
    a, b = map(int, input().split())
    result = a*b            # 처음에 리턴 값 정의 안했더니 자꾸 0 나옴 

    while b > 0:
        a, b = b, a%b      # 시간초과라고 떠서 유클리드 호제법을 배웠다. . 
    print(result//a)