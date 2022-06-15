import sys
input = sys.stdin.readline
x, y, w, s = map(int, input().split())
a = (x + y) * w
if (x + y) % 2 == 0:
    b = max(x, y) * s
else:
    b = (max(x, y) - 1) * s + w
c = (min(x, y) * s) + ((max(x, y) - min(x, y)) * w)
res = min(min(a, b), c)
print(res)