class Solution:
    
    def filter_words(self, w, p):
        if len(w) != len(p):
            return False
        return len(set(w)) == len(set(p)) == len(set(zip(w, p)))
    
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        return [w for w in words if self.filter_words(w, pattern)]
            