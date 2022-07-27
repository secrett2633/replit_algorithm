import sys
input = sys.stdin.readline
s = input().rstrip()
n = int(input())
arr = [input().rstrip() for _ in range(n)]
arr.sort()
result = -1
for i in range(n):
  res = []
  for j in ["L", "O", "V", "E"]:
    res.append(arr[i].count(j) + s.count(j))
  cnt = 1
  for j in range(3):
    for k in range(j + 1, 4):
      cnt *= (res[j] + res[k])
  cnt %= 100
  if cnt > result: result = cnt; answer = arr[i]
print(answer)