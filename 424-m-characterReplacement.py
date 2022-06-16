class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = dict()
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print(len(s))
        for c in alpha:
            ans[c] = k
        def solve(s,c,k):
            ans = k
            cnt = 0
            left = 0
            for right in range(len(s)):
                if s[right] ==c:
                    ans = max(ans,right-left+1)
                else:
                    if k!=0:
                        ans = max(ans,right-left+1)
                        k-=1
                    else:
                        while s[left]==c:#找到第一个修改的位置
                            left+=1
                        #k+=1这里不能加1，因为当前的字符也不等于c,双指针范围内已经包含了k个不符合范围的字符了
                        left+=1#找到了，复原它
            #AAABBACCCCCAAABAA
            return ans
        for c in alpha:
            ans[c] = solve(s, c , k)
        return max(ans[c] for c in ans)
