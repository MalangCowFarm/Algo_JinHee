'''
[투 포인터 알고리즘 O(N)]
리스트에 순차적으로 접근해야 할 때 두 점의 위치를 기록하며 처리하는 알고리즘.
이 때, 두 점은 시작점과 끝 점을 의미한다.

1. 시작점과 끝점이 첫 인덱스(0)를 가리키게 한다.
2. 현재 부분합 == M이면 cnt +1
3. 현재 부분합 < M이면 끝점 인덱스 +1
4. 현재 부분합 > M이면 시작점 인덱스 +1
5. 조건에 맞는 결과 나올 때까지 2~4 반복
'''

n, m = map(int,input().split())
lst = list(map(int,input().split()))

ans = n+1
sm = 0
end = 0

# start 증가시키며 반복
for start in range(n):    while sm<m and end<n:
        sm += lst[end]
        end += 1
    # 부분합이 m일때 cnt+=1
    if sm == m:
        if len(lst[start:end]) < ans:
            ans = len(lst[start:end])
    sm -= lst[start]

if ans == n+1:
    print(0)
else:
    print(ans)
    # end를 가능한 만큼 이동


