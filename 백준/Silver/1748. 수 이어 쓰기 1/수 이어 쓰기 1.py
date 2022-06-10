import sys
#from collections import deque
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n = int(input())
res = 0
for i in range(9, 0, -1):
  if n >= 10 ** (i - 1):
    res += (n - 10 ** (i - 1) + 1) * i
    n -= (n - 10 ** (i - 1) + 1)
print(res)
