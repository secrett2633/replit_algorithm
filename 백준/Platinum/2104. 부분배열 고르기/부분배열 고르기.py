import sys
input = sys.stdin.readline
def seg_find(start, end):
  if start == end:
    return arr[start] ** 2
  else:
    ans = max(seg_find(start, (start + end) // 2), seg_find((start + end) // 2 + 1, end))
    i = (start + end) // 2
    j = i + 1
    l = arr[i] + arr[j]    
    low = min(arr[i], arr[j])
    s = l * low
    while start < i or end > j:
      if j == end or i > start and arr[i - 1] >= arr[j + 1]:
        i -= 1
        l += arr[i]
        low = min(low, arr[i])
        s = max(s, l * low)
      else:
        j += 1
        l += arr[j]
        low = min(low, arr[j])
        s = max(s, l * low)    
    return max(ans, s)
n = int(input())
arr = list(map(int, input().split()))
print(seg_find(0, n - 1))