import sys
#from collections import deque
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
res = 0
for i in range(n):
  res += (a[i] * b[n - i - 1])
print(res)