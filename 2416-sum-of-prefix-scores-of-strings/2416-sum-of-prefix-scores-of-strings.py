class trie_node:
    def __init__(self):
        self.next = [None] * 26
        self.cnt = 0

class Solution:
    def __init__(self):
        self.root = trie_node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            x = ord(char) - ord("a")
            if node.next[x] == None:
                node.next[x] = trie_node()
            node.next[x].cnt +=1
            node = node.next[x]
            
    def startsWithCount(self, prefix: str) -> bool:
        node = self.root
        ans = 0
        for char in prefix:
            x = ord(char) - ord("a")            
            if node.next[x] == None:
                return False
            ans += node.next[x].cnt
            node = node.next[x]
        return ans
    
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        N = len(words)
        score = [0] * N
        for i in range(N):
            self.insert(words[i])
        for i in range(N):
            score[i] = self.startsWithCount(words[i])
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
                