import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(n)]
n, m = map(int, input().split())
arr2 = [list(map(int, input().split())) for _ in range(n)]

answer = [[0] * (len(arr2[0])) for _ in range(len(arr1))]
for i in range(len(arr1)):
  for j in range(len(arr2[0])):
    for b in range(len(arr2)):
      answer[i][j] += arr1[i][b] * arr2[b][j]
for i in answer:
  print(*i)