class trie_node:
    def __init__(self):
        self.next = [None] * 26
        self.cnt = 0
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = trie_node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if node.next[ord(char) - ord("a")] == None:
                new = trie_node()
                node.next[ord(char) - ord("a")] = new
            node.next[ord(char) - ord("a")].cnt +=1
            node = node.next[ord(char) - ord("a")]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if node.next[ord(char) - ord("a")] == None:
                return False
            node = node.next[ord(char) - ord("a")]
        return True and node.is_end == True
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if node.next[ord(char) - ord("a")] == None:
                return False
            node = node.next[ord(char) - ord("a")]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)