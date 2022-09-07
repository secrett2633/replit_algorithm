import sys
import math
input = sys.stdin.readline
def seg_change(node):
    temp = size + node - 1
    while temp >= 1:
        tree[temp] += 1
        temp //= 2           
def seg_count(node, node1, node2, start, end):
    if end < node1 or start > node2: return 0
    elif start <= node1 and end >= node2: return tree[node]
    else: 
        a = seg_count(node * 2, node1, (node1 + node2) // 2, start, end)
        b = seg_count(node * 2 + 1, (node1 + node2) // 2 + 1, node2, start, end)
        return a + b
n = int(input())
tree = [0] * (2 ** math.ceil(math.log2(n) + 1))
arr = [int(input()) for _ in range(n)]
cache = {i: a + 1 for a, i in enumerate(sorted(arr))}
size = 2 ** math.ceil(math.log2(n))
for i in range(n):
    print(i + 1 - seg_count(1, 0, size - 1, 0, cache[arr[i]] - 1))
    seg_change(cache[arr[i]])