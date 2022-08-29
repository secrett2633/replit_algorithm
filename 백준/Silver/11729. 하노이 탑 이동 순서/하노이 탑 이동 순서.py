import sys
input = sys.stdin.readline
n = int(input())
def solve(n, a1, a2, a3):
    if n == 1: print(a1, a3); return
    solve(n - 1, a1, a3, a2)    
    solve(1, a1, a2, a3)    
    solve(n - 1, a2, a1, a3)
print(2 ** n - 1)
solve(n, 1, 2, 3)