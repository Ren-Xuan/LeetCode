class Solution:
    def minOperations(self, target, arr) -> int:
        dic = dict()
        for i,e in enumerate(target):
            dic[e] = i
        arrIndexinTar = [dic[e] for e in arr if e in dic]
        #print(tar)
        #print(arrIndexinTar)
        def lengthOfLIS(nums):
            tails = [0] * len(nums)
            size = 0
            for x in nums:
                i, j = 0, size
                while i != j:#找到第一个大于
                    m = (i + j) // 2
                    if tails[m] < x:
                        i = m + 1
                    else:
                        j = m
                tails[i] = x
                size = max(i + 1, size)
            return size

        return len(target) - lengthOfLIS(arrIndexinTar)
    def minOperations(self, target, arr) -> int:
        # 分析:
        # 本题要找最少操作次数，实际上就是找最长的公共子序列(这样需要的操作最少)
        # 根据target中互不相同，我们知道每个数字对应的坐标唯一
        # 于是最长公共子序列等价于arr用target的坐标转换后构成最长的上升子序列

        # 数字对应坐标
        idx_dict = {num: i for i, num in enumerate(target)}
        # 300.最长上升子序列
        stack = []
        for num in arr:
            # 只有在target的数字才可能属于公共子序列
            if num in idx_dict:
                # 转换坐标
                idx = idx_dict[num]
                # 该坐标在当前栈中的位置
                i = bisect.bisect_left(stack, idx)
                # 如果在最后要加入元素，否则要修改该位置的元素
                # 跟一般的讲，i代表了目前这个idx在stack中的大小位置，
                # 在前面出现还比idx大的stack中的元素是无法和idx构成最长上升子序列的。
                # i左边的数比idx小，可以和idx构成上升子序列，(idx构成的长度就是i+1)
                # idx比i的值小，将i替换后可以方便后面构成更优的子序列(越小后面能加入的数越多)
                if i == len(stack):
                    stack.append(0)
                stack[i] = idx
        # 最终stack的长度就构成了最长上升子序列的长度，用减法即可得到本题答案
        return len(target) - len(stack)


"""

tails的第i个位置记录nums中长度为i+1的所有递增子序列中，结尾最小的数字。
我们很容易证明，tails是一个递增的数组。首先，tails[0]一定是所有元素中最小的那个数字min1，因为长度为1的子序列中，结尾最小的数字就是序列中最小的那个。同样，长度为2的子序列中，结尾最小的的那个子序列的结尾元素一定大于min1，因为首先所有长度为2的递增子序列，第二个元素一定比第一个元素大，如果长度为2的子序列中某个子序列的结尾元素小于min1，那么在第一次操作中，这个元素就会更新为min1。对于长度为3的子序列，假设之前tails已经存储了前两个结尾最小数[a, b]，若长度为三的子序列结尾数字c3小于b，即[c1, c2, c3]是一个递增子序列，且c3 < b，则必然有c2 < b，这样和之前的结论b是长度为2的递增子序列结尾最小元素矛盾。所以，通过这样的一步步的反证法，很容易证明tails一定是一个递增的数组。那么很容易通过二分查找， 找到在tails数组中需要被更新的那个数。
每次我们遍历数组nums，只需要做以下两步中的一步：

如果 x 比所有的tails都大，说明x可以放在最长子序列的末尾形成一个新的自许下，那么就把他append一下，并且最长子序列长度增加1
如果tails[i-1] < x <= tails[i]，说明x需要替换一下前面那个大于x的数字，以便保证tails是一个递增的序列，那么就更新tails[i]
这样维护一个tails变量，最后的答案就是这个长度。

举一个具体的例子来说，比如我们的目标数组是[3, 4, 7, 2, 5]。我们从前往后开始遍历数组。tails = [3, 0, 0, 0, 0]
1. x = 3，此时i = 0，直接令tails[0] = 3，tails = [3, 0, 0, 0, 0]。说明到目前为止长度为1的递增子序列末尾最小为3。
2. x = 4，此时i != j，但是x大于tails的末尾，直接另tail[1] = 4， tails = [3, 4, 0, 0, 0]。说明到目前为止长度为1的递增子序列末尾最小为3，长度为2的递增子序列末尾最小为4。
3. x = 7，大于tails的末尾，直接令tails[2] = 7，tails = [3, 4, 7, 0, 0]。说明到目前为止长度为1的递增子序列末尾最小为3，长度为2的递增子序列末尾最小为4，长度为3的递增子序列末尾最小为7.
4. x = 2，此时x小于tails的末尾，需要用二分查找到比x大的最小的那个数更新之，查找到tails中比2大的最小数是3，更新tail[0] = 2，此时tails = [2, 4, 7, 0, 0]。说明到目前为止长度为1的递增子序列末尾最小为2，长度为2的递增子序列末尾最小为4，长度为3的递增子序列末尾最小为7。这一步理解很关键，[2, 4, 7, 0, 0]的存在并不是说目前为止的递增子序列是2 4 7，而是长度分别为1，2， 3的递增子序列目前所能得到的最小结尾元素是2，4，7。我们这样做的目的就是，通过维护tails中的元素，保证每次对于长度为i+1的一个子序列对应的tails[i]元素最小，这样新元素的出现并替换前面的一个值，这就是在告诉我们，“虽然在我之前，你们形成了一个长度为m的递增序列，但是呢，你们长度为m这个序列的末尾最大的一个数比我还大，不如把我和末尾最大的那个元素换一下，这样你看咱们还是一个递增序列，长度也不变，但是我和你们更亲近”。别的元素一听是这么个道理啊，于是就踢出最后一个元素，换上了这个新的更小的元素


"""