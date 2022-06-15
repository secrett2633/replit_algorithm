import sys
input = sys.stdin.readline
n = int(input())
result = 1
while n > 0:
  result *= n
  n -= 1

cnt = 0

for i in range(len(str(result)) - 1, -1, -1):
  if str(result)[i] == "0":
    cnt += 1
  else:
    break
print(cnt)