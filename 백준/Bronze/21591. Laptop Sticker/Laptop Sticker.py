import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
wc, hc, ws, hs = map(int, input().split())
if wc - 2 >= ws and hc - 2 >= hs:
  print(1)
else:
  print(0)