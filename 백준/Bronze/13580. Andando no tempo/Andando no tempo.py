import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a, b, c = list(map(int, input().split()))
if a + b - c == 0 or a + c - b == 0 or b + c - a == 0 or b - c - a == 0 or a - b == 0 or a - c == 0 or b - a == 0 or b - c == 0 or c - a == 0 or c - b == 0:
  print("S")
else:
  print("N")
