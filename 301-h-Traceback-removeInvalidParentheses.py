"""
*
* LOOK the No.22 generateParentesis
*
"""
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        
        #self.situ = self.result
        result = set()
        for i in range(n):
            print(i)
            enum = self.permuteUnique(i,n-i)
            for e in enum:
                situation = self.suitable(s,e)
                if len(situation)!=0:
                    result.add(self.suitable(s,e))
            if len(result)!=0:
                return list(result)
        return [""]

    def isvalid(self,string):  # 判断括号串是否合法
            l_minus_r = 0
            for c in string:
                if c == '(':
                    l_minus_r += 1
                elif c == ')':
                    l_minus_r -= 1
                    if l_minus_r < 0:
                        return False
            return l_minus_r == 0
    def permuteUnique(self,zero,one):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = [0]*zero+[1]*one
        if not nums:
            return []
        def _per(nums, beg, end, res):
            if beg == end - 1:
                res.append(nums[:])  # appen copy

            for i in range(beg, end):
                if nums[i] not in nums[beg:i]:
                    nums[i], nums[beg] = nums[beg], nums[i]
                    _per(nums, beg + 1, end, res)
                    nums[i], nums[beg] = nums[beg], nums[i]

        res = []
        _per(nums, 0, len(nums), res)
        return res

    def suitable(self,s,situ):
        #print(situ)
        stack = 0
        result = ""
        for i,b in enumerate(situ):
            if b == 1:
                result+=s[i]
        for i in range(len(result)):
            if result[i] == '(':
                stack+=1
            elif result[i] == ')':
                stack-=1
            if stack<0:
                return ""
        if stack != 0:
            return  ""
        return result
"""
best way
"""

class Solution2:
    def removeInvalidParentheses(self, s):
        def isValid(s):
            cnt = 0
            for c in s:
                if c == "(": cnt += 1
                elif c == ")": cnt -= 1
                if cnt < 0: return False  # 只用中途cnt出现了负值，你就要终止循环，已经出现非法字符了
            return cnt == 0

        # BFS
        #more like levle order
        level = {s}  # 用set避免重复
        while True:
            valid = list(filter(isValid, level))  # 所有合法字符都筛选出来
            if valid: return valid # 如果当前valid是非空的，说明已经有合法的产生了
            # 下一层level
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in "()":                     # 如果item[i]这个char是个括号就删了，如果不是括号就留着
                        next_level.add(item[:i]+item[i+1:])
            level = next_level
            print(len(level))

        

s = Solution2()
#print(s.suitable("()())()",[1,0,1,1,1,1,1]))
#print(s.suitable(")(",[1,0]))
#print(s.suitable(")(",[0,1]))
#print(s.suitable("(a)())()",[1,1,0,1,1,1,1,1]))
print(s.removeInvalidParentheses("()()()()()())()"))
print(s.removeInvalidParentheses("(a)())()"))

print(s.removeInvalidParentheses("()())()"))
print(s.removeInvalidParentheses("()"))
print(s.removeInvalidParentheses(")("))

print(s.removeInvalidParentheses("(()()))q(l)()o)(z"))
print(s.removeInvalidParentheses(")()m)(((()((()(((("))