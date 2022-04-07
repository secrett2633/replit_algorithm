n = int(input())
def check(num):
    for i in range(2, int(num ** 0.5) + 1): 
        if int(num) % i == 0: 
            return False
    return True

def backtracking(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(10):
            temp = num * 10 + i
            if check(temp) == True:
                backtracking(temp)
backtracking(2)
backtracking(3)
backtracking(5)
backtracking(7)