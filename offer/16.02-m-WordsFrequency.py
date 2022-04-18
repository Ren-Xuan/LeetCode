
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        #   记录以该节点结尾的次数
        self.count = 0

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.isEnd = True
        node.count += 1

    def search(self, word: str) -> int:
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                return 0
            node = node.children[idx]

        if node.isEnd:
            return node.count
        else:
            return 0

class WordsFrequency:
    def __init__(self, book: List[str]):
        self.t = Trie()
        for word in book:
            self.t.insert(word)

    def get(self, word: str) -> int:
        return self.t.search(word)

