# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        ans = []
        visited = [False]*501
        def search(root,k):
            if not root:
                return
            if visited[root.val] == True:
                return
            visited[root.val] = True
            if k == 0:
                ans.append(root.val)
            elif k<0:
                return
            search(root.left,k-1)
            search(root.right,k-1)
        if target.val == root.val:
            search(root,k)
            return ans

        self.parent = dict()
        self.parent[root.val] = None
        def preorder(root):
            if not root:
                return
            if root.left:
                self.parent[root.left.val] = root
                preorder(root.left)
            if root.right:
                self.parent[root.right.val] = root
                preorder(root.right)
        preorder(root)
        search(target,k)
        p = target

        while self.parent[p.val]!=None and k!=0:
            k-=1
            p = self.parent[p.val]
            search(p,k)
        if root.left and not visited[root.left.val]:
            search(root.left,k-1)
        elif root.right and not visited[root.right.val]:
            search(root.right,k-1)
        return ans

