import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
s = int(input())
m = int(input())
l = int(input())
if s + 2 * m + 3 * l >= 10:
  print("happy")
else:
  print("sad")