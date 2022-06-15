class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1] * len(rains) # 第一天全部为空
        sunny = [] # 晴天日
        rain = {} # 上一次下雨日
        for i, x in enumerate(rains):
            if x > 0: # 第 i 天，x 湖泊下雨。
                if x in rain: # 湖满
                    j = bisect_left(sunny, rain[x]) # 插入位置，即右邻居
                    if j >= len(sunny): return []
                    ans[sunny.pop(j)] = x # 抽干 x
                rain[x] = i # 更新下雨日期
                ans[i] = -1
            else: sunny.append(i)
        return ans