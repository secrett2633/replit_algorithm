import math
n = int(input())
s = input().rstrip()
cnt = 0
for i in range(n):
  if s[i] == 'C':
    cnt += 1
print(math.ceil(cnt / (n - cnt + 1)))