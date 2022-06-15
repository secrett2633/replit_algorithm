import sys
input = sys.stdin.readline
n = int(input())
a, b, c = map(int, input().split())
visited_max = [a, b, c]
visited_min = [a, b, c]
max_temp = [0, 0, 0]
min_temp = [0, 0, 0]
for i in range(1, n):
  a, b, c = map(int, input().split())
  max_temp[0] = max(visited_max[0], visited_max[1]) + a
  max_temp[1] = max(visited_max[0], visited_max[1], visited_max[2]) + b
  max_temp[2] = max(visited_max[1], visited_max[2]) + c
  min_temp[0] = min(visited_min[0], visited_min[1]) + a
  min_temp[1] = min(visited_min[0], visited_min[1], visited_min[2]) + b
  min_temp[2] = min(visited_min[1], visited_min[2]) + c
  visited_max = [max_temp[0], max_temp[1], max_temp[2]]
  visited_min = [min_temp[0], min_temp[1], min_temp[2]]
print(str(max(visited_max)) + " " + str(min(visited_min)))