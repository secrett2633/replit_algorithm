import sys
input = sys.stdin.readline
n = int(input())
res = [6, 15, 35, 77, 143, 221, 323, 437, 667, 899, 1147, 1517, 1763, 2021, 2491, 3127, 3599, 4087, 4757, 5183, 5767, 6557, 7387, 8633, 9797, 10403]
for i in res:
  if i > n:
    print(i)
    exit(0)