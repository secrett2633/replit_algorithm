import sys
input = sys.stdin.readline
def dfs(x):
    if visited[x]:
        return False    
    visited[x] = 1    
    for i in check[x]:
        if not eat[i] or dfs(eat[i]):
            eat[i] = x
            return True
    return False    

n, m, k = map(int, input().split())
check = [[]] + [list(map(int, input().split()))[1:] for _ in range(n)]
eat = [0] * (m + 1)
cnt = 0
for j in range(1, n + 1):
    visited = [0] * (n + 1)
    if dfs(j):
      cnt += 1
      
for j in range(1, n + 1):
  while k > 0:
    visited = [0] * (n + 1)
    if dfs(j):
      cnt += 1
      k -= 1   
    else:
      break
print(cnt) 