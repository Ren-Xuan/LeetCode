class Solution:
    def countRoutesOvertime(self, locations, start: int, finish: int, fuel: int) -> int:
  
        level = set()
        n = len(locations)
        def cost(i,j):
            return abs(locations[i]-locations[j])
        cnt = 0
        for i in range(n):
            if i ==start:
                continue
            if fuel >= cost(start,i):
                level.add((i,fuel-cost(start,i)))
                if i == finish:
                    cnt+=1

        l = 1
        while True:
            nextLevel = []
            for item in level:
                for j in range(n):
                    if item[0] == j:
                        continue
                    if  item[1] >= cost(item[0],j):
                        if j == finish:
                            cnt+=1
                        nextLevel.append((j,item[1]-cost(item[0],j)))
            level = nextLevel
            if len(level) == 0:
                break
            l+=1
           
        return cnt
    def countRoutes(self, locations, start: int, finish: int, fuel: int) -> int:
        """
        dp[i][j] = dp[i][j]表示在第i个城市剩余j的汽油的方案数
        dp[i][j - k] = dp[i][j-k] + dp[r][j] 其中k = cost(r,i)
        """
        n = len(locations)
        def cost(i,j):
            return abs(locations[i]-locations[j])
        dp = [[0] * (fuel+1) for _ in range(n)]
        changed = True
        dp[start][fuel] = 1
        for k in range(fuel,-1,-1):
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    d = cost(i,j)
                    if k>=d:
                        dp[j][k-d] =(dp[j][k-d] + dp[i][k])
        result = 0
        for i in range(0,fuel+1):
            result+=(dp[finish][i])

        return result%(pow(10,9)+7)
    def countRoutesOvertime(self, locations, start: int, finish: int, fuel: int) -> int:

        n = len(locations)
        def cost(i,j):
            return abs(locations[i]-locations[j])
        dp = [[0] * (fuel+1) for _ in range(n)]
        def dfs(locations,i,finish,fuel,dp):
            if fuel<0:
                return 0
            if dp[i][fuel] !=0:
                return dp[i][fuel]
            result = 0
            if i == finish:
                result+=1
            for j in range(len(locations),-1,-1):
                if i == j:
                    continue
                result+=dfs(locations,j,finish,fuel - cost(i,j),dp)
            dp[i][fuel] = result
            return result
        return dfs(locations,start,finish,fuel,dp)%(pow(10,9)+7)
        
        