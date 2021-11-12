"""
2-sum问题

面试题41：和为s的两个数字VS和为s的连续正数序列
题目一：输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，
输出任意一对即可。
"""


class Solution:
    def twoSum(self, nums, target):
        """ 注意这题目 letcode 不是有序的，剑指offer 上的是有序的。一种方式是用 hash 来做
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_idx_map = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in num_idx_map:
                return [num_idx_map[diff], idx]
            else:
                num_idx_map[num] = idx

    def twoSum1(self, nums, target):
        """ 注意这题目 letcode 不是有序的，剑指offer 上的是有序的。可以先排序来做。之后首位指针向中间归并
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pairs = [(num, i) for i, num in enumerate(nums)]
        nums = sorted(pairs)
        print(nums)
        beg, end = 0, len(nums) - 1
        while beg < end:
            sum2 = nums[beg][0] + nums[end][0]
            if sum2 == target:
                break
            elif sum2 > target:
                end -= 1
            else:
                beg += 1
        return [nums[beg][1], nums[end][1]]
    """
    给定一个可能有重复数字的整数数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

    candidates 中的每个数字在每个组合中只能使用一次，解集不能包含重复的组合。 

    DFS  DFS   

    """
    """
    worest way
    use queue to BFS
    """
    
    def combinationSumWithQueue(self, candidates, target):
        if sum(candidates) == target:
            return [candidates]
        candidates = sorted(candidates)
        result = []
        t= []
        containTarget = False
        for e in candidates:
            if e < target:
                t.append(e)
            elif e == target and not containTarget:
                result.append([e])
                containTarget = True
        candidates = t
        from collections import deque
        q = deque()
        n = len(candidates)
        result = []

        q.append((candidates,sum(candidates)))
        while len(q)!=0:
            top = q.popleft()
            cnt = top[1]
            top = top[0]
            if cnt <=target:
                if cnt == target:
                    result.append(top)
                continue
            for i,e in enumerate(top):
                cnt -=e
                q.append((top[:i]+top[i+1:],cnt))
                cnt +=e
                
        res = []
        for e in result:
            tmp = sorted(e)
            if tmp not in res:
                res.append(tmp)

        return res

    """
    worest way
    deleting way
    """
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if sum(candidates) == target:
            return [candidates]
        candidates = sorted(candidates)
        result = set()
        level = set()
        t= []
        for e in candidates:
            if e < target:
                t.append(e)
        candidates = t
        
        level.add(tuple(t))
        #BFS
        #level order
        for t in range(len(candidates)):
            # n level
            #print(level)
            nextLevel = set()
            for item in level:
                for i in range(len(item)):
                    arr = item[:i]+item[i+1:]
                    count = sum(arr)
                    if count < target:
                        continue
                    elif count == target:
                        result.add(arr)
                    else:
                        nextLevel.add(arr)
            level = nextLevel
        result = list(result)
        result.sort(key= lambda x: len(x),reverse= True)
        return result

    """
    ==========================================
                DFS
                deleting way
                over time 
    """
    def combinationSum3(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if sum(candidates) == target:
            return [candidates]
        candidates = sorted(candidates)

        t= []
        result = []
        for e in candidates:
            if e <= target:
                if e == target:
                    result.append([e])
                    break
                t.append(e)
        candidates = t
        #print(candidates)
        def traceBack(arr,n,target,s):
            #s = sum(arr)
            if s == target:
                if arr not in result:
                    result.append(arr)
                return
            elif s < target:
                return
            
            for i in range(n,len(arr)):# consider the n************
                traceBack(arr[:i]+arr[i+1:],i,target,s - arr[i])
        s = sum(candidates)
        traceBack(candidates,0,target,s)
        return result
    
    """
    ==========================================
                Final vision
                DFS
                generating way
                120ms

    """
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if sum(candidates) == target:
            return [candidates]
        #candidates = sorted(candidates)
        result = []
        t= []
        visited = False
        for e in candidates:
            if e < target:
                t.append(e)
            elif e == target and not visited:
                result.append([e])
                visited = True
        
        candidates = t
        d = dict()
        for e in candidates:
            if e not in d:
                d[e] = 1
            else:
                d[e]+=1
        def traceBack(arr,s,target):
            #s = sum(arr)
            if s == target:
                if arr not in result:
                    result.append(arr)
                return
            elif s > target:
                return
            
            for e in d:
                if d[e]>0:
                    d[e]-=1
                    traceBack(arr+[e],s+e,target)
                    d[e]+=1
        traceBack([],0,target)
        res = []
        for e in result:
            tmp = sorted(e)
            if tmp not in res:
                res.append(tmp)
        return res

    """
    ==========================================
                Final vision
                DFS NOT RECUR
                generating way
                80ms
    """
    def combinationSumNotRecur(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if sum(candidates) == target:
            return [candidates]
        #candidates = sorted(candidates)
        result = []
        t= []
        containTarget = False
        for e in candidates:
            if e < target:
                t.append(e)
            elif e == target and not containTarget:
                result.append([e])
                containTarget = True
        candidates = t
        originVisited = dict()
        for e in candidates:
            if e not in originVisited:
                originVisited[e] = 1
            else:
                originVisited[e] +=1

        level = [[]]

        for o in range(len(candidates)):
            nextLevel = []
            for item in(level):
                cnt = sum(item)
                #regenerate visited dict
                visited = originVisited.copy()
                #print(item,visited)
                for e in item:
                    visited[e]-=1
                for e in visited:
                    if visited[e]>0:
                        visited[e]-=1
                        cnt +=e
                        if cnt == target:
                            result.append(item+[e])
                        elif cnt < target:
                            ##################################
                            nextLevel.append(item+[e])
                        visited[e]+=1
                        cnt-=e
            level = nextLevel

        res = []
        for e in result:
            tmp = sorted(e)
            if tmp not in res:
                res.append(tmp)
        return res
    """
        ==========================================
                Final vision
                DFS NOT RECUR
                generating way
                140ms
    """
    def combinationSumRecur(self, candidates, target):
        # 回溯，注意去重逻辑
        if sum(candidates) == target:
            return [candidates]
        candidates = sorted(candidates)
        result = []
        t= []
        containTarget = False
        for e in candidates:
            if e < target:
                t.append(e)
            elif e == target and not containTarget:
                result.append([e])
                containTarget = True
        candidates = t
        originVisited = dict()
        for e in candidates:
            if e not in originVisited:
                originVisited[e] = 1
            else:
                originVisited[e] +=1
        n = len(candidates)
        result = []


        def backtracking(path,aim):
            if aim == 0:
                result.append(path[:])
                return 
            if aim < 0:
                return 
            used = originVisited.copy()
            for e in path:
                    used[e]-=1
            for e in used:
                if used[e] == 0: # 这个数被用过
                    continue  # 不要手误写成return
                used[e] -=1
                backtracking(path+[e],aim-e) # 注意这里是i+1而不是index+1,*******important,only delete the index which is larger than appeding position
        
        backtracking([],target)
        if containTarget:
            result.append([target])
        res = []
        for e in result:
            tmp = sorted(e)
            if tmp not in res:
                res.append(tmp)
        return res



    """
    generating way
    Final final final version
    remove the repeated step
    """
    def combinationSumFinal(self, candidates, target):
        # 回溯，注意去重逻辑
        if sum(candidates) == target:
            return [candidates]
        candidates = sorted(candidates)
        result = []
        t= []
        containTarget = False
        for e in candidates:
            if e < target:
                t.append(e)
            elif e == target and not containTarget:
                result.append([e])
                containTarget = True
        candidates = t

        n = len(candidates)
        result = []
        used = [False for i in range(n)]

        def backtracking(choice,path,aim,index):
            if aim == 0:
                result.append(path[:])
                return 
            if aim < 0:
                return 

            for i in range(index,n):
                if used[i] == True: # 这个数被用过
                    continue  # 不要手误写成return
                """=========================================================="""
                if i > 0 and choice[i] == choice[i-1] and used[i-1] == False: 
                    # 这里不能是used[i-1] == True，因为是顺序选取而不是可以倒着选
                    continue  # 不要手误写成return
                """=========================================================="""
                used[i] = True 
                backtracking(choice,path+[choice[i]],aim-choice[i],i+1) # 注意这里是i+1而不是index+1,*******important,only delete the index which is larger than appeding position
                used[i] = False 
        
        backtracking(candidates,[],target,0)
        if containTarget:
            result.append([target])
        return result





def test():
    s = Solution()
    print(s.twoSum([3, 2, 4], 6) == [1, 2])
    print(s.twoSum([2, 7], 9) == [0, 1])
    print(s.twoSum([2, 7, 11, 15], 9) == [0, 1])
    print(s.twoSum([1, 2, 4, 7, 11, 15], 15) == [2, 4])
    print(s.combinationSumRecur([10,1,2,7,6,1,5,8],8))#1 1 2 5 6 
    print(s.combinationSumRecur([14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12],27))
test()