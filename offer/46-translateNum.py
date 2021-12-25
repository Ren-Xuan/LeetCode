class Solution:
    def translateNum(self, num: int) -> int:
        return 1 if num<10 else ( self.translateNum(num//10)+(self.translateNum(num//100) if (num%100 <26 and num%100 >9) else 0))