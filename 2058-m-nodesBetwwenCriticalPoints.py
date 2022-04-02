class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        #维护上一个和第一个临界点的位置
        minDist = maxDist = -1
        first = last = -1
        pos = 0

        cur = head
        while cur.next.next:
            # 获取连续的三个节点的值
            x, y, z = cur.val, cur.next.val, cur.next.next.val
            # 如果 y 是临界点
            if y > max(x, z) or y < min(x, z):
                if last != -1:
                    # 用相邻临界点的距离更新最小值
                    minDist = (pos - last if minDist == -1 else min(minDist, pos - last))
                    # 用到第一个临界点的距离更新最大值
                    maxDist = max(maxDist, pos - first)
                if first == -1:
                    first = pos
                # 更新上一个临界点
                last = pos
            cur = cur.next
            pos += 1
        
        return [minDist, maxDist]

