import sys
input = sys.stdin.readline

def solve(arr):
  arr.sort(key=lambda x:(x[0],x[1]))
  if len(arr) <=2: return arr
  temp = []
  for i in arr:
    while len(temp) >= 2 and ccw(temp[-2], temp[-1], i) <= 0: temp.pop()
    temp.append(i)
  tmp = []
  for i in reversed(arr):
    while len(tmp) >= 2 and ccw(tmp[-2], tmp[-1], i) <= 0: tmp.pop()
    tmp.append(i)
  return temp[:-1] + tmp[:-1]

def calc(p1, p2):
  return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def ccw(p1, p2, p3):
  return p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1] - p2[1])

def cccw(p1, p2, p3, p4):
  tmp = p4[:]
  tmp[0] -= (p3[0] - p2[0])
  tmp[1] -= (p3[1] - p2[1])
  return ccw(p1, p2, tmp)

for _ in range(int(input())):
  n = int(input())
  dots = [[int(i) for i in input().split()] for _ in range(n)]
  graph = solve(dots)
  N = len(graph)
  d = 0
  j = 1
  d1 = graph[0]
  d2 = graph[1]
  for i in range(N):
    while j+1 != i and cccw(graph[i], graph[(i+1)%N], graph[j%N], graph[(j+1)%N]) > 0:
      if calc(graph[i], graph[j%N]) > d:
        d1 = graph[i]
        d2 = graph[j%N]
        d = calc(graph[i], graph[j%N])
      j += 1

    if calc(graph[i], graph[j%N]) > d:
      d1 = graph[i]
      d2 = graph[j%N]
      d = calc(graph[i], graph[j%N])
  print(*d1, *d2)