from typing import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if not root:
            return 0
        self.res = 0

        def dfs(node, depth):
            if not node.left and not node.right:
                return Counter([depth])

            left_leaf_depth, right_leaf_depth = Counter(), Counter()
            if node.left:
                left_leaf_depth = dfs(node.left, depth + 1)
            if node.right:
                right_leaf_depth = dfs(node.right, depth + 1)
            #不看这一段代码其实dfs就是一个后序遍历记录所有叶节点{层数:个数}的字典
            for left_depth, left_count in left_leaf_depth.items():
                for right_depth, right_count in right_leaf_depth.items():
                    if (left_depth - depth) + (right_depth - depth) <= distance:
                        self.res += left_count * right_count

            return left_leaf_depth + right_leaf_depth

        dfs(root, 0)
        return self.res