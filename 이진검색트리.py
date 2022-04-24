import sys
sys.setrecursionlimit(10**6)
arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

def postorder(first,end):
    if first > end:
        return
    mid = end+1   # 루트보다 큰 값이 존재하지 않을 경우를 대비   
    for i in range(first+1,end+1):
        if arr[first] < arr[i]:
            mid = i
            break
    
    postorder(first+1, mid-1)
    postorder(mid, end)
    print(arr[first])

postorder(0,len(arr)-1)