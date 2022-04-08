from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        NEIGHBORS = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        CACHE = {"123450": 0}
        q = deque([("123450", 5, 0)])
        while q:
            status, x, step = q.popleft()
            s = list(status)
            for y in NEIGHBORS[x]:
                s[x], s[y] = s[y], s[x]
                next_status = "".join(s)
                if not next_status in CACHE:
                    q.append((next_status, y, step + 1))
                    CACHE[next_status] = step + 1
                s[x], s[y] = s[y], s[x]
        status = "".join(str(num) for num in sum(board, []))
        return CACHE.get(status, -1)

