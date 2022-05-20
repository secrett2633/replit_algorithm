import sys
input = sys.stdin.readline
s = input().rstrip()
cache = [0 for _ in range(26)]
for i in s:
    cache[ord(i) - 65] += 1
cnt = 0
a = ''
b = ''
for i in range(26):
    if cache[i] % 2 == 1:
        cnt += 1
        a += chr(i + 65)
    b += chr(i + 65) * (cache[i] // 2)
print(b + a + b[::-1] if cnt <= 1 else "I'm Sorry Hansoo")