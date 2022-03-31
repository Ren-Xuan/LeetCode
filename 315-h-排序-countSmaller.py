
class Solution:
    def countSmaller0(self, nums: List[int]) -> List[int]:
        import bisect
        
        #input 3,  output: [3] -> 3 左边有 0 个数
        #input 2,  output: [2,3] -> 2 左边有 0 个数
        #input 1,  output: [1,2,3] -> 1 左边有 0 个数
        #input 6,  output: [1,2,3,6] -> 6 左边有 3 个数
        #input 3', output: [1,2,3',3,6] -> 3' 左边有 2 个数
        #input 1', output: [1',1,2,3',3,6] -> 1' 左边有 0 个数
        #可以看到，在不断插入的过程中，能根据插入的位置判断出比它小的数有多少个。
        #虽然插入的位置查找速度是 logn 的，但是插入过程却要移动元素，复杂度是 n，这个成本非常高。
        #所以可以引用有序数组
        queue = []
        res = []
        for num in nums[::-1]:
            loc = bisect.bisect_left(queue, num)
            res.append(loc)
            queue.insert(loc, num)
        return res[::-1]

    def countSmaller1(self, nums: List[int]) -> List[int]:
        arr = []
        res = [0] * len(nums)
        for idx, num in enumerate(nums):
            arr.append((idx, num))

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            # print(left, right)
            return merge(left, right)

        def merge(left, right):
            tmp = []
            i = 0
            j = 0
            while i < len(left) or j < len(right):
                if j == len(right) or i < len(left) and left[i][1] <= right[j][1]:
                    tmp.append(left[i])
                    res[left[i][0]] += j
                    i += 1
                else:
                    tmp.append(right[j])
                    j += 1
            return tmp

        merge_sort(arr)
        return res


    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        from sortedcontainers import SortedList
        s = SortedList()
        ans = [0] * n

        # 反向遍历
        for i in range(n - 1, -1, -1):
            # 找到比自己右边小的
            less = s.bisect_left(nums[i])
            # 放到答案里
            ans[i] = less
            # 把自己加上
            s.add(nums[i])
        
        return ans
