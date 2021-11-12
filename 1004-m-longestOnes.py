class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = 0
        n = 0
        cnt = 0
        while right<len(nums):
            if nums[right] == 1:
                right+=1
            elif cnt < k:
                """右指针遇到了0但是补成1的次数还够"""
                cnt+=1
                right+=1
            else:#nums[right] == 0 and cnt > k
                #find the first 0
                """
                不能补1了又想继续增大窗口
                只有从left开始寻找0,把它变成1的机会让给right以后的
                left 变为找到第一个0的index的下一个
                """
                if nums[left] == 0:
                    cnt-=1
                    left+=1
                else:
                    left+=1

            n = max(n,right - left )
        return n
    
    def longestSubOnes(self, nums):
        """
        find longestSubOnes like 0101011100 = 111
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        n = 0
        firstTime = True
        while right<len(nums):
            if nums[right] == 1:
                if firstTime:
                    #find the first 1 from [right:]
                    left = right
                    firstTime = False
                right+=1
            else:# nums[right] == 0
                firstTime = True
                #slide the window
                right+=1
                left +=1
            n = max(n,right - left)
        return n
    def longestSubstr(self, s):
        left = 0
        right = 0
        n = 0
        st = set()
        while right<len(s):
            if s[right] not in st:
                st.add(s[right])
                right+=1
            else:
                #find the index let s[index] == s[right]
                #then left = index+1

                st.remove(s[left])
                left+=1
            n = max(n,right - left)
        return n

s = Solution()
print(s.longestSubstr("abcdefcdef"))
print(s.longestSubstr("abcdefcdefghiaccc"))

print("-"*10)
s = Solution()
print(s.longestSubOnes([1,1,1,0,0,0,1,1,1,1,0]))
print(s.longestSubOnes([1,1,1,1,0,1,1,1,1,1,0]))
print(s.longestSubOnes([1,1,1,1,1,0,1,1,1,1,0]))
print(s.longestSubOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]))
print(s.longestSubOnes([0,0,1,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]))
print("-"*10)
s = Solution()
print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))
print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0],3))
print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
print(s.longestOnes([0,0,1,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
print(s.longestOnes([0,0,1,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],2))
print(s.longestOnes([0,0,1,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],1))
