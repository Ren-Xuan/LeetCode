# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Codec:
    def serialize(self, root):
        def dfs(node):
            if not node:
                return 'None'
            return {'val': node.val, 'left':dfs(node.left), 'right':dfs(node.right) }
        return json.dumps(dfs(root))

    def deserialize(self, data): 
        def dfs(data):
            if data=='None':
                return None
            return TreeNode(data['val'], dfs(data['left']), dfs(data['right']))
        return dfs(json.loads(data))