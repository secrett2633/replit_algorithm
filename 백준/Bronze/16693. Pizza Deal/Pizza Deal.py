import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a1, p1 = map(int, input().split())
r1, p2 = map(int, input().split())
res1 = p1 / a1 
res2 = p2 / (r1 * r1 * 3.14159265359)
if res1 < res2:
  print("Slice of pizza")
else:
  print("Whole pizza")