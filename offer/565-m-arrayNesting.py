from typing import List


class Solution:
    def arrayNesting1(self, nums: List[int]) -> int:
        dd = [None]*len(nums)
        for i in range(len(nums)):
            cur = nums[i]
            if dd[i] == None:
                dd[i] = set()
                while cur not in dd[i]:
                    dd[i].add(cur)
                    if dd[cur] !=None:
                        dd[i] = dd[i].union(dd[cur])
                        if len(dd[i])>len(nums)//2+1:
                            return len(dd[i])
                        break
                    cur = nums[cur]
                    
        cur = 0
        for i in range(len(nums)):
            if len(dd[i])>cur:
                cur = len(dd[i])
        return cur

    def arrayNesting(self, nums: List[int]) -> int:
        visited=set()
        ans=0
        for x in nums:
            cnt=0
            while x not in visited:
                visited.add(x)
                x=nums[x]
                cnt+=1
                ans=max(cnt,ans)
        return ans