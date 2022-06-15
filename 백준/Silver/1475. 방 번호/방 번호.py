import sys
import math
input = sys.stdin.readline
n = input().rstrip()
cnt = [0] * 10
for i in n:
  if i == "9":
    cnt[6] += 1
  else:
    cnt[int(i)] += 1
cnt[6] = math.ceil(cnt[6] / 2)
print(max(cnt))
