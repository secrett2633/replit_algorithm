import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [sorted(list(map(int, input().split()))) for _ in range(n)]
res = [0] * n
for i in range(m):
  tmp = []
  for k in range(n):
    tmp.append(arr[k].pop(-1))
  for k in range(n):
    if tmp[k] == max(tmp): res[k] += 1
ans = [(i + 1) for i in range(n) if res[i] == max(res)]
print(*ans)
  