class Solution:
    def repeatedStringMatch(self, a,b):
        """
        string 中 find() 返回值是子串在母串中的位置（下标记录）
        如果没有找到，那么会返回一个特别的标记 -1 
        """
        dictA = set(a)
        for e in b:
            if e not in dictA:
                return -1
        #判断是否b中有a没出现过的字符
        """
        例如a = "a", b = "aa"，复制的次数是 bSize / aSize
        例如a = "abcd", b = "cdabcdab"，复制的次数是 bSize / aSize + 1
        例如：a = "abcd" , b = "dabcdabcda" ,需要复制 bSize / aSize + 2 次，得到 "abcdabcdabcdabcd"
        只有这三种可能，复制再多次也只是重复
        """
        k = len(b) // len(a)
        t = a*k
        for i in range(3):
            if b in t:
                #or t.find(b) !=-1
                return k+i
            t+=a
        return -1