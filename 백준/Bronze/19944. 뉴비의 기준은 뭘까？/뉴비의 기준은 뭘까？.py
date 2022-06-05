import sys
#from math import sqrt
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
if m == 1 or m == 2:
  print("NEWBIE!")
elif m <= n:
  print("OLDBIE!")
else:
  print("TLE!")