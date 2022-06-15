import sys
#sys.setrecursionlimit(10 ** 6)
#from collections import deque
import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n = 10000
array = [True for i in range(n + 1)] 
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2 
        while i * j <= n:
            array[i * j] = False
            j += 1

t = int(input())
for _ in range(t):
  a = int(input())
  temp = []
  for i in range(2, math.ceil((a + 1) / 2)):
    if array[i] and array[a - i]:
      temp.append([a - 2 * i, i, a - i])
  temp.sort()
  print(temp[0][1], temp[0][2])