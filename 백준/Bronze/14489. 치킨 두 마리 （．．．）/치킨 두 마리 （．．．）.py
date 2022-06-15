import sys
from math import sqrt
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a, b = map(int, input().split())
c = int(input()) * 2
res = a + b
if res >= c:
  print(res - c)
else:
  print(res)
