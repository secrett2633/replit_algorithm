def solution(x, y, n):
    from collections import deque
    q = deque([[0, x]])
    visited = [0] * (y + 1)
    while q:
        cnt, now = q.popleft()
        if visited[now]: continue
        visited[now] = 1
        if now == y: return cnt
        if now + n <= y: q.append([cnt + 1, now + n])
        if now * 2 <= y: q.append([cnt + 1, now * 2])
        if now * 3 <= y: q.append([cnt + 1, now * 3])
    return -1