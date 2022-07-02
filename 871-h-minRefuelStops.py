class Solution:
    def minRefuelStops1(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        self.ans = False
        @lru_cache(None)
        def dfs(pos,fuel,presationIndex):
            if pos>=target or pos+fuel>=target:
                self.ans = True
                return 0
            elif presationIndex >= len(stations)-1:
                return 500
            curMin = 500
            for nextStation in range(presationIndex+1,len(stations)):
                nextPos,add = stations[nextStation]
                if pos+fuel>=nextPos:
                    curMin = min(curMin,dfs(nextPos,fuel-(nextPos-pos)+add,nextStation)+1)
            return  curMin if curMin<500 else 500
        t = dfs(0,startFuel,-1)
        if t>=500:
            return -1
        return t 
        """
        dp[k]到达位置为k的时候最少加多少次油
        k从station和taget中得到
        """

    def minRefuelStops2(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)
        for i, (pos, fuel) in enumerate(stations):
            for j in range(i, -1, -1):
                if dp[j] >= pos:
                    dp[j + 1] = max(dp[j + 1], dp[j] + fuel)
        return next((i for i, v in enumerate(dp) if v >= target), -1)

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        路上的不是加油站，而是一桶桶的油，每次经过的时候，就把油带上，
        当油不够的时候我们就取身上最大的那桶油加上，这样如果身上没油了，那么就到不了了
        """
        if target<=startFuel:return 0
        heap = []
        remainOil = startFuel # 剩余的汽油
        pos = 0 # 经过的加油站
        res = 0 # 加油次数
        while remainOil<target: # 没油了
            for i in range(pos,len(stations)):
                if remainOil>=stations[i][0]: #可以到达这个加油站
                    heapq.heappush(heap,-stations[i][1]) # 带上这桶油
                    pos+=1 # 这个加油站已经路过了
            if remainOil<target:
                if not heap: # 身上没油了
                    return -1
                remainOil-=heapq.heappop(heap) # python 只有最小堆 这里是取负数
                res+=1 # 加油次数加一
        return res
