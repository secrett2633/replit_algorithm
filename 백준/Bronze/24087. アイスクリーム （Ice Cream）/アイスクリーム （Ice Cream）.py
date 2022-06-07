import sys
import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
s = int(input())
a = int(input())
b = int(input())
res = 250
if s - a > 0:
  res += math.ceil((s - a) / b) * 100
print(res)

  