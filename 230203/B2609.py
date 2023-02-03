a, b = map(int, input().split())
mul = a * b # 미리 저장해줘야 밑에서 값 바뀌어도 ㄱㅊ

while b>0:
    a, b = b, a%b   # 최대 공약수 구하기

print(a)
print(mul//a)   # 최소공배수 