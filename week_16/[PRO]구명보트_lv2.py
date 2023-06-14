def solution(people, limit):
    people.sort()
    start, end = 0, len(people)-1
    cnt = 0

    while start <= end:
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1
        cnt += 1
    return cnt