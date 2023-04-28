n = int(input())
open, close = 600, 1320
lst = [(open,open),(close,close)]

for _ in range(n):
 s, e = input().split()
 s = int(s[:2])*60 + int(s[2:]) -10
 e = int(e[:2])*60 + int(e[2:]) +10
 lst.append((s,e))
lst.sort()


mx = 0
end = 600
for s,e in lst:
    mx = max(mx,s-end)
    end = max(end, e)

print(mx)


'''
첫 시도 
n = int(input())
open, close = 600, 1320
lst = [(close,0)]

for _ in range(n):
 s, e = input().split()
 s = int(s[:2])*60 + int(s[2:]) -10
 e = int(e[:2])*60 + int(e[2:]) +10
 lst.append((s,e))
lst.sort()


mx = 0
for s,e in lst:
    if s >= open:
        mx = max(mx,s-open)
    open = e

print(mx)
'''
