class Solution(object):
    def numSubseq(self, nums, target):
        nums.sort()
        mod = int(10**9+7)
        ret = 0
        l=0
        r=len(nums)-1
        while l<=r:
            if nums[l]+nums[r]>target:#从右边开始减，直到找到合适的序列，更新l以后，r也要更新
                r -= 1
            else:
                ret = (ret + (1<<(r-l)))%mod#这一步计算的是包含nums[l]的所有子集个数，这样l+1后，之后计算的子集里面肯定没有之前的nums[l]，这样就不会重复计算
                l+=1
        return ret
"1 2 3 4 5"
"""
子序列有
长度为1：5
长度为2：4
长度为3: 3
长度为4：2
长度为5：1
因此总共 pow(2,n) - 1
此题含有nums[l]的子序列有它自身加上nums[l]后面长度为r-l的子序列组合
因此有pow(2,r-l) - 1 + 1= 1<<(r-l)
"""