# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        else:
            l = self.maxDepth(root.left)
            r = self.maxDepth(root.right)
            if  l == r:
                return root
            elif l>r:
                return self.subtreeWithAllDeepest(root.left)
            else:
                return self.subtreeWithAllDeepest(root.right)
    def maxDepth(self,root):
        if root == None:
            return 0
        else:
            return max(self.maxDepth(root.left),self.maxDepth(self.right))+1
