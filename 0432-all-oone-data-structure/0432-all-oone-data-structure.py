class AllOne:

    def __init__(self):
        self.seen = {}
        

    def inc(self, key: str) -> None:
        if key in self.seen:
            self.seen[key] += 1
        else:
            self.seen[key] = 1
        

    def dec(self, key: str) -> None:
        if self.seen[key] > 1:
            self.seen[key] -= 1
        else:
            self.seen.pop(key)
        

    def getMaxKey(self) -> str:
        if len(self.seen.values()) == 0 :
            return ""
        maxval = max(self.seen.values())
        for key,val in self.seen.items():
            if val == maxval:
                return key

    def getMinKey(self) -> str:
        if len(self.seen.values()) == 0 :
            return ""
        minval = min(self.seen.values())
        for key,val in self.seen.items():
            if val == minval:
                return key
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()