import sys
input = sys.stdin.readline
a, b, c, d = map(int, input().split())
arr = list(map(int, input().split()))
res = [0, 0, 0]
for i in range(3):
    if 0 < arr[i] % (a + b) <= a: res[i] += 1
    if 0 < arr[i] % (c + d) <= c: res[i] += 1
print("\n".join(map(str, res)))