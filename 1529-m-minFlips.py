class Solution:
    def minFlips(self, target: str) -> int:
        """
        1 1
        10 2
        101 3
        1010 -> 1011->101 4
        10101 -> 10100 -> 1010 :5
        101010 ->101011->10101->6
        """
        cur = ""
        target = '0'+target
        for i in range(len(target)):
            if target[i] == '1':
                if len(cur) == 0 or cur[-1] == '1':
                    cur+='0'
            else:
                if len(cur) == 0 or cur[-1] =='0' :
                    cur+='1'
        return len(cur)-1