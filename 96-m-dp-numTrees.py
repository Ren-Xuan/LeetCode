class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        结题思路：假设n个节点存在二叉排序树的个数是G(n)，
        1为根节点，2为根节点，...，n为根节点，当1为根节点时，
        其左子树节点个数为0，右子树节点个数为n-1，
        同理当2为根节点时，其左子树节点个数为1，右子树节点为n-2，
        所以可得G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)
        dp[i] 表示最大为i的二叉排序树有多少
        """
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2,n+1):
            for j in range(1,i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]
