# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getGCD(self, x: int, y: int) -> int:
        if x == y:
            return x
        if x % y == 0 or y % x == 0:
            return min(x,y)
        for i in range(min(x,y), 0, -1):
            if x % i == 0 and y % i == 0:
                return i
            
        
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current  = head
        
        while current.next is not None:
            nex = current.next
            gcd = self.getGCD(current.val, nex.val)
            temp = ListNode(gcd, None)
            current.next = temp
            temp.next = nex
            current = nex
        return head
        