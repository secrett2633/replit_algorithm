import sys
input = sys.stdin.readline 

def init(node, node1, node2):
    if node1 == node2:
        tree[node] = [a[node1 - 1], 0]
        return tree[node]
    mid = (node1 + node2) // 2
    tmp = init(node * 2, node1, mid) + init(node * 2 + 1, mid + 1, node2)
    tmp.sort(reverse=True)
    tree[node] = tmp[:2]
    return tree[node]
 
def seg_change(x, s, e, idx, v):
    if e < idx or idx < s:
        return tree[x]
    if s == e:
        tree[x] = [v, 0]
        return tree[x] 
    mid = (s + e) // 2
    tmp = seg_change(x * 2, s, mid, idx, v) + seg_change(x * 2 + 1, mid + 1, e, idx, v)
    tmp.sort(reverse=True)
    tree[x] = tmp[:2]
    return tree[x]
 
def seg_count(x, l, r, s, e):
    if e < l or r < s:
        return [0, 0]
    if l <= s and e <= r:
        return tree[x]
    mid = (s + e) // 2
    tmp = seg_count(x * 2, l, r, s, mid) + seg_count(x * 2 + 1, l, r, mid + 1, e)
    tmp.sort(reverse=True)
    return tmp[:2]
 
n = int(input())
a = list(map(int, input().split()))
tree = [[0, 0] for _ in range(n * 4)] 
init(1, 1, n)
 
m = int(input())
for query in range(m):
    q, i, j = map(int, input().split())
    if q == 1:
        seg_change(1, 1, n, i, j)
    else:
        ret = seg_count(1, i, j, 1, n)
        print(ret[0] + ret[1])