import sys
#from math import sqrt
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
s = input().rstrip()
if s[-1] == "0":
  print(int(s[:-2]) + 10)
else:
  print(int(s[:-1]) + int(s[-1]))