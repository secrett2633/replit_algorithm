import sys
input = sys.stdin.readline
n = int(input())
arr = [[int(input()), i] for i in range(n)]
arr1 = sorted(arr)
res = 0
for i in range(n):
  res = max(res, arr1[i][1] - arr[i][1])
print(res + 1)