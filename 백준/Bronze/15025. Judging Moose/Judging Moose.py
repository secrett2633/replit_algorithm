import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
l, r = map(int, input().split())
if l == r == 0:
  print("Not a moose")
elif l == r:
  print("Even " + str(l * 2))
else:
  print("Odd " + str(max(l, r) * 2))