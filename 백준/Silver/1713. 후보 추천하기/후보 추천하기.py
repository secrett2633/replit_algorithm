import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
arr = list(map(int, input().split()))
stu = [0] * 101
q = []
for i in arr:
  stu[i] += 1
  if i in q: continue
  if len(q) == n:
    cnt = 1001
    for k in range(n):
      cnt = min(cnt, stu[q[k]])
    for k in range(n):
      if stu[q[k]] == cnt:
        stu[q[k]] = 0
        del q[k]
        break
  q.append(i)
print(*sorted(q))