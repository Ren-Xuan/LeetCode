# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder):
        def build(preorder):
            if len(preorder) == 0:
                return None
            else:
                return TreeNode(preorder[0],build([e for e in preorder[1:] if e < preorder[0]]),build([e for e in preorder[1:] if e > preorder[0]]))
        return build(preorder)