import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
s = int(input())
st = [list(map(int, input().split())) for _ in range(s)]
for a, b in st:
  if a == 1:
    i = b
    while i - 1 < n:
      if arr[i - 1] == 0: arr[i - 1] = 1
      else: arr[i - 1] = 0
      i += b
  else:
    i = 1
    b -= 1
    if arr[b] == 0: arr[b] = 1
    else: arr[b] = 0
    while b - i >= 0 and b + i < n:
      if arr[b - i] != arr[b + i]: break
      if arr[b - i] == 0: arr[b - i] = 1; arr[b + i] = 1
      else: arr[b - i] = 0; arr[b + i] = 0
      i += 1
print(*arr[:min(20, n)])
if n > 20: print(*arr[20:min(40, n)])
if n > 40: print(*arr[40:min(60, n)])
if n > 60: print(*arr[60:min(80, n)])
if n > 80: print(*arr[80:])