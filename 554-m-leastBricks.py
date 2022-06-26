class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        res = {0: 0}
        for lvl in wall:
            pos = 0
            for brick in lvl[:-1]:
                pos += brick
                res[pos] = res.get(pos, 0) +1
        return len(wall)-max(res.values())