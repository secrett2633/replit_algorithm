import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a, b, c = list(map(int, input().split()))
if a == b != c:
  print("C")
elif a != b == c:
  print("A")
elif a == c != b:
  print("B")
else:
  print("*")