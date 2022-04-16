class TrieNode:
    def __init__(self):
        self.val = 0
        self.next = [None for _ in range(26)]

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        delta = val
        if key in self.map:
            delta -= self.map[key]
        self.map[key] = val
        node = self.root
        for c in key:
            if node.next[ord(c) - ord('a')] is None:
                node.next[ord(c) - ord('a')] = TrieNode()
            node = node.next[ord(c) - ord('a')]
            node.val += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if node.next[ord(c) - ord('a')] is None:
                return 0            
            node = node.next[ord(c) - ord('a')]
        return node.val

