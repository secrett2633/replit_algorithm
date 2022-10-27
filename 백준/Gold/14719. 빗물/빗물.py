import sys
input = sys.stdin.readline
h, w = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
for i in range(1, w - 1):
    res += max(0, min(max(arr[:i]), max(arr[i + 1:])) - arr[i])
print(res)