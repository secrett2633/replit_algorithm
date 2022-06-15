import sys
input = sys.stdin.readline
n = int(input())
a = set()
for i in range(n):
  a.add(int(input()))
a = list(a)
a.sort(reverse = True)
print("\n".join(map(str, a)))