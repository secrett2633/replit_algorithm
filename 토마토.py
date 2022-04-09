from collections import deque

# BFS 함수 정의
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([])
    for i in range(m):
      for j in range(n):
        if graph[i][j] == 1:
            queue.append([i, j])
    # 큐가 빌 때까지 반복
    while queue:      
        # 큐에서 하나의 원소를 뽑아 출력
        x, y = queue.popleft()
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if nx <0 or ny < 0 or nx >= m or ny >= n:
            continue
          if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))
            
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)

n, m = map(int, input().split())
graph = []
for i in range(m):
  graph.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0 , -1, 1]
# 정의된 BFS 함수 호출

          
bfs(0, 0)
cnt = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(i))
# 처음 시작을 1로 표현했으니 1을 빼준다.
print(cnt - 1)