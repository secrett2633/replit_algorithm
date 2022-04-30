#root를 저장하는 Vroot 배열을 생성한다. (여기서 root는 연결요소중 가장 작은 값, 처음에는 자기 자신을 저장)
#간선들(Elist)을 가중치 기준으로 정렬한다.
#간선들이 이은 두 정점을 find함수를 통해 두 root(sRoot, eRoot)를 찾는다.
#두 root가 다르다면 큰 root값을 작은 root값으로 만들어 연결되게 해준다.
#가중치를 더한다.

import sys
input = sys.stdin.readline

V, E = map(int, input().split())
Vroot = [i for i in range(V+1)]
Elist = [list(map(int, input().split())) for _ in range(E)]
Elist.sort(key=lambda x: x[2])


def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]


answer = 0
for s, e, w in Elist:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        
        answer += w

print(answer)