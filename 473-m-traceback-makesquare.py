class Solution:
    def makesquare(self, nums) -> bool:
        """
        递归，贪心，深度优先，剪枝
        4条边假设为4个固定容量的桶，每次尝试把每根火柴放入4个桶， 全部放完则可以组成正方形
        """
        # 先排除一些特殊情况
        suml = sum(nums)
        if suml % 4 or len(nums) < 4:
            return False
        a = suml // 4

        # 先排序可以大大节约回溯的次数
        nums.sort(reverse=True)

        # 最长火柴大于边长时直接返回
        if a < nums[0]:
            return False

        def dfs(i, sums):
            """
            深度优先遍历
            :param i: 当前访问的火柴位置
            :param sums: 当前桶的容量
            :return:
            """
            # 搜索完了即火柴全部放入桶中，成功
            if i == len(nums):
                return True

            # 尝试把火柴放入4个桶中
            for j in range(4):
                # 只有在桶容量足够时才能放入
                if sums[j] + nums[i] <= a:
                    # 这里有一个非常重要的剪枝过程，即前一个桶和当前桶火柴数一致时，可以直接跳过，因为对于1根火柴来讲，两个桶如果当前大小一样，再放入时是没有区别的，而前面那个桶放入失败，则如果重新放入也肯定失败，故可以直接跳过，实测效率可以提高几十倍
                    if j == 0 or sums[j] != sums[j - 1]:
                        # 尝试放入并开始放下一根火柴
                        sums[j] += nums[i]
                        if dfs(i + 1, sums):
                            return True
                        
                        # 放入失败，取出火柴并开始下一个桶
                        sums[j] -= nums[i]
                        
            # 4个桶都不能放火柴时即需要回溯，体现在上述过程中的取出操作
            return False
        
        # 初始化桶并从0开始放入
        return dfs(0, [0, 0, 0, 0])