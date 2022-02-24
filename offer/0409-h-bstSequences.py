#Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root: return [[]]
        res=[]
        path=[]#为了节约空间，函数内部的temp改成在函数外的
        def dfs(cur_nodes):
            if not cur_nodes:
                res.append(path[:])
                return
            for i in range(len(cur_nodes)):
                cur=cur_nodes[i]
                new_nodes=cur_nodes[:i]+cur_nodes[i+1:]
                if cur.left: new_nodes.append(cur.left)#不要在cur_nodes上操作，会超时，因为会重复遍历
                if cur.right: new_nodes.append(cur.right)#所以新建了一个new_nodes来存接下来遍历的
                path.append(cur.val)#节约空间，只用外面的path
                dfs(new_nodes)
                path.pop()#外面的用完pop
        dfs([root])
        return res

