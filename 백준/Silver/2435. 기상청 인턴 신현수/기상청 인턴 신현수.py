import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = -10000000000
for i in range(n - k + 1):
  res = max(res, sum(arr[i:i+k]))
print(res)