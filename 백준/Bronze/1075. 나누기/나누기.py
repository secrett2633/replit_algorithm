import sys
input = sys.stdin.readline
n = int(input().rstrip()[:-2] + "00")
f = int(input())
for i in range(100):
  if (n + i) % f == 0: print(i if i >= 10 else "0" + str(i)); break