import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x:(100 - x[0], x[1]))
res = 0
for i in range(5, n):
  if arr[i][0] == arr[4][0]: res += 1
print(res)