import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr = [0] + arr
partial_sum = [0] * len(arr)
for i in range(1, len(arr)):
    partial_sum[i] = partial_sum[i-1] + arr[i]

for a in range(m):
    i, j = map(int, input().split())
    print(partial_sum[j] - partial_sum[i - 1])
  