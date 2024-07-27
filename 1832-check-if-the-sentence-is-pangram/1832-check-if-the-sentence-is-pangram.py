class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a = "abcdefghijklmnopqrstuvwxyz"
        for i in sentence:
            a = a.replace(i, "")
        return len(a) == 0