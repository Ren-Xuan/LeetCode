#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans=0
        def before_search(root,max_num):
            nonlocal ans 
            if root==None:
                return 
            if root.val>=max_num:
                ans+=1
                max_num=root.val 
            before_search(root.left,max_num)
            before_search(root.right,max_num)
        before_search(root,root.val)
        return ans