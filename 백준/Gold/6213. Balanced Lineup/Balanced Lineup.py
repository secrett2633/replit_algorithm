import sys
import heapq
input = sys.stdin.readline
def init(node, node1, node2):
    if node1 == node2:
        tree[node] = [arr[node1], arr[node1]]
    else:
        init(node * 2, node1, (node1 + node2) // 2)
        init(node * 2 + 1, (node1 + node2) // 2 + 1, node2)
        tree[node][0] = min(tree[node * 2][0], tree[node * 2 + 1][0])
        tree[node][1] = max(tree[node * 2][1], tree[node * 2 + 1][1])
def seg_change(node, node1, node2, idx, diff):
    if idx > node2 or idx < node1: return [int(1e9), -int(1e9)]
    elif node1 == node2:
        tree[node] = [diff, node1]
    else:        
        seg_change(node * 2, node1, (node1 + node2) // 2, idx, diff)
        seg_change(node * 2 + 1, (node1 + node2) // 2 + 1, node2, idx, diff)
        tree[node] = sorted([tree[node * 2]] + [tree[node * 2 + 1]])[0]
def seg_count(node, node1, node2, start, end):
    if end < node1 or start > node2: return [int(1e9), -int(1e9)]
    elif start <= node1 and end >= node2: return tree[node]
    else: 
        a = seg_count(node * 2, node1, (node1 + node2) // 2, start, end)
        b = seg_count(node * 2 + 1, (node1 + node2) // 2 + 1, node2, start, end)
        return [min(a[0], b[0]), max(a[1], b[1])]
n, q = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = [[0, 0] for _ in range(n * 4)]
init(1, 0, n - 1)
for _ in range(q):
    a, b = list(map(int, input().split()))
    c = seg_count(1, 0, n - 1, a - 1, b - 1)
    print(c[1] - c[0])
