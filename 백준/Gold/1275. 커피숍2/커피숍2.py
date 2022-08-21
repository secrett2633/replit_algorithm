import sys
input = sys.stdin.readline

def init(node, node1, node2):
  if node1 == node2:
    tree[node] = arr[node1]
  else:
    tree[node] = init(node * 2, node1, (node1 + node2) // 2) + init(node * 2 + 1, (node1 + node2) // 2 + 1, node2)
  return tree[node]

def seg_find(node, node1, node2, start, end):
  if start > node2 or end < node1: return 0
  elif start <= node1 and end >= node2: return tree[node]
  else: return seg_find(node * 2, node1, (node1 + node2) // 2, start, end) + seg_find(node * 2 + 1, (node1 + node2) // 2 + 1, node2, start, end)

def seg_change(node, node1, node2, idx, diff):
  if idx > node2 or idx < node1: return
  elif node1 == node2: tree[node] += diff
  else:
    tree[node] += diff
    seg_change(node * 2, node1, (node1 + node2) // 2, idx, diff)
    seg_change(node * 2 + 1, (node1 + node2) // 2 + 1, node2, idx, diff)
    

n, m = map(int, input().split())
arr = list(map(int, input().split()))
tree = [0] * (4 * n)
init(1, 0, n - 1)
for _ in range(m):
  x, y, a, b = map(int, input().split())
  x, y = min(x, y), max(x, y)
  print(seg_find(1, 0, n - 1, x - 1, y - 1))
  seg_change(1, 0, n - 1, a - 1, b - arr[a - 1])
  arr[a - 1] = b