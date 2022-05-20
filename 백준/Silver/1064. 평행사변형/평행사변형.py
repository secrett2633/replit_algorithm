import sys
input = sys.stdin.readline
ax, ay, bx, by, cx, cy = map(int, input().split())
answer = 0.0
if ax == bx == cx or ay == by == cy:
    answer = -1.0
elif ay-by != 0 and ay-cy != 0 and by-cy != 0 and (ax-bx)/(ay-by) == (bx-cx)/(by-cy) == (ax-cx)/(ay-cy):
    answer = -1.0
else :
    a = ((ax - bx) ** 2 + (ay - by) ** 2) ** (1/2)
    b = ((bx - cx) ** 2 + (by - cy) ** 2) ** (1/2)
    c = ((cx - ax) ** 2 + (cy - ay) ** 2) ** (1/2)
    answer = (max(a, b, c) - min(a, b, c)) * 2
print(answer)