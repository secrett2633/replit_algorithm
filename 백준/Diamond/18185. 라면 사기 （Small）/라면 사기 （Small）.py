import sys
import heapq
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ans = 0
i = 0
while i < n:
  if i + 2 < n:
    if arr[i + 1] > arr[i + 2]:
      cnt = min(arr[i], arr[i + 1] - arr[i + 2])
      arr[i], arr[i + 1] = arr[i] - cnt, arr[i + 1] - cnt
      ans += (5 * cnt)
    cnt = min(arr[i], arr[i + 1], arr[i + 2])
    arr[i], arr[i + 1], arr[i + 2] = arr[i] - cnt, arr[i + 1] - cnt, arr[i + 2] - cnt
    ans += (cnt * 7)
  elif i + 1 < n:
    cnt = min(arr[i], arr[i + 1])
    arr[i], arr[i + 1] = arr[i] - cnt, arr[i + 1] - cnt
    ans += (cnt * 5)
  ans += (arr[i] * 3)  
  arr[i] = 0
  i += 1
print(ans)