import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = [0] * (4 * n)
def init(node, node1, node2):
  if node1 == node2:
    tree[node] = arr[node1]
  else:
    tree[node] = (init(node * 2, node1, (node1 + node2) // 2) * init(node * 2 + 1, (node1 + node2) // 2 + 1, node2)) % 1000000007
  return tree[node]
def seg_sum(node, node1, node2, start, end):
  if node1 > end or node2 < start: return 1
  elif node1 >= start and node2 <= end: return tree[node]
  else:
    return seg_sum(node * 2, node1, (node1 + node2) // 2, start, end) * seg_sum(node * 2 + 1, (node1 + node2) // 2 + 1, node2, start, end)

def seg_change(node, node1, node2, idx, diff):
  if idx > node2 or idx < node1: return
  elif node1 == node2: tree[node] = diff
  else:    
    seg_change(node * 2, node1, (node1 + node2) // 2, idx, diff)
    seg_change(node * 2 + 1, (node1 + node2) // 2 + 1, node2, idx, diff)
    tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % 1000000007

init(1, 0, n - 1)
for _ in range(m + k):
  a, b, c = map(int, input().split())
  if a == 1: # b를 c로 바꾸기
    seg_change(1, 0, n - 1, b - 1, c)
    arr[b - 1] = c
  else: #b 부터 c까지의 곱을 출력  
    print(seg_sum(1, 0, n - 1, b - 1, c - 1) % 1000000007)