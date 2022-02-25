# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(r):
            if r == None:
                return [0,0]
            #对于以r.left为根的树，计算抢劫根节点(r.left)与不抢劫根节点可获得最大金额. 
            # left[0]则为不抢r.lrft可获得的最大金额,left[1]则为抢劫r.left可获得的最大金额  
            # 以下right[] 分析同理
            left = dfs(r.left)
            right = dfs(r.right)
            res = [0,0]
            #计算不抢劫当前根节点可获得的最大金额(那么其左右子树可以随便抢)
            res[0] = max(left[0],left[1])+max(right[0],right[1])
            #计算若抢劫根节点可获得的最大金额(此时,其左右子树的根节点不能被抢)
            res[1] = r.val + left[0]+right[0]
            return res
        return max(dfs(root))