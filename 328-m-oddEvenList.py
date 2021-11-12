# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        oddHead = head
        evenHead = head.next
        curOdd = oddHead
        curEven = evenHead
        while not (curOdd.next== None or curEven.next == None):
            curOdd.next,curEven.next = curOdd.next.next,curEven.next.next
            curOdd =curOdd.next
            curEven = curEven.next
        
        
        curOdd.next = evenHead
        return oddHead