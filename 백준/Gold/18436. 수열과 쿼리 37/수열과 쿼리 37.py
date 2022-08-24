import sys
import heapq
input = sys.stdin.readline
def init(node, node1, node2):
    if node1 == node2:
        if arr[node1] % 2 == 0: tree[node] = [1, 0]
        else: tree[node] = [0, 1]
    else:
        init(node * 2, node1, (node1 + node2) // 2)
        init(node * 2 + 1, (node1 + node2) // 2 + 1, node2)
        tree[node][0] = tree[node * 2][0] + tree[node * 2 + 1][0]
        tree[node][1] = tree[node * 2][1] + tree[node * 2 + 1][1]
def seg_change(node, node1, node2, idx, diff):
    if idx > node2 or idx < node1: return
    elif node1 == node2:
        if diff: tree[node][0] -= 1; tree[node][1] += 1
        else: tree[node][0] += 1; tree[node][1] -= 1
    else:        
        seg_change(node * 2, node1, (node1 + node2) // 2, idx, diff)
        seg_change(node * 2 + 1, (node1 + node2) // 2 + 1, node2, idx, diff)
        tree[node][0] = tree[node * 2][0] + tree[node * 2 + 1][0]
        tree[node][1] = tree[node * 2][1] + tree[node * 2 + 1][1]
def seg_count(node, node1, node2, start, end):
    if end < node1 or start > node2: return [0, 0]
    elif start <= node1 and end >= node2: return tree[node]
    else: 
        a = seg_count(node * 2, node1, (node1 + node2) // 2, start, end)
        b = seg_count(node * 2 + 1, (node1 + node2) // 2 + 1, node2, start, end)
        return [a[0] + b[0], a[1] + b[1]]
n = int(input())
arr = list(map(int, input().split()))
tree = [[0, 0] for _ in range(4 * n)]
init(1, 0, n - 1)
m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1: #change
        if arr[b - 1] % 2 == c % 2: continue
        elif c % 2 == 0: seg_change(1, 0, n - 1, b - 1, False) 
        else: seg_change(1, 0, n - 1, b - 1, True) 
        arr[b - 1] = c
    elif a == 2: # even
        print(seg_count(1, 0, n - 1, b - 1, c - 1)[0])
    else: #odd
        print(seg_count(1, 0, n - 1, b - 1, c - 1)[1])
