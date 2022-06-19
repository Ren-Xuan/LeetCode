class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        tail = dict()
        for i in range(len(s)-1,-1,-1):
            if s[i] not in tail:
                tail[s[i]] = i
        start = 0
        end = 0
        ans = []
        for i in range(len(s)):
            end = max(end,tail[s[i]])
            if i == end:
                ans.append(end-start+1)
                start = i+1
        return ans