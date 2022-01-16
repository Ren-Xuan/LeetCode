class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.root = head

    def getRandom(self) -> int:
        node, ans, i = self.root, None, 0
        while node:
            if not randint(0, i):
                ans = node.val
            node, i = node.next, i + 1
        return ans
