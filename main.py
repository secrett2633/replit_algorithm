import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
new_arr = [[0] * (m + 6) for _ in range(n + 6)]
for i in range(n):
  arr.append(list(map(int, input().split())))
for i in range(n):
  for j in range(m):
    new_arr[i + 3][j + 3] = arr[i][j]

shapes = [[(0, 0), (0, 1), (1, 0), (1, 1)], [(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (1, 0), (1, 1), (2, 1)], [(0, 0), (1, 0), (1, -1), (2, -1)], [(0, 0), (0, 1), (1, 1), (1, 2)], [(0, 0), (0, 1), (-1, 1), (-1, 2)], [(0, 0), (0, 1), (0, 2), (1, 2)], [(0, 0), (1, 0), (2, 0), (2, -1)], [(0, 0), (1, 0), (1, 1), (1, 2)], [(0, 0), (0, -1), (1, -1), (2, -1)], [(0, 0), (-1, 0), (-1, 1), (-1, 2)], [(0, 0), (1, 0), (2, 0), (2, 1)], [(0, 0), (0, 1), (0, 2), (-1, 2)], [(0, 0), (0, 1), (1, 1), (2, 1)], [(0, 0), (0, 1), (-1, 1), (0, 2)], [(0, 0), (1, 0), (1, 1), (2, 0)], [(0, 0), (0, 1), (1, 1), (0, 2)], [(0, 0), (1, 0), (1, -1), (2, 0)]]
result = 0
for i in range(3, n + 3):
  for j in range(3, m + 3):
    #1번
    for direction in shapes:
      temp = 0
      for a, b in direction:
        temp += new_arr[a + i][b + j]
      result = max(result, temp)
print(result)