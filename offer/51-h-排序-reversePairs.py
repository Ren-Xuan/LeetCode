from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(nums, low, high):
            if low >= high:
                return
            mid = (high+low)//2     
            mergeSort(nums, low, mid)       # 递归排序
            mergeSort(nums, mid+1, high)
            
            nonlocal ans    # 全局变量，记录结果

            tmp = []
            left, right = low, mid+1
            while left<=mid and right<=high:
                if nums[left] <= nums[right]:
                    tmp.append(nums[left])
                    left += 1
                else:       # 后半部分值较小，出现了逆序
                    tmp.append(nums[right])
                    right += 1
                    ans += mid+1-left       # 当前值 nums[right] 贡献的逆序对个数为 mid+1-left
                                            #【解释】若nums[left] > nums[right]，则nums[left:mid+1] 均 > nums[right]，共 mid+1-left 项
            
            # 左或右数组需遍历完（只有一个未遍历完）
            while left<=mid:
                tmp.append(nums[left])
                left += 1
            
            while right<=high:
                tmp.append(nums[right])
                right += 1
                # ans += mid+1-left     # 此时，前半部分一定遍历完了，即left=mid+1，因此无需再更新结果
            
            nums[low:high+1] = tmp
        
        
        # 主程序
        n = len(nums)
        ans = 0
        mergeSort(nums, 0, len(nums)-1)
        return ans
