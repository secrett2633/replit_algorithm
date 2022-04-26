import sys
import math
input = sys.stdin.readline
m = int(input())
def recursive(now, cnt):
  if cnt == 1:
    return now % 1000000007
  if cnt % 2 == 0:
    temp = recursive(now, cnt // 2) 
    return temp * temp % 1000000007
  else:
    temp = recursive(now, cnt // 2)
    return temp * temp * now % 1000000007
result = 0
for i in range(m):
  n, s = map(int, input().split())
  result += (recursive(n // math.gcd(n, s), 1000000005) * (s // math.gcd(n, s))) % 1000000007
print(result % 1000000007)
    