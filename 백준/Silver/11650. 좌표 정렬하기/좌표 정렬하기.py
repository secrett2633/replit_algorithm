from sys import stdin
input = stdin.readline
n = int(input())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))

arr.sort(key = lambda x:(x[0], x[1]))

for i in arr:
  print(str(i[0]) + " " + str(i[1]))