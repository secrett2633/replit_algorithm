import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a, b, c = list(map(int, input().split()))
cnt = 0
while a < b:
  a += c
  cnt += 1
print(cnt)
