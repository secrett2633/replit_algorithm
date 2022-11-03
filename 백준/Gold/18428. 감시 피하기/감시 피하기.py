import sys
from collections import deque
import heapq
input = sys.stdin.readline
n = int(input())
arr = [list(input().rstrip().split()) for _ in range(n)]
ba = []
st = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == "X": ba.append([i, j])
        elif arr[i][j] == "S": st.append([i, j])
for i in range(len(ba) - 2):
    arr[ba[i][0]][ba[i][1]] = "B"
    for j in range(i + 1, len(ba) - 1):
        arr[ba[j][0]][ba[j][1]] = "B"
        for k in range(j + 1, len(ba)):
            arr[ba[k][0]][ba[k][1]] = "B"
            flag = True
            for x, y in st:
                for z in range(y + 1, n):
                    if arr[x][z] == "T": flag = False; break
                    elif arr[x][z] == "B": break
                for z in range(y - 1, -1, -1):
                    if arr[x][z] == "T": flag = False; break
                    elif arr[x][z] == "B": break
                for z in range(x + 1, n):
                    if arr[z][y] == "T": flag = False; break
                    elif arr[z][y] == "B": break
                for z in range(x - 1, -1, -1):
                    if arr[z][y] == "T": flag = False; break
                    elif arr[z][y] == "B": break
            if flag: print("YES"); exit(0)
            arr[ba[k][0]][ba[k][1]] = "X"
        arr[ba[j][0]][ba[j][1]] = "X"
    arr[ba[i][0]][ba[i][1]] = "X"
print("NO")