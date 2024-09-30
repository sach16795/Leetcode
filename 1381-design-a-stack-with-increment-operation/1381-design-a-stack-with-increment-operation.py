class CustomStack:

    def __init__(self, maxSize: int):
        self.stk = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stk) < self.maxSize:
            self.stk.append(x)

    def pop(self) -> int:
        return self.stk.pop() if len(self.stk) > 0 else -1

    def increment(self, k: int, val: int) -> None:
        for i in range(0, min(len(self.stk), k)):
            self.stk[i] += val        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)