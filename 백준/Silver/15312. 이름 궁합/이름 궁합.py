import sys
from itertools import permutations
import math
input = sys.stdin.readline
cache = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
s1 = input().rstrip()
s2 = input().rstrip()
res = []
for i in range(len(s1)):
  res.append(cache[ord(s1[i]) - 65])
  res.append(cache[ord(s2[i]) - 65])
while len(res) > 2:
  tmp = []
  for i in range(len(res) - 1):
    tmp.append((res[i] + res[i + 1]) % 10)
  res = tmp[::]
print(str(res[0]) + str(res[1]))