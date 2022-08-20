import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = [[0, 0] for _ in range(4 * n)]
def init(node, node1, node2):
  if node1 == node2:
    tree[node][0] = arr[node1]
    tree[node][1] = arr[node1]
  else:
    a = init(node * 2, node1, (node1 + node2) // 2)
    b = init(node * 2 + 1, (node1 + node2) // 2 + 1, node2)
    tree[node][0] = min(a[0], b[0])
    tree[node][1] = max(a[1], b[1])
  return tree[node]
def seg_sum(node, node1, node2, start, end):
  if node1 > end or node2 < start: return [int(2e9), -1]
  elif node1 >= start and node2 <= end: return tree[node]
  else:
    a = seg_sum(node * 2, node1, (node1 + node2) // 2, start, end)
    b = seg_sum(node * 2 + 1, (node1 + node2) // 2 + 1, node2, start, end)
    return [min(a[0], b[0]), max(a[1], b[1])] 
init(1, 0, n - 1)
for _ in range(m):
  a, b = map(int, input().split())
  print(*seg_sum(1, 0, n - 1, a - 1, b - 1))