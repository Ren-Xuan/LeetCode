class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ans = 0
        #对于每个房屋，要么用前面的暖气，要么用后面的，二者取近的，得到距离；
        #对于所有的房屋，选择最大的上述距离。
        houses.sort()
        heaters.sort()
        j = 0
        for i, house in enumerate(houses):
            curDistance = abs(house - heaters[j])
            while j + 1 < len(heaters) and abs(houses[i] - heaters[j]) >= abs(houses[i] - heaters[j + 1]):
                j += 1
                curDistance = min(curDistance, abs(houses[i] - heaters[j]))
            ans = max(ans, curDistance)
        return ans
