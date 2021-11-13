class Node():
    def __init__(self):
        self.son = [None]*24
        self.val = [0]*24
class MapSum:

    def __init__(self):
        
        self.root =Node()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for e in key[:-1]:
            index = ord(e) - ord('a')
            if not cur.son[index]:
                cur.son[index] = Node()
            cur = cur.son[index]
        cur.val[ord(key[-1]) - ord('a')]  =val

    def sum(self, prefix: str) -> int:
        cur = self.root
        for e in prefix:
            index = ord(e) - ord('a')
            cur = cur.son[index]
        def getSum(root):
            if not root:
                return 0
            s = 0
            for i in range(24):
                s+=root.val[i] if root.son[i] else 0
                s+=getSum(root.son[i])
            return s

        return getSum(cur)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)