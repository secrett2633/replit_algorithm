from collections import deque

# BFS 함수 정의
def bfs(start):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append(start)
    # 현재 노드를 방문 처리
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()        
        if v == k:
          cnt[0] += 1
          continue
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in (v - 1, v + 1, v * 2):
          if 0 <= i and i <= 100000 and (graph[i] == graph[v] + 1 or graph[i] == 0):
            graph[i] = graph[v] + 1
            queue.append(i)
          
                
                
cnt = [0]
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
n, k = map(int, input().split())
graph = [0] * (100001)
# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
# 정의된 BFS 함수 호출
bfs(n)
print(graph[k])
print(cnt[0])