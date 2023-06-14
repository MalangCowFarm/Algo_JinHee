left = [1,4,7]
right = [3,6,9]

def compare(sd, st):
    distance = abs(sd-st)
    distance = distance//3 + distance%3
    return distance

def solution(numbers, hand):
    for n in numbers:
        if n == 0:
            numbers[numbers.index(n)] = 11
    sl = 10
    sr = 12
    answer = ''
    for n in numbers:
        if n in left:
            answer += 'L'
            sl = n
        elif n in right:
            answer += 'R'
            sr = n
        else:
            if compare(sl,n) < compare(sr,n):
                answer += 'L'
                sl = n
            elif compare(sl,n) > compare(sr,n):
                answer += 'R'
                sr = n
            else:
                answer += hand[0].upper()
                if hand[0] == 'l':
                    sl = n
                else:
                    sr = n
    return answer

