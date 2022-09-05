import sys
input = sys.stdin.readline
w, h, x, y, p = map(int, input().split())
res = 0
for _ in range(p):
    a, b = map(int, input().split())
    if ((x - a) ** 2 + (y - b + h // 2) ** 2 <= (h // 2) ** 2) or (x <= a <= x + w and y <= b <= y + h) or ((x - a + w) ** 2 + (y - b + h // 2) ** 2 <= (h // 2) ** 2): res += 1
print(res)