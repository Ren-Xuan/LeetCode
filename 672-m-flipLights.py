class Solution(object):
    def flipLights(self, n, m):
        """
        因为前 6 个灯唯一地决定了其余的灯。
        这是因为修改第 x 灯光的每个操作都会修改 第 (x+6)灯光，
        因此 xx 灯光始终等于 (x+6)灯光。

        实际上，前 3 个灯唯一地确定了序列的其余部分
        解释一下为什么只与前三个有关
        Light 1 = 1 + a + c + d
        Light 2 = 1 + a + b
        Light 3 = 1 + a + c
        Light 4 = 1 + a + b + d
        Light 5 = 1 + a + c
        Light 6 = 1 + a + b
        因为light2,light3与light5,light6相同，
        不需要另外讨论，而light1和light3状态确定d的值，light2+d就确定了light4的状态
        """
        n = min(n, 3)
        if m == 0: return 1
        if m == 1: return [2, 3, 4][n-1]
        if m == 2: return [2, 4, 7][n-1]
        return [2, 4, 8][n-1]



