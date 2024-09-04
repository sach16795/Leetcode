class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        arr = s.split(" ")
        a = ""
        print (arr)
        for i in arr[::-1]:
            if i == '':
                continue
            a +=i
            a += " "
        return a.strip()