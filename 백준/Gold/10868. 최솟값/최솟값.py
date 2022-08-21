import sys
input = sys.stdin.readline

def init(node, node1, node2):
  if node1 == node2:
    tree[node] = arr[node1]
  else:
    tree[node] = min(init(node * 2, node1, (node1 + node2) // 2), init(node * 2 + 1, (node1 + node2) // 2 + 1, node2))
  return tree[node]

def seg_find(node, node1, node2, start, end):
  if start > node2 or end < node1: return int(2e10)
  elif start <= node1 and end >= node2: return tree[node]
  else: return min(seg_find(node * 2, node1, (node1 + node2) // 2, start, end), seg_find(node * 2 + 1, (node1 + node2) // 2 + 1, node2, start, end))

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = [0] * (4 * n)
init(1, 0, n - 1)
for _ in range(m):
  a, b = map(int, input().split())
  print(seg_find(1, 0, n - 1, a - 1, b - 1))