def solution(user_id, banned_id):
    answer = []
    from collections import deque
    cnt = [[0] * len(banned_id) for _ in range(len(user_id))]
    def check(users, banned):
        if len(users) != len(banned): return False
        for i in range(len(users)):
            if users[i] != banned[i] and banned[i] != "*": return False
        return True
    for i, user in enumerate(user_id):
        for j, ban in enumerate(banned_id):
            if check(user, ban): 
                cnt[i][j] += 1
    q = deque([[0, [0] * len(user_id)]])
    while q:
        j, visited = q.popleft()
        if j == len(banned_id):
            if visited not in answer:
                answer.append(visited)
            continue
        for i in range(len(user_id)):
            if cnt[i][j] and not visited[i]:
                visited[i] = 1
                q.append([j + 1, visited[::]])
                visited[i] = 0
    return len(answer)