from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        if x == 0:
            return 0
        start = {0:0}
        cnt = 0
        forbidden = set(forbidden)
        while len(start)!=0:
            nextLevel = dict()
            cnt+=1
            if cnt>4000:#不知道为什么
                return -1
            for e in start:
                if e == x:
                    return cnt-1
                elif  e>x+6*b:#不知道为什么
                    continue
                if start[e]!=1:
                    if e + a not in forbidden:
                        nextLevel[e+a] = 0
                        forbidden.add(e+a)
                    if e - b not in forbidden and e - b >0:
                        nextLevel[e-b] = 1
                else:
                    if e+a not in forbidden:
                        forbidden.add(e+a)
                        nextLevel[e+a] = 0
            start = nextLevel
        return -1
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        Q = deque()
        Q.append((0, 0, False))
        while Q:
            cur, cnt, used = Q.popleft()
            if cur == x:
                # 第一次到x即最小步数，因为队列后序元素cnt都是大于等于当前cnt的
                return cnt
            if cur + a < 6000 and cur + a not in forbidden:
                # 6000是往右探索的最大值，x最大为2000
                forbidden.add(cur+a)
                Q.append((cur+a, cnt+1, False))
            if not used and cur - b > 0 and cur - b not in forbidden:
                # forbidden.add(cur-b) 
                # 这里不能forbidden，因为后退回cur-b处时，无法覆盖前进到cur-b再后退到cur-2b的情况。
                Q.append((cur-b, cnt+1, True))
        return -1
