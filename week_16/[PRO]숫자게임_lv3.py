def solution(A, B):
    A.sort()
    B.sort()
    answer = 0
    idx = 0
    num = len(A)

    for i in range(num):
        if B[i] > A[idx]:
            answer += 1
            idx += 1

    return answer

