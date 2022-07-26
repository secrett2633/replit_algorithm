import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
now = 100000000000000
cnt = 0
for i in range(n):
  if arr[i][1] < now: cnt += 1; now = arr[i][1]
print(cnt)