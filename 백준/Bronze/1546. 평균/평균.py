import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
good = max(a)

for i in range(n):
  a[i] = a[i] / good * 100
print(sum(a) / n)