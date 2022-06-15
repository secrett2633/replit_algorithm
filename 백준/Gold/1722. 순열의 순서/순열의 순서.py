import sys
import math
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
if arr[0] == 1:
    K = arr[1]
    ans = []
    nums = list(range(1, N+1))
    key = K
    for i in range(N):
        X = math.factorial(N-1-i)
        step = (key-1) // X
        ans.append(nums[step])
        nums.remove(nums[step])
        key -= X * (step)
    print(" ".join(map(str, ans)))
else:
    arr = arr[1:]
    arr1 = list(sorted(arr))
    ans = 1
    for i in range(N):
        step = arr1.index(arr[i])
        arr1.remove(arr[i])
        ans += math.factorial(N-1-i) * step        
    print(ans)