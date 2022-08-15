import sys
from itertools import product
n = int(input())
arr = sys.stdin.read()
tmp = ""
res = 0
for i in arr:
  if i.isdigit(): tmp += i
  elif i == " ": res += int(tmp); tmp = ""
res += int(tmp)
print(res - (n * (n - 1) // 2))