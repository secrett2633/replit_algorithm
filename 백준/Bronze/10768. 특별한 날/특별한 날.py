import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a = int(input())
b = int(input())
if a == 2 and b == 18:
  print("Special")
elif a < 2 or (a == 2 and b < 18):
  print("Before")
else:
  print("After")