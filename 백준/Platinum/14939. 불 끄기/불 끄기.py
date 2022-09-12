import copy
import sys
input = sys.stdin.readline
def solve(graph, i, j):
    if i - 1 >= 0: graph[i - 1][j] = 1 - graph[i - 1][j]
    if j - 1 >= 0: graph[i][j - 1] = 1 - graph[i][j - 1]
    if i + 1 < 10: graph[i + 1][j] = 1 - graph[i + 1][j]
    if j + 1 < 10: graph[i][j + 1] = 1 - graph[i][j + 1]
    graph[i][j] = 1 - graph[i][j]
    return graph
arr = [list(input().rstrip()) for _ in range(10)]
for i in range(10):
    for j in range(10):
        if arr[i][j] == "#": arr[i][j] = 0
        else: arr[i][j] = 1
arr1 = []
arr1.append([copy.deepcopy(arr), 0])
for i in range(10):
    for j in range(10):
        tmp = []
        for k in range(len(arr1)): 
            if i == 0:
                tmp.append([copy.deepcopy(arr1[k][0]), arr1[k][1]])
                tmp.append([solve(arr1[k][0], i, j), arr1[k][1] + 1])
            elif not arr1[k][0][i - 1][j]:
                tmp.append([arr1[k][0], arr1[k][1]])             
            elif arr1[k][0][i - 1][j]:                
                tmp.append([solve(arr1[k][0], i, j), arr1[k][1] + 1])                      
        arr1 = tmp
ans = 101
for i in range(len(arr1)):
    if sum(arr1[i][0][9]) == 0: ans = min(ans, arr1[i][1])
print(ans if ans != 101 else -1)