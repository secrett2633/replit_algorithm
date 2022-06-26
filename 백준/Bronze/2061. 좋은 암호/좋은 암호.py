import sys
input = sys.stdin.readline
k, l = list(map(int, input().split()))
for i in range(2, l):
  if k % i == 0: print("BAD", str(i)); exit(0)
print("GOOD")