import sys
#from collections import deque
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n = int(input())
res = [0] * 21
for i in range(1, n + 1):
  a, b = list(map(int, input().split()))
  res[a + i] = max(max(res[:i + 1]) + b, res[a + i])
print(max(res[:n + 2]))
