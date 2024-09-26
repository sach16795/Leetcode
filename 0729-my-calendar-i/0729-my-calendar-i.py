class MyCalendar:

    def __init__(self):
        self.seen = {}

    def book(self, start: int, end: int) -> bool:
        if len(self.seen) > 0:
            for s,e in self.seen.items():
                if (start < s and end > s) or (start == s) or( start > s  and start < e) :
                    return False
            self.seen[start] = end
        else:
            self.seen[start] = end
            return True
        
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)