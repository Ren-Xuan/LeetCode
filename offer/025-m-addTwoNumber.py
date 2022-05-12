# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        n1 = 0
        while p:
            n1+=1
            p = p.next
        p = l2
        n2 = 0
        while p:
            n2+=1
            p = p.next
        if n1<n2:
            n1,n2 = n2,n1
            l1,l2 = l2,l1
        l1 = ListNode(0,l1)#多设置1个节点免得头部相加有进位的时候被丢弃
        l2 = ListNode(0,l2)
        n1+=1
        n2+=1
        for _ in range(n1-n2):#延长短的那条和长的那条一样长
            l2 = ListNode(0,l2)
        def union(a,b):
            if a.next == None:
                cur = (a.val+b.val)
                a.val = cur%10
                return cur//10 
            cur = union(a.next,b.next)+a.val+b.val
            a.val = cur%10
            return cur//10
        jinwei = union(l1,l2)
        p = l1
        while p and p.val ==0:
            p = p.next
        if not p:
            return ListNode(0,None)
        return p