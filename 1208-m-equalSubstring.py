
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        diff = [abs(ord(sc) - ord(tc)) for sc, tc in zip(s, t)]
        maxLength = start = end = 0
        total = 0

        while end < n:
            total += diff[end]
            while total > maxCost:
                total -= diff[start]
                start += 1
            maxLength = max(maxLength, end - start + 1)
            end += 1
        
        return maxLength


    def equalSubstring2(self, s: str, t: str, maxCost: int) -> int:
        maxLen = 0
        left = 0
        right = 0
        cost = maxCost
        while left<=right<len(s):
            if cost>=abs(ord(s[right]) - ord(t[right])):
                cost-=abs(ord(s[right]) - ord(t[right]))
                right+=1
                maxLen = max(maxLen,right - left)
            else:
                cost+=abs(ord(s[left]) - ord(t[left]))
                if cost>maxCost:
                    cost = maxCost
                    right = left+1
                left+=1
        return maxLen