import itertools
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        res = set()
        def caculate(path):
            result = None
            try:
                result = eval(path)
            except Exception:
                pass
            return result

        def dfs(path,candidate,target,res):
            #print(path,"\t",candidate,res)
            if len(path)== 2 and path[-2] == "0" and path[-1] in ['0','1','2','3','4','5','6','7','8','9'] :
                #in python2 eval(1*05) can be done,and in python3 will throw error
                return
            elif len(path)>= 3 and path[-3] in ['+','-',"*"] and  path[-2] == "0" and path[-1] in ['0','1','2','3','4','5','6','7','8','9'] :
                #delete the situation: +05 or *01
                return
            cur = caculate(path)
            if cur == target and len(candidate) == 0:
                res.add(path)
                return
            elif len(candidate) == 0:
                return
            for e in ["+","-","*",""]:
                dfs(path+e+candidate[0],candidate[1:],target,res)
        dfs(num[0],num[1:],target,res)
        return list(res)

    def addOperators2(self, num: str, target: int):
        ans = []
        num = list(num)
        for comb in itertools.product(['+','-','*',''],repeat=len(num)-1):
            s = num[0]
            vals = [num[0]]
            for char, val in zip(comb,num[1:]):
                s += char + val
                if char == '':
                    vals[-1] += val
                else:
                    vals.append(val)
            for val in vals:
                if val[0] == '0' and len(val)>1:
                    break
            else:
                if eval(s) == target:
                    ans.append(s)
        return ans
s = Solution()
#print(s.addOperators("3456237490",9191))
#print(s.addOperators("105",5))
#print(s.addOperators("00",0))
res1 = s.addOperators("123456789",45)
res2 = s.addOperators2("123456789",45)
print("duoyude")
for e in res1:
    if e not in res2:
        print(e)
print("queshaode")
for e in res2:
    if e not in res1:
        print(e)