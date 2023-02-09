def solution(users, emoticons): 
    ans = []
    def solve(arr, now):
        if not arr:      
            cnt1 = 0
            cnt2 = 0
            for a, b in users:
                tmp = 0
                for a1, b1 in now:
                    if a <= a1: tmp += (b1 * (100 - a1) / 100)
                if tmp >= b: cnt1 += 1
                else: cnt2 += tmp
            ans.append([cnt1, cnt2])
        else:
            a = arr.pop()
            for b in [10, 20, 30, 40]:
                solve(arr[::], now[::] + [[b, a]])
    solve(emoticons, [])       
    
    return sorted(ans)[-1]