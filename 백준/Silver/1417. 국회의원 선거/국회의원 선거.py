import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
res = 0
if n == 1:
  print("0")
else:
  while arr[0] <= max(arr[1:]):
    temp = max(arr[1:])
    for i in range(1, n):
      if arr[i] == temp:
        arr[i] -= 1
        break
    arr[0] += 1
    res += 1
  print(res)