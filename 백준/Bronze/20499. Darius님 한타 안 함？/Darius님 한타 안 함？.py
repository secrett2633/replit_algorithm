import sys
#from math import sqrt
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
k, d, a = map(int, input().rstrip().split("/"))
if k + a < d or d == 0:
  print("hasu")
else:
  print("gosu")