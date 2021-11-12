class Solution:
    def containsNearbyAlmostDuplicate1(self, nums, k: int, t: int) -> bool:
        ls = [[nums[i], i] for i in range(len(nums))]
        ls.sort(key=lambda x: x[0])
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if ls[j][0] - ls[i][0] > t:
                    break
                if abs(ls[j][1] - ls[i][1]) <= k:
                    return True
        return False
    def containsNearbyAlmostDuplicate(self,nums,k:int,t:int)->bool:
        """
        我们也可以使用利用桶排序的思想解决本题。
        我们按照元素的大小进行分桶，维护一个滑动窗口内的元素对应的元素。

        对于元素 x，其影响的区间为[x−t,x+t]。
        于是我们可以设定桶的大小为t+1。
        如果两个元素同属一个桶，那么这两个元素必然符合条件。
        如果两个元素属于相邻桶，那么我们需要校验这两个元素是否差值不超过t。
        如果两个元素既不属于同一个桶，也不属于相邻桶，那么这两个元素必然不符合条件。

        具体地，我们遍历该序列，
        假设当前遍历到元素 x，那么我们首先检查 x 所属于的桶是否已经存在元素，
        如果存在，那么我们就找到了一对符合条件的元素，
        否则我们继续检查两个相邻的桶内是否存在符合条件的元素。

        实现方面，我们将 int 范围内的每一个整数 x 表示为 x =(t+1)×a+b(0≤b≤t) 的形式，
        这样 x 即归属于编号为 a 的桶。
        因为一个桶内至多只会有一个元素，所以我们使用哈希表实现即可。
        
        """
        mp = dict()
        def getID(x,w):
            if x>=0:
                return x//w
            else:
                return (x+1)//w - 1
        for i,e in enumerate(nums):
            id = getID(e,t+1)
            if id in mp:#这里就隐含了每个桶元素只有一个
                return True
            if id-1 in mp:
                if abs(e- mp[id-1])<=t:
                    return True
            if id+1 in mp:
                if abs(e- mp[id+1])<=t:
                    return True
            mp[id] = e
            if i>=k:
                mp.pop(getID(nums[i-k],t+1))
        return False