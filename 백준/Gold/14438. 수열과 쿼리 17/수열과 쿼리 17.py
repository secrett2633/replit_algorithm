import sys
input = sys.stdin.readline

def init(node, node1, node2):
  if node1 == node2:
    tree[node] = [arr[node1]]
  else:
    tree[node] = init(node * 2, node1, (node1 + node2) // 2) + init(node * 2 + 1, (node1 + node2) // 2 + 1, node2)
  return tree[node]

def seg_find(node, node1, node2, start, end):
  if start > node2 or end < node1: return int(2e9)
  elif start <= node1 and end >= node2: return min(tree[node])
  else: return min(seg_find(node * 2, node1, (node1 + node2) // 2, start, end), seg_find(node * 2 + 1, (node1 + node2) // 2 + 1, node2, start, end))

def seg_change(node, node1, node2, idx, diff1, diff2):
  if idx > node2 or idx < node1: return
  elif node1 == node2: tree[node].remove(diff1); tree[node] += [diff2]
  else:
    tree[node].remove(diff1); tree[node] += [diff2]
    seg_change(node * 2, node1, (node1 + node2) // 2, idx, diff1, diff2)
    seg_change(node * 2 + 1, (node1 + node2) // 2 + 1, node2, idx, diff1, diff2)
    
n = int(input())
arr = list(map(int, input().split()))
tree = [[] for _ in range(4 * n)]
init(1, 0, n - 1)
for _ in range(int(input())):
  a, x, y = map(int, input().split())
  if a == 2:
    #x, y = min(x, y), max(x, y)
    print(seg_find(1, 0, n - 1, x - 1, y - 1))
  else:
    seg_change(1, 0, n - 1, x - 1, arr[x - 1], y)
    arr[x - 1] = y