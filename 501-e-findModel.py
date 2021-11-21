# Definition for a binary tree node.
from typing import DefaultDict, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode1(self, root: TreeNode) -> List[int]:
        self.result = DefaultDict(int)
        def preorder(root):
            if not root:
                return 
            self.result[root.val]+=1
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        m = -1
        for e in self.result:
            if self.result[e]>m:
                m = self.result[e]
        res = set()
        for e in self.result:
            if self.result[e] == m:
                res.add(e)
        
        return list(res)
    def findMode(self, root: TreeNode) -> List[int]:

        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
            
        ans = []
        cnt, max_cnt, last = 0, 0, None
        for v in inorder(root):
            if v == last:
                cnt += 1
            else:
                cnt = 1
            if cnt > max_cnt:
                ans = [v]
                max_cnt = cnt
            elif cnt == max_cnt:
                ans.append(v)
            last = v
        return ans