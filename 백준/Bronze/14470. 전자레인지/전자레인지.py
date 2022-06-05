import sys
from math import sqrt
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
res = 0
while a < 0:
  res += c
  a += 1
if a == 0:
  res += d
while a < b:
  res += e
  a += 1
print(res)