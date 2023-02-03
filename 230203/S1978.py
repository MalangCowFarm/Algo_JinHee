n = int(input())
nums = list(map(int,input().split())) 
cnt = 0         # 총 개수 

for i in nums:  
    if i == 1:           # 1 != 소수 예외처리
        continue  
    elif i == 2:         # 2 일때 +=1 
        cnt += 1  
    else:   
        for j in range(2,i):    # 2부터 i-1까지 꺼내오기
            if i%j == 0 :       # 나누어 떨어지면 소수가 아님 
                break
            elif j == i-1:      
                cnt += 1
print(cnt)
