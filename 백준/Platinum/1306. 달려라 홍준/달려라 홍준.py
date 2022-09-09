import sys
import heapq
input = sys.stdin.readline
def init(node):
    for i in range(node - 1, 0, -1):
        tree[i] = max(tree[i << 1], tree[i << 1 | 1])
def query(node, start, end):
    result = 0
    start += node
    end += node
    while start < end:
        if start & 1:
            result = max(result, tree[start])
            start += 1
        if end & 1:
            result = max(result, tree[end - 1])
            end -= 1
        start >>= 1
        end >>= 1
    return result
n, m = map(int, input().split())
arr = list(map(int, input().split()))
tree = [0] * (2 * n)
for i in range(n):
    tree[n + i] = arr[i]
init(n)
for i in range(n - (m * 2 - 1) + 1):
    print(query(n, i, i + 2 * m - 1), end = " ")
print()