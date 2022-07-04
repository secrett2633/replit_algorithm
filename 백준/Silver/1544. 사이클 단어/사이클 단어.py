import sys
input = sys.stdin.readline
n = int(input())
arr = [input().rstrip() for _ in range(n)]
cnt = n
visited = []
i = 0
while i < len(arr):
  j = i + 1
  while j < len(arr):
    if arr[i] in arr[j] * 2 and len(arr[i]) == len(arr[j]):
      cnt -= 1
      del arr[j]
    else: j += 1
  i += 1
print(cnt)