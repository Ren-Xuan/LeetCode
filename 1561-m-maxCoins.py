from typing import _SpecialForm


class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        """
        Bob 每次取最小的那堆
        然后考虑Alice，每次Alice取最多那堆，然后你获得的就是reward = total - sum(Alice) - Bob
        then 最大化reward
        policy = 由于Alice取1次，我也一定努力取一次，直到最后剩下一堆银币，这一堆硬币只有一个
                    当我一轮中不能选硬币的时候一定是[x,0,0,...,0,0] x>=0
                    then 最小化x
                    这时候policy就是 每次让Alice拿最高那堆硬币
                    我拿次高那堆硬币

        """
        piles.sort(reverse= True)
        n = len(piles)//3
        count = 0
        for i in range(n):
            count+=piles[2*i+1]
        return count
    """
        假如每次取不是取一堆，而是取一个可以这样做
        Bob 每次取最小的那堆
        然后考虑Alice，每次Alice取最多那堆，然后你获得的就是reward = total - sum(Alice) - Bob
        then 最大化reward
        policy = 由于Alice取1次，我也一定努力取一次，直到最后剩下一堆银币
                    当我一轮中不能选硬币的时候一定是[x,0,0,...,0,0] x>=0
                    then 最小化x
                    这时候policy就是 每次让Alice拿最高那堆硬币
                    我拿次高那堆硬币

        """
    def minCoins2(self,piles):

        pq = queue.PriorityQueue()
        min = 100001
        minIndex = -1
        for i,e in enumerate(piles):
            if e < min:
                min = e
                minIndex = i   
                     
        piles[minIndex]=0
        for e in piles:
            pq.put(-e)
        print(piles)
        count = 0
        for i in range(min):
            first = -pq.get()
            second = -pq.get()
            count+=1
            pq.put(-(first-1))
            pq.put(-(second-1))
        second = 0
        print("c:",count)
        while True:
            first = -pq.get()
            second = -pq.get()
            if first == 0 or second == 0:
                return count
            first-=1
            second-=1
            count+=1
            pq.put(-first)
            pq.put(-second)

s = Solution()
print(s.maxCoins( [2,4,1,2,7,8]))
print(s.maxCoins( [2,4,5]))
print(s.maxCoins([9,8,7,6,5,1,2,3,4]))