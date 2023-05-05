import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

result = []

for i in reversed(p) :
    result.insert(i, n)
    n -= 1

for i in result :
    print(i, end = ' ')


# n = int(input())
# lst = list(map(int,input().split()))
# ans = [0] * n
#
# for idx in range(n):
#     cnt = 0
#     for j in range(n):
#         if not ans[j]:
#             if cnt == lst[idx]:
#                 ans[j] = idx+1
#                 break
#             else:
#                 cnt += 1
#
# print(*ans)


# for i in range(n):
#     if not ans[lst[i]]:
#         ans[lst[i]] = i+1
#     else:
#         j += 1
#         if not ans[lst[i]+j]:
#             ans[lst[i]+j] = i+1

