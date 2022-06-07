import sys
import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a = int(input())
res = a * 0.01 + 25
if res < 100:
  print("100.00")
elif res > 2000:
  print("2000.00")
else:
  print("%.2f" % res)