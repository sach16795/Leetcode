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
                node.next[ord(char) - ord("a")] = trie_node()
            node.next[ord(char) - ord("a")].cnt +=1
            node = node.next[ord(char) - ord("a")]
        node.is_end = True

    def startsWithCount(self, prefix: str) -> bool:
        node = self.root
        ans = 0
        for char in prefix:
            if node.next[ord(char) - ord("a")] == None:
                return False
            ans += node.next[ord(char) - ord("a")].cnt
            node = node.next[ord(char) - ord("a")]
        return ans

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        N = len(words)
        score = [0] * N
        for word in words:
            trie.insert(word)
        for i in range(N):
            # Get the count of all prefixes of given string.
            score[i] = trie.startsWithCount(words[i])
        return score
    
        # Approach 1 Bruteforce
        # seen = {}
        # ans = [0] * len(words)
        # for i in range(len(words)):
        #     for j in range(len(words[i])+1):
        #         if i in seen:
        #             seen[i].append(words[i][0:j])
        #         else:
        #             seen[i] = []
        #     ans[i] += len(seen[i])
        # for i in range(len(words)):
        #     for j in range(i+1, len(words)):
        #         temp = len(set(seen[i]).intersection(set(seen[j])))
        #         ans[j] += temp
        #         ans[i] += temp
        # return ans
                