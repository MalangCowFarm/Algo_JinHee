from collections import deque

F,S,G,U,D = map(int,input().split())
visited = [0] * (F+1)
q = deque()


def bfs(S,G):
    # 현재위치 큐에 저장 & 방문처리
    q.append(S)
    visited[S] = 1

    # 큐가 빌 때까지 반복
    while q:
        sc = q.popleft()

        if sc == G:
            return visited[sc]-1

        # 범위 내에 있고 미방문일 때 방문 처리
        for nc in (sc + U, sc - D):
            if 1<= nc <= F and not visited[nc]:
                q.append(nc)
                visited[nc] = visited[sc]+1

    return 'use the stairs'


print(bfs(S,G))

##### recursion error #####
# def check(start):
#     # (a) 목표지점 도착
#     if start == G:
#         return True
#     # (b) 출발지가 더 높은 층이면
#     if start > G:
#         # 내려갈 수 없다면 False
#         if D == 0:
#             return False
#         # 내려갈 수 있다면 내려간 뒤 체크
#         return check(start-D)
#     # (c) 출발지가 더 낮다면
#     else:
#         # 올라갈 수 없다면 False
#         if U == 0:
#             return False
#         # 올라갈 수 있다면 올라간 후 체크
#         return check(start+U)
#
# if check(S):
#     cnt = 0
#     while S != G:
#         if S < G:
#             S += U
#         else:
#             S -= D
#         cnt += 1
#     print(cnt)
# else:
#     print('use the stairs')
#
