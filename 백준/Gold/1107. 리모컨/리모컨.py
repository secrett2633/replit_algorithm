import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
if m != 0:
  arr = list(map(int, input().split()))
else:
  arr = []
  
cnt = abs(n - 100)
for now in range(1000001):
  for i in range(len(str(now))):
    if int(str(now)[i]) in arr:
      break
    elif i == len(str(now)) - 1:
      cnt = min(cnt, abs(now - n) + len(str(now)))
print(cnt)