class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        time = minutesToTest // minutesToDie +1
        pig = 0
        while pow(time,pig)<buckets:
            pig+=1
        return pig