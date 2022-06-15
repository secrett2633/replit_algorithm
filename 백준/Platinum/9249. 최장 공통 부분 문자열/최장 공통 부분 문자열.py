words = [input(), input()]
word = "$".join(words)
sa = [i for i in range(len(word))]
rank = [ord(i) for i in word]
tmp = [0] * len(word)
def f(x): return rank[x] if x < len(word) else -1
t = 1
while t <= len(word):
    sa.sort(key=lambda x: (f(x), f(x + t)))
    p = 0
    tmp[sa[0]] = 0
    for i in range(1, len(word)):
        if f(sa[i - 1]) != f(sa[i]) or f(sa[i - 1] + t) != f(sa[i] + t):
            p += 1
        tmp[sa[i]] = p
    rank = tmp[:]
    t <<= 1
result = [0]*len(word)
for i in range(len(word)):
    rank[sa[i]] = i
length = 0
for i in range(len(word.split()[0])):
    if not rank[i]:
        continue
    j = sa[rank[i] - 1]
    while i+length < len(word) and j+length < len(word) and word[i+length] == word[j+length]:
        length += 1
    result[rank[i]] = length
    length = length-1 if length else length
m = (0, 0)
for i, j in enumerate(result):
    if 0 <= sa[i-1] + j - 1 < len(words[0]) and len(words[0]) < sa[i] + j - 1 < len(word):
        m = max(m, (j, i))
    if 0 <= sa[i] + j - 1 < len(words[0]) and len(words[0]) < sa[i-1] + j - 1 < len(word):
        m = max(m, (j, i))
length, start = m
print(length)
print(word[sa[start]:sa[start]+length])