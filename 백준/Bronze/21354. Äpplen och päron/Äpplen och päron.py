import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a, p = map(int, input().split())
if a * 7 > p * 13:
  print("Axel")
elif a * 7 < p * 13:
  print("Petra")
else:
  print("lika")