from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 回溯，无重复元素，根据剩余值凑成目标
        ans = []
        path = []
        candidates.sort() # 预先排序，
        # 收集逻辑为target == 0

        def backtracking(index,path,target):
            if index >= len(candidates) or target < 0:
                return 
            if target == 0: # 收集条件
                ans.append(path[:])
                return    
            for i in range(index,len(candidates)):  # 注意可以重复收集          
                path.append(candidates[i])  # 做选择
                backtracking(i,path,target-candidates[i])
                path.pop() # 取消选择
         
        backtracking(0,[],target)
        return ans

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = set()
        candidates = list(filter(lambda x : x<=target,candidates))#剪枝去掉一些不可能的元素
        candidates.sort()
        level = {str(e):e for e in candidates}
        if str(target) in level:
            self.ans.add(str(target))
        while len(level)>0:
            nextLevel = {}
            for cur in level:
                last = int(cur) if cur.find(',') == -1 else int(cur[::-1][:cur[::-1].find(',')][::-1])#这里的复杂度肯定爆炸高
                for e in candidates:
                    if last<e:
                        #这样是保证最后的ans结果里面每个组合(实际上我用的字符串，因为set不支持list作为key，
                        #最后暴力转换一遍就是数组了)都是递增的
                        #当前选择的candidate小于已经选择的组合的最后一个元素，就可以排除
                        continue
                    tmp = level[cur]+e
                    if tmp>target:
                        #剪枝，如果和已经大于target就可以跳出循环
                        break
                    elif tmp == target:
                        self.ans.add(cur+','+str(e))
                        if len(self.ans)>150:
                            #他规定了最后答案不超过150个我就用上去
                            return list(list(int(x) for x in e.split(',')) for e in self.ans)
                    nextLevel[cur+','+str(e)] = level[cur]+e 
            level = nextLevel
        return list(list(int(x) for x in e.split(',')) for e in self.ans)#字符串set转list