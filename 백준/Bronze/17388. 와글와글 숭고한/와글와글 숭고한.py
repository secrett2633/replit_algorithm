import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
s, k, h = map(int, input().split())
if s + k + h >= 100:
  print("OK")
else:
  if s == min(s, k, h):
    print("Soongsil")
  elif k == min(s, k, h):
    print("Korea")
  else:
    print("Hanyang")