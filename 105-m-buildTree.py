# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.root = None
        def build(preorder,inorder)->TreeNode:
            if len(inorder) == 0:
                return None
            root = TreeNode(preorder[0])
            k = inorder.index(preorder[0])
            root.left = build(preorder[1:][:k],inorder[:k])
            root.right = build(preorder[1:][k:],inorder[k+1:])
            return root
        self.root = build(preorder,inorder)
        return self.root