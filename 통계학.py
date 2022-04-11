import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
  arr.append(int(input()))
arr.sort()
print(round(sum(arr) / n))
print(arr[n // 2])
counter = Counter(arr)
if len(counter) > 1:
  a, b = counter.most_common(2)
  print(b[0] if a[1] == b[1] else a[0])
else:
  print(arr[0])
print(max(arr) - min(arr))