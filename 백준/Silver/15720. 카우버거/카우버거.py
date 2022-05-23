import sys
from itertools import combinations
input = sys.stdin.readline
b, c, d = map(int, input().split())
ham = sorted(list(map(int, input().split())))
side = sorted(list(map(int, input().split())))
drink = sorted(list(map(int, input().split())))
print(sum(ham) + sum(side) + sum(drink))
res = 0
while b > 0 and c > 0 and d > 0:
  res += int((ham.pop(-1) + side.pop(-1) + drink.pop(-1)) * 0.9)
  b -= 1
  c -= 1
  d -= 1
res += (sum(ham) + sum(side) + sum(drink))
print(res)