class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        import re
        if '.' not in s:
            s+="."
        if '.' not in t:
            t+="."
        if '(' not in s:
            s+="(0)"
        if '(' not in t:
            t+="(0)"
        #提取括号内的内容
        route1 = re.search('\(.*?\)',s).group()[1:-1]
        route2 = re.search('\(.*?\)',t).group()[1:-1]
        #提取(之前的内容
        pre1 = re.search('.*?\(',s).group()[:-1]
        pre2 = re.search('.*?\(',t).group()[:-1]
        res1 = pre1+(route1*20)
        res2 = pre2+(route2*20)
        return abs(float(res1) - float(res2)) <1e-10
        