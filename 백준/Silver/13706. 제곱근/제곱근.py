import sys
input = sys.stdin.readline
n = int(input())
left = 0
right = n
while left <= right:
  mid = (left + right) // 2
  if mid * mid > n:
    right = mid
  elif mid * mid < n:
    left = mid + 1
  else:
    print(mid)
    exit(0)