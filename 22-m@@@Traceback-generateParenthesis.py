"""
*   TraceBack
# DFS 
# BFS or level order
# level order is good for fixed length and Unrepeated set
# BFS with queue is simple and good for list all possibilities

* No.301 is same 
* No.22 is same
* offer.82 is same
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def isValid(s):
            cnt = 0
            for c in s:
                if c == "(": cnt += 1
                elif c == ")": cnt -= 1
                if cnt < 0: return False  # 只用中途cnt出现了负值，你就要终止循环，已经出现非法字符了
            return cnt == 0
        def count(s):
            cnt = 0
            n = 0
            for c in s:
                if c == "(": cnt += 1
                elif c == ")": cnt -= 1
                if cnt == 0:
                    n+=1
            return n
        # BFS
        level = {"()"}  # 用set避免重复
        for i in range(n-1):
            tmp_level = set()
            for item in level:
                for i in range(len(item)):
                    tmp_level.add(item[:i+1]+")"+item[i+1:])
            next_level = set()
            for item in tmp_level:
                for i in range(len(item)):
                    next_level.add(item[:i]+"("+item[i:])
            level = next_level
        return (list(filter(isValid,level)))

    def generateParenthesis2(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def isValid(s):
            cnt = 0
            for c in s:
                if c == "(": cnt += 1
                elif c == ")": cnt -= 1
                if cnt < 0: return False  # 只用中途cnt出现了负值，你就要终止循环，已经出现非法字符了
            return cnt == 0
        # BFS
        level = {"()"}  # 用set避免重复
        for i in range(n-1):
            tmp_level = set()
            for item in level:
                for i in range(len(item)):
                    s = item[:i+1]+")"+item[i+1:]
                    for j in range(len(s)):
                        tmp_level.add(s[:j]+'('+s[j:])
            
            level = tmp_level
        return (list(filter(isValid,level)))
    """
    the best way to solve the problem
    """
    def generateParenthesis3(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # BFS
        level = {"()"}  # 用set避免重复
        for i in range(n-1):
            tmp_level = set()
            for item in level:
                for i in range(len(item)+1):
                    s = item[:i]+"()"+item[i:]
                    tmp_level.add(s)
            level = tmp_level
        return (list(level))


s = Solution()
print(s.generateParenthesis(1))

print(s.generateParenthesis(2))

res = s.generateParenthesis(3)

print(s.generateParenthesis2(1))

print(s.generateParenthesis2(2))

print(s.generateParenthesis2(3))

print(s.generateParenthesis3(1))

print(s.generateParenthesis3(2))

print(s.generateParenthesis3(3))