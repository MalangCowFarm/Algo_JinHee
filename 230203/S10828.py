import sys
n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    msg = sys.stdin.readline().split()

    if msg[0] == 'push':
        stack.append(msg[1])
    elif msg[0] == 'pop':   # 리스트 맨 마지막 요소 리턴 후 그 요소 삭제
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif msg[0] == 'size':
        print(len(stack))
    elif msg[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif msg[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

