import sys
input = sys.stdin.readline
t = int(input())
q = []
max_distance = 0
for i in range(t):
  a, b = map(int, input().split())
  max_distance = max(max_distance, b - a)
  q.append(b - a)
now = 0
distance = [0]
while distance[-1] < max_distance:
  now += 1
  distance.append(distance[-1] + now)
  distance.append(distance[-1] + now)
for i in q:
  for j in range(1, len(distance)):
    if i <= distance[j]:
      print(j)
      break      