# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self,root):
        res = [0]
        def depth(root):
            if res[0] == -1:
                return 0
            if root == None:
                return 0
            if root.left ==None and root.right == None:
                return 1
            l = 0
            r = 0
            if root.left!=None:
                l = depth(root.left)
            if root.right!=None:
                r = depth(root.right)
            #print(root.val,l,r)
            if abs(l-r)>1:
                res[0] = -1
                return -1
            return max(l,r)+1
        depth(root)
        if res[0] == -1:
            return False
        else:
            return True

#s =Solution()
#print(s.isBalanced([3,9,20,None,None,15,7]))