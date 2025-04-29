word = input()
mod = 10**9 + 7

k = int(input())
a = ord('a')

class Node:

    def __init__(self, char, done):
        self.char = char
        self.done = done
        self.children = [None] * 26

    def set_done(self):
        self.done = True
    
    def add_child(self, char):
        idx = ord(char) - a
        if self.children[idx] is None:
            self.children[ord(char) - a] = Node(char, False)

def second_descent(node, string):
    for char in string:
        if node.children[ord(char) - a] is None:
            return False
        else:
            node = node.children[ord(char) - a]
    return node.done

root = Node(None, False)

for _ in range(k):
    word = input()
    node = root
    for char in word:
        node.add_child(char)
        node = node.children[ord(char) - a]
    node.done = True

total = 0
node = root
for i in range(len(word) - 1):
    idx = ord(word[i]) - a
    node = node.children[idx]
    if node is None:
        break
    else:
        if node.done:
            if second_descent(node, word[i+1:]):
                total += 1
                total %= mod


print(total)







