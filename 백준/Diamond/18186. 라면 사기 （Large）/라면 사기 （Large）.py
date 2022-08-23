import sys
import heapq
input = sys.stdin.readline
n, b, c = list(map(int, input().split()))
arr = list(map(int, input().split()))
ans = 0
i = 0
if b > c:
  while i < n:
    if i + 2 < n:
      if arr[i + 1] > arr[i + 2]:
        cnt = min(arr[i], arr[i + 1] - arr[i + 2])
        arr[i], arr[i + 1] = arr[i] - cnt, arr[i + 1] - cnt
        ans += ((b + c) * cnt)
      cnt = min(arr[i], arr[i + 1], arr[i + 2])
      arr[i], arr[i + 1], arr[i + 2] = arr[i] - cnt, arr[i + 1] - cnt, arr[i + 2] - cnt
      ans += (cnt * (b + 2 * c))
    elif i + 1 < n:
      cnt = min(arr[i], arr[i + 1])
      arr[i], arr[i + 1] = arr[i] - cnt, arr[i + 1] - cnt
      ans += (cnt * (b + c))
    ans += (arr[i] * b)  
    arr[i] = 0
    i += 1
else:
  ans = sum(arr) * b
print(ans)