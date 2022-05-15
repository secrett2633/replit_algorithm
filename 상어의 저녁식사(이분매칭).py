import sys
input = sys.stdin.readline

def dfs(x):
    if visited[x]:
        return False    
    visited[x] = 1    
    for i in range(1, n+1):
        if check[x][i]:
            if not eat[i] or dfs(eat[i]):
                eat[i] = x
                return True
    return False    

n = int(input())
arr = [[]] + [list(map(int, input().split())) for _ in range(n)]
check = [[0] * (n + 1) for _ in range(n + 1)]
eat = [0] * (n + 1) 
    
for i in range(1, n + 1):
    for j in range(1, n + 1):         
        if i == j or (arr[i][0] == arr[j][0] and arr[i][1] == arr[j][1] and arr[i][2] == arr[j][2] and i > j):
            continue            
        elif arr[i][0] >= arr[j][0] and arr[i][1] >= arr[j][1] and arr[i][2] >= arr[j][2]:
            check[i][j] = 1   

for i in range(2):
    for j in range(1, n + 1):
        visited = [0] * (n + 1)
        dfs(j) 

print(eat[1:].count(0))

