import sys
input = sys.stdin.readline
a = list(map(int, input().split()))
x = [a[0]]
y = [a[1]]
for _ in range(2):
    a = list(map(int, input().split()))
    if a[0] in x: x.remove(a[0])
    else: x += [a[0]]
    if a[1] in y: y.remove(a[1])
    else: y += [a[1]]
print(x[0], y[0])