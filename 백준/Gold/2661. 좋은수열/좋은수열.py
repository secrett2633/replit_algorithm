import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
q = deque([["", 0]])
def check(now):
    for i in range(1, len(now) // 2 + 1):
        for j in range(len(now) - i):
            if now[j:j+i] == now[j+i:j+i*2]: 
                return False
    return True
while True:
    now, cnt = q.pop()
    if check(now):
        if cnt == n: break
        for i in ["3", "2", "1"]:
            q.append([now + i, cnt + 1])
print(now)
 