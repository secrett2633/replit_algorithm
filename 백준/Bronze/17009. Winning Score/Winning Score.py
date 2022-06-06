import sys
import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
res = 0
for i in range(3):
  res += int(input()) * (3 - i)
res1 = 0
for i in range(3):
  res1 += int(input()) * (3 - i)
if res > res1:
  print("A")
elif res < res1:
  print("B")
else:
  print("T")