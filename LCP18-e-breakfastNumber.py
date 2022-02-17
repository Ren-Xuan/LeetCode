class Solution(object):
    def breakfastNumber(self, staple, drinks, x):
        staple.sort()
        drinks.sort()
        i = 0
        j = len(drinks) - 1
        ans = 0
        while i < len(staple) and j>=0:
            s = staple[i] + drinks[j]
            if s <=x:
                i+=1
                ans=ans + j + 1
            else:
                j-=1
        return ans % 1000000007