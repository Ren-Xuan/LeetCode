class Node():
    def __init__(self,val):
        self.son = {}
        self.val = val
class MapSum:

    def __init__(self):
        
        self.root =Node(0)

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for e in key:
            index = e
            if index not in cur.son:
                cur.son[index] = Node(0)
            cur = cur.son[index]
        if key[-1] not in  cur.son:
            cur.son[key[-1]] = Node(val)
        else:
            cur.son[key[-1]].val = val

    def sum(self, prefix: str) -> int:
        cur = self.root
        for e in prefix:
            index = e
            if index not in cur.son:
                return 0 
            cur = cur.son[index]
        def getSum(root):
            if not root:
                return 0
            s = 0
            for k in root.son:
                s+=root.son[k].val
                s+=getSum(root.son[k])
            return s

        return getSum(cur)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)