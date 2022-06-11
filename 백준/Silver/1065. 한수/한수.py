import sys
#from collections import deque
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n = int(input())
if n < 100:
  print(n)
else:
  start = 100
  res = 99
  while start <= n and start != 1000:
    temp = str(start)
    if int(temp[0]) - int(temp[1]) == int(temp[1]) - int(temp[2]):
      res += 1
    start += 1
  print(res)
      