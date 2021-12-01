
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


        
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def maxDepth(root: TreeNode) -> int:
            return 0 if not root else max(maxDepth(root.left)+1,maxDepth(root.right)+1)
        if not root:
            return True
        if not root.left:
            if not root.right:
                return True
            else:
                return abs(maxDepth(root.left) - maxDepth(root.right))<=1 and self.isBalanced(root.right)
        elif not root.right:
                return abs(maxDepth(root.left) - maxDepth(root.right))<=1 and self.isBalanced(root.left)
        else:
            return abs(maxDepth(root.left) - maxDepth(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    def isBalanced2(self, root: TreeNode) -> bool:
        def maxDepth(root: TreeNode) -> int:
            return 0 if not root else max(maxDepth(root.left)+1,maxDepth(root.right)+1)
        if not root:
            return True
        else:
            return abs(maxDepth(root.left) - maxDepth(root.right))<=1 and self.isBalanced2(root.left) and self.isBalanced2(root.right)