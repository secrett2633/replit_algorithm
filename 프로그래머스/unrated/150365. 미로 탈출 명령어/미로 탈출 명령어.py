def solution(n, m, x, y, r, c, k):
    from collections import deque
    answer = ["u","r","l","d"]
    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]
    q = deque([[x, y, 0, ""]])
    if abs(x - r) + abs(y - c) > k: return "impossible"
    while q:
        nx, ny, cnt, s = q.pop()
        if cnt == k:
            if nx == r and ny == c: return s
            continue
        if abs(nx - r) + abs(ny - c) > k - cnt: continue
        if (k - cnt - (abs(nx - r) + abs(ny - c))) % 2 == 1: continue
        for i in range(4):
            nnx, nny = nx + dx[i], ny + dy[i]
            if 0 < nnx <= n and 0 < nny <= m:
                q.append([nnx, nny, cnt + 1, s + answer[i]])
    return "impossible"