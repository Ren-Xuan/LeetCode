class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def forward(x):
            return sum([sqrt((x[0] - x1) ** 2 + (x[1] - y1) ** 2) for x1, y1 in positions])
        def backward(x):
            x0_b = sum([(x[0]-x1)/sqrt((x[0] - x1) ** 2 + (x[1] - y1) ** 2) for x1,y1 in positions])
            x1_b = sum([(x[1]-y1)/sqrt((x[0] - x1) ** 2 + (x[1] - y1) ** 2) for x1,y1 in positions])
            return x0_b,x1_b
        n = 1000
        x0 = 0
        x1 = 0
        k = 0.001
        for epoch in range(n):
            x0_b,x1_b = backward((x0,x1))
            x0 -=k*x0_b
            x1 -=k*x1_b
        print(x0,x1)

        return forward((x0,x1))