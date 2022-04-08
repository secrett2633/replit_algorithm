from collections import deque

# BFS 함수 정의
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    count = 0
    while queue:      
        # 큐에서 하나의 원소를 뽑아 출력
        x, y = queue.popleft()
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if nx <0 or ny < 0 or nx >= n or ny >= n:
            continue
          if graph[nx][ny] == 0:
            continue
          if graph[nx][ny] == 1 and not visited[nx][ny]:
            count += 1
            visited[nx][ny] = True
            queue.append((nx, ny))
    return count
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)

n = int(input())
graph = []
visited = [[False] * (n+1) for i in range(n+1)]
for i in range(n):
  graph.append(list(map(int, input())))
dx = [-1, 1, 0, 0]
dy = [0, 0 , -1, 1]
# 정의된 BFS 함수 호출
list1 = []
for i in range(n):
  for j in range(n):
    a = bfs(i, j)
    if a != 0:
      list1.append(a)
list1.sort()
print(len(i))
for i in list1:
  print(i)