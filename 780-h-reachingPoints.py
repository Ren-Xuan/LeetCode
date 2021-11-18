class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx>0 and ty>0:
            if sx ==tx and sy == ty:
                return True
            if tx>ty:
                tx -= max((tx-sx)//ty,1)*ty
            else:
                ty -= max((ty-sy)//tx,1)*tx
        return False
    def reachingPoints2(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if tx<sx or ty<sy:
            return False
        if tx == sx and (ty-sy)%sx!=0:
            return False
        if ty == sy and (tx-sx)%sy!=0:
            return False
        if tx>sx and ty>sy:
            return self.reachingPoints(sx,sy,tx%ty,ty%tx)
        return True