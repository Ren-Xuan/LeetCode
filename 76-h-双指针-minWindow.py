import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_dict = collections.defaultdict(int) #用来装分别需要的字符数量，包括必要的和非必要的，需要的必要字符数量>0，非必要的字符数量<0
        for ch in t:   #初始化需要的必要字符数量
            need_dict[ch] += 1
        need_cnt = len(t) #用来判断总共需要多少字符才能达到要求
        i = j = 0
        res = [0,float('inf')]
        for j in range(len(s)):
            if need_dict[s[j]] > 0: #只有必要字符的数量才可能>0
                need_cnt -= 1
            need_dict[s[j]] -= 1  #任意值都可以装进need_dict，但是非必要字符只可能<0
            if need_cnt == 0:  # 需要的字符都足够了
                while need_cnt == 0: #开始准备右移左指针，缩短距离
                    if j-i < res[1] - res[0]: #字符串更短，替换答案
                        res = [i,j]
                    need_dict[s[i]] += 1    #在移动左指针之前先将左指针的值加回来，这里可以是非必要字符
                    if s[i] in t and need_dict[s[i]] > 0: #确认是必要字符且不多于所需要的数量（有多余的话只可能<=0，因为上一句我们已经将字符+1了）后，将need_cnt+1
                        need_cnt += 1    
                    i += 1   #右移左指针，寻找下一个符合的子串
        return s[res[0]:res[1]+1] if res[1]-res[0]<len(s) else ''