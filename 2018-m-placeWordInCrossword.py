class Solution:
    def placeWordInCrossword(self, board, word: str) -> bool:
        from itertools import chain
        match = lambda x, y: all(a in [' ', b] for a, b in zip(x, y))
        for row in chain(board, zip(*board)):
            for ss in ''.join(row).split('#'):
                if len(ss) == len(word) and (match(ss, word) or match(ss, word[::-1])):
                    return True
        return False