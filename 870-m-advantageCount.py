class Solution:
    def advantageCountOvertime(self, nums1, nums2) :
        nums1.sort()
        #print(nums1)
        result = []
        for e in nums2:
            add = -1
            for i in range(len(nums1)):
                if nums1[i] >e :
                    result.append(nums1[i])
                    nums1 = nums1[:i]+nums1[i+1:]
                    add = i
                    break
            if add ==-1:
                result.append(-1)
        index =0 
        for i in range(len(result)):
            if result[i] == -1:
                result[i] = nums1[index]
                index+=1
              
        return result
    def advantageCount(self, nums1, nums2) :
        # Python3 没有最大堆，所以变成负数做最小堆
        import heapq
        nums2 = [(-x, index) for index, x in enumerate(nums2)]
        heapq.heapify(nums2)
        # A是不需要顺序的，B是需要顺序的，所以数字记录index，不然做不了
        nums1.sort()
        # 第一个，是用双端队列，第二个是用双指针（两端取数的时间复杂度为1）
        # 我自己用双指针
        left, right = 0, len(nums1) - 1
        # 一个数组记录答案
        ans = [0] * len(nums1)
        while nums2:
            # 如果打得过对面最大的，那么就拿自己最大的打赢他
            # 这个题目是标准的贪心
            data, index = heapq.heappop(nums2)
            if nums1[right] > - data:
                ans[index] = nums1[right]
                right -= 1
            # 如果打不赢，那么就拿自己最小的PK
            else:
                ans[index] = nums1[left]
                left += 1
        # 时间复杂度N
        return ans

    def advantageCount2(self, A, B) :
        A1 = sorted(A)
        B1 = sorted(B)
        d = {b:[] for b in B}
        p = []
        i = 0
        for a in A1:
            if a > B1[i]:
                d[B1[i]].append(a)
                i += 1
            else:
                p.append(a)
        return [d[b].pop(0) if d[b] else p.pop(0) for b in B]
s = Solution()
print(s.advantageCountOvertime([12,24,8,32],  [13,25,32,11]))