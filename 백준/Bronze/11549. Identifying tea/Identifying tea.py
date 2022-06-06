import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
t = int(input())
arr = list(map(int, input().split()))
res = 0
for i in arr:
  if i == t:
    res += 1
print(res)