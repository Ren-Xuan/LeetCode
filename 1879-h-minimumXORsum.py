class Solution:
    def minimumXORSum(self, nums1, nums2) -> int:
        candidate1 = []
        candidate2 = []
        n = len(nums1)
        for i in range(n):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    nums1[i] = -1
                    nums2[j] = -1
        for i in range(n):
            if nums1[i]!=-1:
                candidate1.append(nums1[i])
            if nums2[i]!=-1:
                candidate2.append(nums2[i])
        curMin = [-1]
        nums1 = candidate1
        nums2 = candidate2
        nums1.sort(reverse= True)
        nums2.sort(reverse= True)
        print(nums1,'\n',nums2)
        def dfs(path,candidate,curVal,curMin):
            if curMin[0]!=-1 and curVal>curMin[0]:
                return
            elif curMin[0] == -1 and len(candidate) == 0:
                curMin[0] =curVal
            elif len(candidate) == 0 and curVal < curMin[0]:
                curMin[0] = curVal

            for i in range(len(candidate)):
                val = candidate[i]^nums1[len(path)]
                curVal += val
                dfs(path+[candidate[i]],candidate[:i]+candidate[i+1:],curVal,curMin)
                curVal -= val
        dfs([],nums2,0,curMin)
        return curMin[0]

s = Solution()
print(s.minimumXORSum([1,0,3],[5,3,4]))
a= [2486049,4395362,7707310,8834753,2726898,2325653,2316899,7393406,6058081,5196941,6723570,4034813,1943421,3459280]
b =[5125370,1144646,1784851,3818824,6660686,5391696,8260455,1677288,3133334,754650,928502,390631,3633236,582394]
print(s.minimumXORSum(a,b))