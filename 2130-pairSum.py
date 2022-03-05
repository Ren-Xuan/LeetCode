# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 快慢指针，多设置一个pre节点，用于反转链表
        pre, slow, fast = None, head, head
        # 一遍找中间节点，一遍反转链表，前一半的链表会被反转
        while fast and fast.next:
            # fast指针走两步
            fast = fast.next.next
            # 反转链表
            tmp = slow.next
            slow.next = pre
            pre = slow
            slow = tmp
        # 开始求和
        res = float("-inf")
        while pre:
            res = max(res, pre.val + slow.val)
            pre, slow = pre.next, slow.next
        return res
        

    def pairSum1(self, head: Optional[ListNode]) -> int:
        p = head
        headRecur = ListNode(-1)
        n = 0
        while p:
            tmp = headRecur.next
            cur = ListNode(p.val)
            headRecur.next = cur
            cur.next = tmp
            p = p.next
            n+=1
        ans = -1
        p1 = head
        p2 = headRecur.next
        for i in range(n):
            ans = max(ans,p1.val+p2.val)
            p1=p1.next
            p2=p2.next
        return ans