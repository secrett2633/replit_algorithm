import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n = int(input())
k = int(input())
res = 0
if n > k + 60:
  n -= k + 60
  res += (k + 60) * 1500 + n * 3000
else:
  res += n * 1500
print(res)