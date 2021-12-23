class Solution:
    def longestDupSubstring1(self, s: str) -> str:
        
        n = len(s)
        subN = n//2
        for i in range(subN,0,-1):
            for start in range(n-i):
                if s[start:start+i] in s[start+1:]:
                    return s[start:start+i]
        return ""
    def longestDupSubstring2(self, s: str) -> str:
        indexDict = dict()
        for i,e in enumerate(s):
            if e not in indexDict:
                indexDict[e] = set()
                indexDict[e].add(i)
            else:
                indexDict[e].add(i)
        n = len(s)
        subN = n//2
        for i in range(subN,0,-1):
            for start in range(n-i):
                if len(indexDict[s[start]])==1:
                    continue
                for k in indexDict[s[start]]:
                    if k == start:
                        continue
                    else:
                        if s[start:start+i] == s[k:k+i]:
                            return s[start:start+i]
        return ""
    def longestDupSubstring3(self, s: str) -> str:
        indexDict = dict()
        for i,e in enumerate(s):
            if e not in indexDict:
                indexDict[e] = set()
            indexDict[e].add(i)
            #记录一下每一个字母的index
            #下次查询这个字母开始的相同子串的时候就不用遍历整个子串
            #用回溯法模板，每次如果某一个字母开头的相同子串数目大于等于2就说明可能是他是最终结果的前缀
            #将这样的前缀首字母index加入到nextIndexDict里面就减少了搜索空间，但是还是超时
        k = 1
        res = ""
        changed = True
        for n in range(len(s)):
            nextStrDict = dict()
            nextIndexDict = dict()
            changed = False
            for e in indexDict:
                if e not in nextStrDict:
                        nextStrDict[e] = set()
                if e not in nextIndexDict:
                        nextIndexDict[e] = set()
                for i in indexDict[e]:
                    if i+k >len(s):
                        continue
                    if s[i:i+k] in nextStrDict[e]:
                        res = s[i:i+k]
                        changed = True
                        nextIndexDict[e].add(i)
                    else:
                        nextStrDict[e].add(s[i:i+k])
                        nextIndexDict[e].add(i)
            indexDict = nextIndexDict
            k+=1
            if not changed:
                break
        return res
    def longestDupSubstring4(self, s: str) -> str:
        global n, ans 
        n, ans = len(s), ''
        L, R = 0, n
        while L < R:
            mid = (L + R + 1) >> 1
            if self.check(s, mid) == True: L = mid  #符合条件的最右端
            else: R = mid - 1 
        return ans

    def check(self, s: str, k: int) -> bool:
        visited = set()
        for i in range(n - k + 1): # 0 1 2 3 4 5  n=6, k=2,i可取到4 
            cur = s[i:i+k]
            if cur in visited:
                global ans
                ans = cur
                return True
            else: visited.add(cur)
        return False
    def longestDupSubstring(self, s: str) -> str:
        # 左指针
        left = 0
        # 右指针
        right = 1
        res = ""
        n = len(s)
        while right < n:
            # 判断后续字符串中是否含有判断字符串
            if s[left:right] in s[left + 1:]:
                if right - left > len(res):
                    res = s[left:right]
                # 字符串右侧右移一位
                right += 1
                continue
            # 字符串左侧右移
            left += 1
            if left == right:
                right += 1
        return res
