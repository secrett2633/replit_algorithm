import sys
input = sys.stdin.readline
class Trie(object):
    def __init__(self):
        self.head = Node(0)
    def insert(self,element):
        cur = self.head
        for i in element:
            if i == "0":
                if cur.left:
                    cur.left.data += 1
                else:
                    cur.left = Node(0)
                cur = cur.left
            else:
                if cur.right:
                    cur.right.data += 1                
                else:
                    cur.right = Node(0)
                cur = cur.right
    def delete(self, element):
        cur = self.head
        for i in element:
            if i == "0":
                if cur.left.data > 0:
                    cur.left.data -= 1
                else:
                    cur.left = False
                    break                
                cur = cur.left
            else:
                if cur.right.data > 0:
                    cur.right.data -= 1
                else:
                    cur.right = False
                    break
                cur = cur.right
    def xor(self, element):
        cur = self.head
        ans = "0b"
        for i in element:
            if i == "0":
                if cur.right :
                    ans += "1"
                    cur = cur.right
                else:
                    ans += "0"                    
                    cur = cur.left
            else:
                if cur.left :
                    ans += "1"
                    cur = cur.left 
                else:
                    ans += "0"
                    cur = cur.right
        answer = int(ans,2)
        return answer
      
class Node(object):
    def __init__(self, data):
        self.data = data    
        self.left = {}      
        self.right = {}   

M = int(input())
trie = Trie()
trie.insert(format(0,'b').zfill(30))
for _ in range(M):
    a, b = map(int, input().split())
    element = format(b,'b').zfill(30)
    if a == 1:
        trie.insert(element)
    elif a == 2:
        trie.delete(element)
    elif a == 3:
        result = trie.xor(element)
        print(result)        