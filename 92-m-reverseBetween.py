# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        h = ListNode(501,head)
        preLeft = h
        rightRight = head
        for _ in range(left-1):
            preLeft = preLeft.next
        for _ in range(right-1):
            rightRight = rightRight.next
        p = rightRight
        rightRight = rightRight.next
        p.next = None
        def reverseList( head: ListNode) -> ListNode:
            if head is None:
                return None
            pre = None
            cur = head
            while cur:
                # 等号左边cur一定要位于cur.next之后，否则cur.next指针将被影响。
                cur.next, pre, cur = pre, cur, cur.next
            return pre
        p = preLeft.next#反转它
        p = reverseList(p)
        preLeft.next = p
        while p.next:
            p = p.next
        p.next = rightRight
        return h.next

