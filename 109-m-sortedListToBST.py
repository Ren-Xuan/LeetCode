class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return self.helper(head,None)

    def helper(self,head,tail):
        if head==tail:
            return
        slow=head
        fast=head
        while fast!=tail and fast.next!=tail:
            slow=slow.next
            fast=fast.next.next
        root=TreeNode(slow.val)
        root.left=self.helper(head,slow)
        root.right=self.helper(slow.next,tail)
        return root