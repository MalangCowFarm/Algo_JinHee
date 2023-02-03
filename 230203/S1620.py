# 런타임 에러로 포기합니다.. 
import sys
input = sys.stdin.readline 

n, m = map(int,input().split())

pokemon = {}

for i in range(1, n+1):
    p = input()
    pokemon[i] = p
    pokemon[p] = i 

for _ in range(m):
    answer = input()
    if answer.isdigit():
        print(pokemon[int(answer-1)])
    else:
        print(pokemon[answer]+1)



# pokemon = []   시간초과 
# for _ in range(n): # 0 1 2 3 ... 25
#     p = input()
#     pokemon.append(p)

# for _ in range(m):
#     answer = input()
#     if answer.isdigit():
#         print(pokemon[int(answer)-1])
#     else:
#         print(pokemon.index(answer)+1)

    