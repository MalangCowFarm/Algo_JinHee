n = int(input())
tree = list(map(int,input().split()))
grow = list(map(int,input().split()))

# 성장 속도가 더딘 순으로 오름차순 정렬
lst = []
for i in range(n):
    lst.append([tree[i],grow[i]])
lst.sort(key=lambda x:x[1])


mx = 0
i = 0
while True:
    if i == n:
        break
    mx += lst[i][0] + lst[i][1] * i
    i += 1

print(mx)

'''
성장이 가장 큰 나무는 마지막에 베는 것이 이득
더딘 순으로 정렬을 먼저 하고 순서대로 베었다
시간초과에러가 뜰 줄 알았지만 생각보다 짧게 걸렸음! '''

'''
다른 사람 코드 : 나무는 왜 정렬 안해줘도 같은 값 나오는 지?'''
# grow.sort()
#
# mx = 0
# for i in range(n):
#     mx += tree[i]+grow[i]*i
#     print(tree[i]+grow[i]*i)
# print(mx)

