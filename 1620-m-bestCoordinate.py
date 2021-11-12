class Solution(object):
    def bestCoordinate(self, towers, radius):
        """
        :type towers: List[List[int]]
        :type radius: int
        :rtype: List[int]
        """
        import math
        def distanceSquare(x1,y1,x2,y2):
            return (x1 - x2)**2+(y1 - y2)**2

        def generatePos(towers,radius):
            res = set()
            for tower in towers:
                for x in range(tower[0]-radius,tower[0] + radius + 1):
                    for y in range(tower[1] - radius ,tower[1] + radius + 1):
                        if distanceSquare(tower[0],tower[1],x,y) <= radius**2:
                            res.add((x,y))    
            return res

        def signalSum(pos,towers,radius):
            s = 0
            for tower in towers:
                dis = distanceSquare(pos[0],pos[1],tower[0],tower[1])
                distance = math.sqrt(dis)
                #print(pos,tower,dis,distance)
                if distance<=radius:
                    s += tower[2]//(1+distance)

            return s
        
        #print(signalSum((43,1),towers,radius))
        
        candidate = generatePos(towers,radius)
        #print(candidate)
        m = 0.0
        result = [towers[0][0],towers[0][1]]
        for pos in candidate:
            s = signalSum(pos,towers,radius)
            #print(pos,s,m)
            if s > m:
                m = s
                result = pos
            elif s == m:
                if pos[0]<result[0] or (pos[0] == result[0] and pos[1] < result[1]):
                    result = pos
        if m == 0.0:
            return [0,0]
        result=list(result)
        return result

s = Solution()
towers = [[42,0,0]]
radius = 7
print(s.bestCoordinate(towers,radius))

towers = [[1,2,5],[2,1,7],[3,1,9]]
radius = 2
print(s.bestCoordinate(towers,radius))
print("ed")

towers = [[23,11,21]]
radius = 9
print(s.bestCoordinate(towers,radius))
print("ed")
towers = [[2,1,9],[0,1,9]]
radius = 2
print(s.bestCoordinate(towers,radius))
print("ed")