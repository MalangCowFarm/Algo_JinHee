a, b = map(int, input().split())

aa = list(map(int, input().split()))
bb = list(map(int, input().split()))

print(2 * len(set(aa+bb))-len(aa)-len(bb))