from collections import defaultdict
from typing import List



class SegmentTree:
    def __init__(self) -> None:
        self.tree = defaultdict(int)
        self.mark = defaultdict(int)

    def update(self, l, r, val, cl, cr, p=1):
        if cl>r or cr<l:
            return
        elif cl>=l and cr<=r:
            self.tree[p] = val
            self.mark[p] = val
        else:
            mid = (cl+cr)//2
            self.pushDown(p)
            self.tree[p] = max(val, self.tree[p])
            self.update(l, r, val, cl, mid, p*2)
            self.update(l, r, val, mid+1, cr, p*2+1)

    def query(self, l, r, cl, cr, p=1):
        if cl>r or cr<l:
            return 0
        elif cl>=l and cr<=r:
            return self.tree[p]
        else:
            mid = (cl+cr)//2
            self.pushDown(p)
            return max(self.query(l, r, cl, mid, p*2), self.query(l, r, mid+1, cr, p*2+1))
    
    def pushDown(self, p):
        if self.mark[p]:
            self.tree[p*2] = self.mark[p]
            self.tree[p*2+1] = self.mark[p]
            self.mark[p*2] = self.mark[p]
            self.mark[p*2+1] = self.mark[p]
            self.mark[p] = 0

class Solution(object):
    def fallingSquares1(self, positions):
        qans = [0] * len(positions)
        for i, (left, size) in enumerate(positions):
            right = left + size
            qans[i] += size
            for j in range(i+1, len(positions)):
                left2, size2 = positions[j]
                right2 = left2 + size2
                if left2 < right and left < right2: #intersect
                    qans[j] = max(qans[j], qans[i])

        ans = []
        for x in qans:
            ans.append(max(ans[-1], x) if ans else x)
        return ans
    


    def fallingSquares2(self, positions: List[List[int]]) -> List[int]:
        points = set()
        for p in positions:
            points.add(p[0])
            points.add(p[0]+p[1]-1)
        points = sorted(points)
        d, n = {}, len(points)
        for i in range(n): d[points[i]] = i

        st = SegmentTree()
        ans = []
        for p in positions:
            start, end = d[p[0]], d[p[0]+p[1]-1]
            cur = st.query(start, end, 0, n-1)
            st.update(start, end, cur+p[1], 0, n-1)
            ans.append(st.query(0, n-1, 0, n-1))
        return ans
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
            # 离散化
            index_set = set()
            for pos in positions:
                index_set.add(pos[0])
                index_set.add(pos[0] + pos[1] - 1)
            index_set = sorted(list(index_set))
            
            index_map = {val: idx for idx, val in enumerate(index_set)}
            
            ans = []
            res = 0
            ground = [0 for _ in range(len(index_map))]
            for pos in positions:
                x, y = index_map[pos[0]], index_map[pos[0] + pos[1] - 1]
                # 如需进一步优化, 这里的查询max和update可以用线段树处理
                max_cur = max(ground[x : y + 1])
                cur_res = max_cur + pos[1]
                for idx in range(x, y + 1):
                    ground[idx] = cur_res
                
                res = max(cur_res, res)
                ans.append(res)
            return ans

