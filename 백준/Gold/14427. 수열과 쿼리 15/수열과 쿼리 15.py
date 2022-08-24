import sys
import heapq
input = sys.stdin.readline
def init(node, node1, node2):
    if node1 == node2:
        tree[node] = [arr[node1], node1]
    else:
        init(node * 2, node1, (node1 + node2) // 2)
        init(node * 2 + 1, (node1 + node2) // 2 + 1, node2)
        tree[node] = sorted([tree[node * 2]] + [tree[node * 2 + 1]])[0]
def seg_change(node, node1, node2, idx, diff):
    if idx > node2 or idx < node1: return []
    elif node1 == node2:
        tree[node] = [diff, node1]
    else:        
        seg_change(node * 2, node1, (node1 + node2) // 2, idx, diff)
        seg_change(node * 2 + 1, (node1 + node2) // 2 + 1, node2, idx, diff)
        tree[node] = sorted([tree[node * 2]] + [tree[node * 2 + 1]])[0]
def seg_count(node, node1, node2, start, end):
    if end < node1 or start > node2: return []
    elif start <= node1 and end >= node2: return tree[node]
    else: 
        a = seg_count(node * 2, node1, (node1 + node2) // 2, start, end)
        b = seg_count(node * 2 + 1, (node1 + node2) // 2 + 1, node2, start, end)
        return sorted([a] + [b])[0]
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
tree = [[] for _ in range(n * 4)]
init(1, 0, n - 1)
for _ in range(m):
    q = list(map(int, input().split()))
    if q == [2]: #가장 작은 값의 인덱스 출력
        print(seg_count(1, 0, n - 1, 0, n - 1)[1] + 1)
    else: #b-1를 c로 바꾸기 
        seg_change(1, 0, n - 1, q[1] - 1, q[2])
