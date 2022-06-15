import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  n = int(input())
  clothes = dict()
  for i in range(n):
    a, b = input().rstrip().split()
    if b in clothes:
      clothes[b] += 1
    else:
      clothes[b] = 1
  cnt = 1
  for i in clothes:
    cnt *= (clothes[i] + 1)
  print(cnt - 1)