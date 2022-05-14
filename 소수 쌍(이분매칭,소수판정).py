import sys
import math
input = sys.stdin.readline
def dfs(x):
    if visited[Y.index(x)]: return False
    visited[Y.index(x)] = True
    for y in Y:
        if array[x + y]:
            if y not in matched or dfs(matched[y]):
                matched[y] = x
                return True
    return False
N = int(input())
X = list(map(int, input().split()))
array = [True for i in range(2001)]
for i in range(2, int(math.sqrt(2000)) + 1): 
    if array[i] == True: 
        j = 2 
        while i * j <= 2000:
            array[i * j] = False
            j += 1
answers = []
for i in X:
    matched = {}
    if i == X[0]: continue
    if array[X[0] + i]:
        if N == 2:
            answers.append(i)
            break
        Y = [x for x in X if x not in [X[0], X[X.index(i)]]]
        matched = {}
        for y in Y:
            visited = [False for _ in range(len(Y))]
            dfs(y)
    if N != 2 and len(matched) == N - 2: 
      answers.append(i)
if not answers:
    answers.append(-1)
print(' '.join(list(map(str, sorted(answers)))))