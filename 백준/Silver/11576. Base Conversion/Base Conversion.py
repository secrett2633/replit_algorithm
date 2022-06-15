import sys
input = sys.stdin.readline
A, B = map(int, input().split())
m = input()
arr = list(map(int, input().split()))
res = 0
div = 0
for b in arr[::-1]:
    res += (b * (A ** div))
    div += 1
result = []
while res:
    result.append(str(res % B))
    res //= B
print(' '.join(result[::-1]))