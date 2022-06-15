from collections import deque
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
n = int(input())
m = int(input())
graph = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = [0]

def dfs(v):
    # 현재 노드를 방문 처리
    visited[v] = True
    count[0] += 1
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
  
# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * (n + 1)

# 정의된 DFS 함수 호출

dfs(1)
print(count[0] - 1)