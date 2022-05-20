n = int(input())
graph = [list(map(int,(input()))) for _ in range(n)]
result = []

def recursive(x,y,n):
    now = graph[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if now != graph[i][j]: # 범위안에 한개라도 다른경우는 4분면으로 나눠서 다시 검색
                result.append("(") # 4분면으로 나눌때 괄호를 친다.
                recursive(x,y,n//2)
                recursive(x, y+n//2, n//2)
                recursive(x+n//2, y, n//2)
                recursive(x+n//2, y+n//2, n//2)
                result.append(")")
                return
    result.append(now) 

recursive(0,0,n)
print("".join(map(str,(result))))