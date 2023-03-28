N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
ans = []


def dfs(n):  # n은 만든 리스트의 길이
    if n == M:  # 종료 조건 만약 길이가 M이 되면 출력 및 종료 처리
        print(*ans)
        return

    for i in range(N):
        if num[i] not in ans:
            ans.append(num[i])  # 정답리스트에 없으면 추가
            dfs(n + 1)  # 길이 +1 . . 재귀
            ans.pop()


dfs(0)
