import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = [0] * 4 * n
def init(node, start, end):
  if start == end:
    tree[node] = arr[start]
  else:
    tree[node] = init(node * 2, start, (start + end) // 2) + init(node * 2 + 1, (start + end) // 2 + 1, end)
  return tree[node]

def seg_change(node, node1, node2, idx, diff):
  if idx < node1 or idx > node2: return 0
  elif node1 == node2:
    tree[node] += diff
  else:
    tree[node] += diff
    seg_change(node * 2, node1, (node1 + node2) // 2, idx, diff)
    seg_change(node * 2 + 1, (node1 + node2) // 2 + 1, node2, idx, diff)

def seg_sum(node, node1, node2, start, end):
  if start > node2 or end < node1: return 0
  elif node1 >= start and node2 <= end: return tree[node]
  else: return seg_sum(node * 2, node1, (node1 + node2) // 2, start, end) + seg_sum(node * 2 + 1, (node1 + node2) // 2 + 1, node2, start, end)

init(1, 0, n - 1)
for _ in range(m + k):
  a, b, c = map(int, input().split())
  if a == 1: #b 번째 수를 c로 바꾸기    
    seg_change(1, 0, n - 1, b - 1, c - arr[b - 1])
    arr[b - 1] = c
  else: # b번째 수 부터 c번째 수의 합을 출력
    print(seg_sum(1, 0, n - 1, b - 1, c - 1))