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





