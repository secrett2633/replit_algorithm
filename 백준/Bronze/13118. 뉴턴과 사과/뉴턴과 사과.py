a = list(map(int, input().split()))
x, y, r = map(int, input().split())
if x in a: print(a.index(x) + 1)
else: print(0)