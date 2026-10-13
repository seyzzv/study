class Node:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word):
        current = self.head
        for char in word:
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]
            current.count += 1

    def get_typing_count(self, word):
        current = self.head
        typing_count = 0
        for char in word:
            typing_count += 1
            current = current.children[char]
            if current.count == 1:
                break
        return typing_count

def solution(words):
    trie = Trie()
    
    for word in words:
        trie.insert(word)
        
    total_count = 0
    for word in words:
        total_count += trie.get_typing_count(word)
        
    return total_count