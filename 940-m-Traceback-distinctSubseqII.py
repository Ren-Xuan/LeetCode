class Solution(object):
    def distinctSubseqIIOverTimeSimple(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isValid(path,dest):
            return True
        
        def traceBack(path,candidate,dest,start,end,res):
            res.add(path)

            for i in range(len(candidate)):
                traceBack(path+candidate[i],candidate[i+1:],dest,start,end,res)
            
        res = set()
        traceBack("",s,s,0,0,res)
        return (len(res)-1) %1000000007

    def distinctSubseqIIOverTime(self, s):
        """
        :type s: str
        :rtype: int
        """

        def isValid(path,dest):
            return True
        
        def traceBack(path,candidate,dest,start,end,res):
            #res.add(path)
            res[0]+=1
            s = set()
            for i in range(len(candidate)):
                if candidate[i] not in s:
                    s.add(candidate[i])
                    traceBack(path+candidate[i],candidate[i+1:],dest,start,end,res)
            

        res = [0]
        traceBack("",s,s,0,0,res)
        return (res[0]-1) %1000000007

    def distinctSubseqIIOverTimeII(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        def traceBack(path,dest,start,end,res):
            #res.add(path)
            res[0]+=1
            s = set()
            for i in range(len(path)+1):
                if path[i] not in s :
                    s.add(path[i])
                    traceBack(path[:i]+path[i+1:],dest,start,end,res)
        #res = set()
        res = [0]
        traceBack(s,s,0,0,res)
        return (res[0]-1) %1000000007


    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        mod = 10 ** 9 + 7
        m = {}
        for c in S:
            m[c] = (sum(m.values()) + 1) % mod
        return sum(m.values()) % mod
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        end = [0] * 26
        for c in S:
            end[ord(c) - ord('a')] = sum(end) + 1
        return sum(end) % (10**9 + 7)
"""
这样去思考，我们遍历输入的S，例如a b a

i=0,此时，我们碰到的以a结尾的字符串只有a，
i=1,此时，以b结尾的字符串有ab和b，也就是a+b，" "+b（上一次的结果加上b）
i=2,此时，以a结尾的字符串有aba、ba、aa和a，也就是ab+a，b+a，a+a，" "+a（上一次的结果加上a）。所以我们最后的结果就是以a和b结尾的字符串个数总和。
"""
    
s = Solution()
print(s.distinctSubseqII("abcdefssacsaafkfksscsldfsv"))
print(s.distinctSubseqII("abcdefef"))