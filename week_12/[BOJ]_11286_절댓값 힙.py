import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = []

for _ in range(n):
    value = int(input())

    # 0이 아니면, 힙에 순서대로 넣기(우선순위 정보 포함해서)
    if value != 0:
        heapq.heappush(h,(abs(value),value))
    # 0이면 원소가 힙에 남아 있으면 pop, 없으면 0 출력
    else:
        if h:
            print(heapq.heappop(h)[1]) # 힙에서 가장 작은 값 pop
        else:
            print(0)
'''
아래 코드는 절댓값 힙에 삽입된 순서대로 결과를 출력하기 때문에
입력값이 0일 때와 아닐 때가 구분되어 있지 않았음
'''
#
# def heapsort(iterable):
#     h = []
#     result = []
#     # 모든 원소를 차례대로 힙에 삽입
#     # 삽입 시 우선순위가 높은 원소의 정보도 넣어주기(절댓값)
#     for value in iterable:
#         heapq.heappush(h,(abs(value),value))
#
#     # 힙에 삽입된 모든 원소를 차례대로 꺼내 담기
#     for i in range(len(h)):
#         result.append(heapq.heappop(h)[1])
#     return result
#
# n = int(input())
# arr = []
#
# for _ in range(n):
#     arr.append(int(input()))
#
# answer = heapsort(arr)
# for ans in answer:
#     if ans != 0:
#         print(ans)
#     else:
#         print(0)


'''
힙에 원소를 추가할 때 (-i, i)의 튜플형태로 넣어주면 
튜플의 첫 번째 원소를 기준으로 힙을 구성하게 된다.

실제값은 튜플의 두 번째 자리에 저장되어 있으므로 
[1]인덱싱을 통해서 접근해주면 된다.
'''