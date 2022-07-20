n = int(input())
arr = list(map(int, input().split()))
cnt = 0
res = 0
for i in arr:  
  if i == 1: cnt += 1; res += cnt
  else: cnt = 0
print(res)