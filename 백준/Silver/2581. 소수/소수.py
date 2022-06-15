import sys
import math
input = sys.stdin.readline
m = int(input())
n = int(input())

array = [True for i in range(n + 1)] 
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2 
        while i * j <= n:
            array[i * j] = False
            j += 1
res = 0
res1 = 0
array[1] = False
for i in range(m, n + 1):
    if array[i]:
      res += i
      if res1 == 0:
        res1 = i
if res != 0:
  print(res)
  print(res1)
else:
  print(-1)