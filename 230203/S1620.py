import sys

n, m = map(int,input().split())

pokemon = {}

for i in range(1, n+1):
    p = sys.stdin.readline().strip()
    pokemon[i] = p
    pokemon[p] = i 

for _ in range(m):
    answer = sys.stdin.readline().strip()
    if answer.isdigit():
        print(pokemon[int(answer)])
    else:
        print(pokemon[answer])

    