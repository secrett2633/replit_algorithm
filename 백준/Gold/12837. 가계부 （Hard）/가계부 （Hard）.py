import sys
import heapq
input = sys.stdin.readline
def init(node, node1, node2):
    if node1 == node2:
        tree[node] = arr[node1]
    else:
        init(node * 2, node1, (node1 + node2) // 2)
        init(node * 2 + 1, (node1 + node2) // 2 + 1, node2)
        tree[node][0] = tree[node * 2][0] + tree[node * 2 + 1][0]
        tree[node][1] = tree[node * 2][1] + tree[node * 2 + 1][1]
def seg_change(node, node1, node2, idx, diff):
    if idx > node2 or idx < node1: return
    elif node1 == node2:
        tree[node] += diff
    else:        
        seg_change(node * 2, node1, (node1 + node2) // 2, idx, diff)
        seg_change(node * 2 + 1, (node1 + node2) // 2 + 1, node2, idx, diff)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]
def seg_count(node, node1, node2, start, end):
    if end < node1 or start > node2: return 0
    elif start <= node1 and end >= node2: return tree[node]
    else: 
        a = seg_count(node * 2, node1, (node1 + node2) // 2, start, end)
        b = seg_count(node * 2 + 1, (node1 + node2) // 2 + 1, node2, start, end)
        return a + b
n, q =  map(int, input().split())
tree = [0] * (4 * n)
for _ in range(q):
    a, b, c = map(int, input().split())
    if a == 1: #add b에 c를
        seg_change(1, 0, n - 1, b - 1, c)
    else: #b~c print
        print(seg_count(1, 0, n - 1, b - 1, c - 1))
