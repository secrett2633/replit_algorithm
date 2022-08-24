import sys
import heapq
input = sys.stdin.readline
def init(node, node1, node2):
    if node1 == node2:
        tree[node] = arr[node1]
    else:
        init(node * 2, node1, (node1 + node2) // 2)
        init(node * 2 + 1, (node1 + node2) // 2 + 1, node2)
        tree[node][0] = min(tree[node * 2][0], tree[node * 2 + 1][0])
        tree[node][1] = max(tree[node * 2][1], tree[node * 2 + 1][1])
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
for _ in range(int(input())):
    b, p, q = map(int, input().split())
    tree = [0] * (b * 4)
    # init(1, 0, b - 1)
    for _ in range(p + q):
        flag, aa, bb = input().rstrip().split()
        aa = int(aa)
        bb = int(bb) 
        if flag == "P": #넣기
            seg_change(1, 0, b - 1, aa - 1, bb)
        else:
            print(seg_count(1, 0, b - 1, aa - 1, bb - 1))