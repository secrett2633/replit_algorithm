import sys
input = sys.stdin.readline
from collections import deque

# BFS 함수 정의
def bfs(start, cnt):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((start, cnt))
    # 현재 노드를 방문 처리
    
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v, cnt = queue.popleft()
        if v == 100:
          print(cnt)
          return
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in range(1, 7):
          if v + i in graph:
            temp = graph1[graph.index(v + i)]
            if temp < 101 and not visited[temp]:
              queue.append((temp, cnt + 1))
              visited[temp] = True
          elif v + i < 101 and not visited[v + i]:
            queue.append((v + i, cnt + 1))
            visited[v + i] = True
          
                
                

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
n, m = map(int, input().split())
graph = []
graph1 = []
for i in range(n):
  a, b = map(int, input().split())
  graph.append(a)
  graph1.append(b)
for i in range(m):
  a, b = map(int, input().split())
  graph.append(a)
  graph1.append(b)
visited = [False] * (101)
# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
# 정의된 BFS 함수 호출
bfs(1, 0)