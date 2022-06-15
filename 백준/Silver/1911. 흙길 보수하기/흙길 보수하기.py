import sys
from math import ceil
n, length = map(int, sys.stdin.readline().split())
location = []
for i in range(n):
      a, b = sys.stdin.readline().split()
      location.append([int(a), int(b)])
location.sort()
now = 0
wood = 0
for i in range(n):
      if now >= location[i][1]:
            continue
      if now < location[i][0]:
            wood += 1
            now = location[i][0] + length
      if now < location[i][1]:
            temp = ceil((location[i][1] - now) / length)
            now += (temp * length)
            wood += temp
print(wood)