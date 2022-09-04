import sys
input = sys.stdin.readline
k = int(input())
x1 = []
y1 = []
xy = [list(map(int, input().split())) for _ in range(6)]
x = 0
y = 0
cache = []
for i in range(6):
    a, b = xy[i]
    if a == 1: x += b
    elif a == 2: x -= b
    elif a == 3: y -= b
    else: y += b
    x1.append(x)
    y1.append(y)
    cache.append([x, y])
midx = sorted(x1)[2]
midy = sorted(y1)[2]
if [max(x1), max(y1)] not in cache: x, y = max(x1), max(y1)
elif [max(x1), min(y1)] not in cache: x, y = max(x1), min(y1)
elif [min(x1), max(y1)] not in cache: x, y = min(x1), max(y1)
else: x, y = min(x1), min(y1)
print(k * (abs((max(x1) - min(x1)) * (max(y1) - min(y1))) - abs((x - midx) * (y - midy))))