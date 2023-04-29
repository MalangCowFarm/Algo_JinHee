'''
링크와 스타트 풀기 전에 푸는 게 좋은 것 같아서 대체해서 풀었습니다.. 
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [0] * n # 인덱스 저장할 방문 배열
mn = 1e8

def dfs(depth,idx):
    global mn
    if depth == n//2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                # 방문처리 한 팀: 스타트/ 미방문 팀 : 링크
                if visited[i] and visited[j]:
                    start += arr[i][j]
                elif not visited[i] and not visited[j]:
                    link += arr[i][j]
        # 점수차가 최소가 되면 최소값 갱신
        mn = min(mn, abs(start-link))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            # 팀이 만들어지기 전(n//2명)까지 백트래킹
            dfs(depth+1, i+1)
            visited[i] = 0

dfs(0,0)
print(mn)

