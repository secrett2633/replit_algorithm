import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
  a, b = input().split()
  temp = list(map(int, (a, b)))
  arr.append(temp)
arr.sort(key = lambda x:(x[1], x[0]))

for a, b in arr:
  print(str(a) + " " + str(b))