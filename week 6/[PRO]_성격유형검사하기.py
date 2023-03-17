'''
- 리스트로만 하려니까 헷갈려서 딕셔너리를 이용해보았다..
- 처음부터 유형에 따라 사전알파벳순으로 정렬하였다
'''

def solution(survey, choices):
    ans = ''
    personality = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(choices)):
        left = survey[i][0]
        right = survey[i][1]
        if choices[i] < 4:
            personality[left]+=(4 - choices[i])
        elif choices[i] > 4:
            personality[right]+=(choices[i] - 4)

    if personality['R'] >= personality['T']:
        ans += 'R'
    else:
        ans += 'T'

    if personality['C'] >= personality['F']:
        ans += 'C'
    else:
        ans += 'F'

    if personality['J'] >= personality['M']:
        ans += 'J'
    else:
        ans += 'M'

    if personality['A'] >= personality['N']:
        ans += 'A'
    else:
        ans += 'N'

    return ans