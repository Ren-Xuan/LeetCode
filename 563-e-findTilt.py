# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:

        def search(root: TreeNode) : # 返回节点和，累积坡度
            if not root:
                return 0, 0
            else:
                sl, pl = search(root.left) # 递归求解子问题
                sr, pr =search(root.right) # 递归求解子问题 
                return sr + sl + root.val, abs(sl - sr) + pl + pr # 跟节点的节点和，累积坡度与子问题的递归关系（合并子问题，形成原问题的解）
        
        _, p = search(root)
        return p

