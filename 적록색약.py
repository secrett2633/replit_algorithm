from collections import deque

# BFS 함수 정의
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:      
        # 큐에서 하나의 원소를 뽑아 출력
        x, y = queue.popleft()
        now = graph[x][y]
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if nx <0 or ny < 0 or nx >= n or ny >= n:
            continue
          if visited[nx][ny] == True:
            continue
          if graph[nx][ny] == now:
            queue.append((nx, ny))
            visited[nx][ny] = True
    return 1

def bfs1(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:      
        # 큐에서 하나의 원소를 뽑아 출력
        x, y = queue.popleft()
        now = graph[x][y]
        if now == "B":
          for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or ny < 0 or nx >= n or ny >= n:
              continue
            if visited[nx][ny] == True:
              continue
            if graph[nx][ny] == now:
              queue.append((nx, ny))
              visited[nx][ny] = True
        else:
          for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or ny < 0 or nx >= n or ny >= n:
              continue
            if visited[nx][ny] == True:
              continue
            if graph[nx][ny] == "R" or graph[nx][ny] == "G":
              queue.append((nx, ny))
              visited[nx][ny] = True
    return 1
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)

n = int(input())
graph = []
for i in range(n):
  graph.append(list(input()))
visited = [[False] * n for i in range(n)] 
dx = [-1, 1, 0, 0]
dy = [0, 0 , -1, 1]
# 정의된 BFS 함수 호출
cnt = 0
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      cnt += bfs(i, j)
visited = [[False] * n for i in range(n)] 
cnt1 = 0
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      cnt1 += bfs1(i, j)
print(str(cnt) + " " + str(cnt1))