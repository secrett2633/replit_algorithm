import sys
input = sys.stdin.readline
t = int(input())
a = []
for _ in range(t):  
  a.append(int(input()))
a.sort()
for i in a:
  print(i)