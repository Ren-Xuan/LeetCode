from typing import Counter


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        s =Counter(arr)
        print(s)
        s =Counter(set(arr))
        print(s)
        print(dict(s))
        d = dict(Counter(arr))
        return len(arr) == len(s)
s = Solution()
print(s.uniqueOccurrences([1,2,3,4,1,2,1]))
print(12^13)