import sys
import math
input = sys.stdin.readline

def init(index, start, end):
    if start == end:
        tree[index] = nums[start]
        return
    init(index * 2, start, (start + end) // 2)
    init(index * 2 + 1, (start + end) // 2 + 1, end)
    tree[index] = tree[index * 2] + tree[index * 2 + 1]

def update(index, start, end, left, right, to_added):
    propagate_tree(index, start, end)
    if right < start or end < left:
        return
    if left <= start and end <= right:
        tree[index] += (end - start + 1) * to_added
        if start != end:
            lazy[index * 2] += to_added
            lazy[index * 2 + 1] += to_added
        return
    update(index * 2, start, (start + end) // 2, left, right, to_added)
    update(index * 2 + 1, (start + end) // 2 + 1, end, left, right, to_added)
    tree[index] = tree[index * 2] + tree[index * 2 + 1]


def query(index, start, end, left, right):
    propagate_tree(index, start, end)
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[index]
    mid = (start + end) // 2
    return query(index * 2, start, mid, left, right) + query(index * 2 + 1, mid + 1, end, left, right)


def propagate_tree(index, start, end):
    if lazy[index] != 0:
        tree[index] += (end - start + 1) * lazy[index]
        if start != end:
            lazy[index * 2] += lazy[index]
            lazy[index * 2 + 1] += lazy[index]
        lazy[index] = 0

N, M, K = map(int, input().split())
nums = [-1]
for i in range(N):
    nums.append(int(input()))
tree = [0] * 2 ** math.ceil(math.log2(N) + 1)
lazy = [0] * 2 ** math.ceil(math.log2(N) + 1)
init(1, 1, N)
for _ in range(M + K):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        update(1, 1, N, arr[1], arr[2], arr[3])
    else:
        print(query(1, 1, N, arr[1], arr[2]))