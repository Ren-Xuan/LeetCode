class Solution:
  def countPalindromicSubsequences(self, S):
    n = len(S)
    mod = 1000000007
    dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(4)]

    for i in range(n-1, -1, -1):
      for j in range(i, n):
        for k in range(4):
          c = chr(ord('a') + k)
          if j == i:
            if S[i] == c: dp[k][i][j] = 1
            else: dp[k][i][j] = 0
          else: # j > i
            if S[i] != c: dp[k][i][j] = dp[k][i+1][j]
            elif S[j] != c: dp[k][i][j] = dp[k][i][j-1]
            else: # S[i] == S[j] == c
              if j == i+1: dp[k][i][j] = 2 # "aa" : {"a", "aa"}
              else: # length is > 2
                dp[k][i][j] = 2
                for m in range(4): # count each one within subwindows [i+1][j-1]
                  dp[k][i][j] += dp[m][i+1][j-1]
                  dp[k][i][j] %= mod

    ans = 0
    for k in range(4):
      ans += dp[k][0][n-1]
      ans %= mod

    return ans
