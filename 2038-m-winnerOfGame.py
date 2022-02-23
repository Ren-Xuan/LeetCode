class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        d={'A':0,'B':0}
        for i in range(1,len(colors)-1):
            if colors[i]==colors[i-1]==colors[i+1]:
                d[colors[i]]+=1
        if d['A']>d['B']:
            return True
        else:
            return False