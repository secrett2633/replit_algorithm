def solution(numbers):
    answer = []
    def solve(start, end):
        if start == end: return number[start]
        mid = (start + end) // 2
        left = solve(start, mid - 1)
        right = solve(mid + 1, end)
        if not left or not right or (number[mid] == "0" and (left == "1" or right == "1")): return False        
        if left == "0" and right == "0" and number[mid] == "0": return "0"
        return "1"
    aa = {"1" : 1, "0" : 0, True : 1, False : 0}
    for number in numbers:
        number = bin(number)[2:]
        i = 2
        while (len(number) + 1) > i:
            i = i << 1
        number = "0" * (i - len(number) - 1) + number
        res = solve(0, len(number) - 1)
        answer.append(aa[res])
    return answer