from typing import Collection


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.result = 0
        self.target = targetSum
        def pathSum(root,targetSum):
            if not root:
                return
            if targetSum -root.val== 0:
                #print(root)
                self.result+=1
            
            pathSum(root.left,targetSum-root.val)
            pathSum(root.right,targetSum-root.val)
        def traverse(root):
            if not root:
                return
            pathSum(root,self.target)
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return self.result
    def pathSum_n(self, root: TreeNode, targetSum: int) -> int:
        prefix = Collection.defaultdict(int)
        prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return 0
            """
            当前前缀和 - 表中的某个前缀和 = targetSum
            所以  表中某个前缀和 = 当前前缀和sum - targetSum
            表中有多少个前缀和x，其中当前前缀和-x = targetSum
            那么某一段路径之和为target的个数就等于前缀x的个数
            """
            curr += root.val
            ret = prefix[curr - targetSum]
            prefix[curr] += 1
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            prefix[curr] -= 1

            return ret

        return dfs(root, 0)
