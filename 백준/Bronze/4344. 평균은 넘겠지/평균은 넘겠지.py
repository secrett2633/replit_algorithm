import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
  a = list(map(int, input().split()))
  count = 0
  avg = (sum(a) - a[0]) / a[0]
  for i in range(1, a[0] + 1):
    if a[i] > avg:
      count += 1
  print("{:.3f}%".format(round((count / a[0]) * 100, 3)))