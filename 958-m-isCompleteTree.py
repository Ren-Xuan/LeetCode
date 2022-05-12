class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        level = [root]
        stop = False
        while len(level)!=0:
            nextlevel = []
            for node in level:
                if node.left:
                    if stop:
                        return False
                    nextlevel.append(node.left)
                else:
                    stop = True
                if node.right:
                    if stop:
                        return False
                    nextlevel.append(node.right)
                else:
                    stop = True
            level = nextlevel
        return True