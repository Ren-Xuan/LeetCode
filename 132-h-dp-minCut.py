class Solution:
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        
        for i in range(1, len(s) + 1):
            if s[:i] == s[i-1::-1] and s[i:] == s[:i-1:-1]:
                return 1
        dp = [i for i in range(len(s))]
        #以dp[right] 为边界的最多需要切几次
        def isPalin(left, right):
            #如果以当前字符为中心的最大回文串左侧为i，右侧为j，
            #那s[i]~s[j]长度是不需要切割的，
            #只需要在s[i-1]处切一刀即可，
            #即dp[i-1]+1。所以更新dp[j] = min(dp[j] , dp[i-1]+1)，
            #不断往外扩散更新dp值取dp[-1]即可。
            while left >=0 and right < len(s):
                if s[left] == s[right]:
                    dp[right] = min(dp[right], dp[left-1] + 1 if left > 0 else 0)
                else:
                    break
                left -= 1
                right += 1
        #那么如果说能找到以每个字符为中心的最长回文串，实际上就已经找到了答案
        for i in range(0, len(s)):
            isPalin(i, i)
            isPalin(i, i+1)
        return dp[-1]
