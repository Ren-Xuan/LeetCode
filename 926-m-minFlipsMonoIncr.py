class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        cnt=0                 #这道题使用了评论中大佬 Peter 的思路。设置一个光标从最左侧开始移动，左侧全为0，右侧全为1，统计左右改完之后要多少步
        cntlast=0
        znt=0
        for i in S:
            if i == '1':
                cnt+=1
            else:
                znt+=1        #统计字符串中0的个数，即将光标移动到最左边的时候，右边全为1要多少步
                cnt-=1
            if cnt < cntlast:
                cntlast=cnt
        return znt+cntlast