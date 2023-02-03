T = int(input())
for _ in range(T):     # T만큼 test 개수 입력 받기 
    k = int(input())   # 층수
    n = int(input())   # 호수

    people = []              # 0층 거주민 수 
    for i in range(n):
        people.append(i+1)   # [1, 2, 3, 4, ...k]

    for i in range(k):  
        for j in range(1,n): # k층 n호 사람 수 = k-1층 호 + k층 n-1호  
            people[j] += people[j-1]
    
    print(people[-1])