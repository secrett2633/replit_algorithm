import sys
import math
input = sys.stdin.readline
def dfs(x):
    if visited[Y.index(x)]: 
        return False
    visited[Y.index(x)] = True
    for y in Y: 
        if array[x + y]: #x와 y값을 더한 값이 소수일때 
            if y not in matched or dfs(matched[y]): #y값이 아직 사용되지 않았을때, 사용되었다면 사용되었을때의 x값을 dfs에 넣음
                matched[y] = x
                return True
    return False
N = int(input())
X = list(map(int, input().split()))
#소수 판별을 하여 인덱스를 활용하여 소수 판별 가능
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
    if i == X[0]: 
        continue
    if array[X[0] + i]:
        if N == 2:
            answers.append(i)
            break
        Y = [x for x in X if x not in [X[0], X[X.index(i)]]] #첫번째 값과 더할값을 제외하여 리스트 생성
        matched = {}
        for y in Y:
            visited = [False for _ in range(len(Y))]
            dfs(y)
    if N != 2 and len(matched) == N - 2: #N-2개의 값이 매칭이 됬다면 모든 수가 매칭이 되었다는 뜻
      answers.append(i)
if not answers:
    answers.append(-1)
print(' '.join(list(map(str, sorted(answers)))))