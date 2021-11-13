
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.cur = 0
        def convert(root):
            if not root:
                return
            convert(root.right)
            root.val+=self.cur
            self.cur = root.val
            convert(root.left)
        convert(root)
        return root