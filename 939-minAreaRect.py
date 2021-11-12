class Solution:
    def minAreaRect(self, points) -> int:
        n = len(points)
        area = 40000*40000
        i = 0
        j = 0
        s = set()
        for e in points:
            s.add((e[0],e[1]))
        for  i in range(n):
            for j in range(i+1,n):
                iX,iY = points[i][0],points[i][1]
                jX,jY = points[j][0],points[j][1]
                if iX == jX:
                    continue
                if iY == jY:
                    continue
                if (iX,jY) not in s:
                    continue
                if (jX,iY) not in s:
                    continue
                sum = abs(iX - jX)*abs(iY - jY)
                if sum < area:
                    area = sum
        if area == 40000*40000:
            return 0
        return area
                
                
s = Solution()
print(s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))
print(s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))
print(s.minAreaRect([[26030,39519],[8964,34856],[26030,34856],[13012,39519],[30289,39519],[13012,21894],[13012,34856],[30289,21894],[30289,48],[8964,48],[8964,39519]]))