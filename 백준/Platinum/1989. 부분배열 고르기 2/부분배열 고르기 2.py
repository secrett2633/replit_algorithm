import sys
input = sys.stdin.readline
def seg_find(start, end):
  if start == end:
    return [arr[start] ** 2, [start + 1, end + 1]]
  else:
    a = seg_find(start, (start + end) // 2)
    b = seg_find((start + end) // 2 + 1, end)
    if a > b: ans = a
    else: ans = b
    i = (start + end) // 2
    j = i + 1
    l = arr[i] + arr[j]    
    low = min(arr[i], arr[j])
    s = l * low
    res = [i + 1, j + 1]
    while start < i or end > j:
      if j == end or i > start and arr[i - 1] >= arr[j + 1]:
        i -= 1
        l += arr[i]
        low = min(low, arr[i])
        if s < l * low:
          s = l * low
          res = [i + 1, j + 1]
      else:
        j += 1
        l += arr[j]
        low = min(low, arr[j])
        if s < l * low:
          s = l * low
          res = [i + 1, j + 1]  
    if ans[0] > s:
      return ans
    else:
      return [s, res]
n = int(input())
arr = list(map(int, input().split()))
a, b = seg_find(0, n - 1)
print(a)
print(*b)