import sys
input = sys.stdin.readline
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    res = 0
    for _ in range(int(input())):
        cx, cy, r = map(int, input().split())
        a = (cx - x1) ** 2 + (cy - y1) ** 2 < r ** 2
        b = (cx - x2) ** 2 + (cy - y2) ** 2 < r ** 2
        if (a and not b) or (not a and b): res += 1 
    print(res)