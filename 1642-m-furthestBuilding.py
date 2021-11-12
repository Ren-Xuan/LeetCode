from heapq import * 
class Solution:
    def furthestBuilding(self, heights, bricks: int, ladders: int) -> int:
        left = 0
        right = len(heights)-1
        def check(dest,heights,bricks,ladders):
            q = []
            for i in range(1,dest+1):
                if heights[i]>heights[i-1]:
                    heappush(q,-(heights[i]-heights[i-1]))
            t = 0
            while bricks!=0 or ladders!=0:
                if len(q) == 0:
                    return True
                t = -heappop(q)
                if ladders!=0:
                    ladders-=1
                if ladders == 0 and bricks!=0:
                    bricks-=1
            if len(q) == 0:
                return True
            else:
                return False
        while left<right:
            mid  = (left+right)//2
            if check(mid,heights,bricks,ladders):
                left = mid
            else:
                right = mid -1

        return left

def check(dest,heights,bricks,ladders):
            q = []
            for i in range(1,dest+1):
                if heights[i]>heights[i-1]:
                    heappush(q,-(heights[i]-heights[i-1]))
            t = 0
            print(q)
            while bricks!=0 or ladders!=0:
                if len(q) == 0:
                    return True
                t = -heappop(q)
                if ladders!=0:
                    ladders-=1
                    continue
                if ladders == 0 and bricks!=0:
                    if bricks>=t:
                        bricks-=t
                    else:
                        return False
            if len(q) == 0:
                return True
            else:
                return False
def furthestBuilding(self, heights, bricks: int, ladders: int) -> int:
        left = 0
        right = len(heights)-1
        def check(dest,heights,bricks,ladders):
            q = []
            for i in range(1,dest+1):
                if heights[i]>heights[i-1]:
                    heappush(q,-(heights[i]-heights[i-1]))
            t = 0
            #print(q)
            while bricks!=0 or ladders!=0:
                if len(q) == 0:
                    return True
                t = -heappop(q)
                if ladders!=0:
                    ladders-=1
                    continue
                if ladders == 0 and bricks!=0:
                    if bricks>=t:
                        bricks-=t
                    else:
                        return False
            if len(q) == 0:
                return True
            else:
                return False
        while left<right:
            mid  = (left+right)//2
            print(left,right,mid)
            if check(mid,heights,bricks,ladders):
                left = mid+1
            else:
                right = mid
        print(left)
        if check(left,heights,bricks,ladders):
            return left
        return left-1
print(check(4,[1,2,3,4,5],0,3))
print(check(4,[4,2,7,6,9,14,12],5,1))
print(furthestBuilding(4,[1,2,3,4,5],0,3))
print(furthestBuilding(4,[4,2,7,6,9,14,12],5,1))