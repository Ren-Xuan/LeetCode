class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        # 首先找到字符串中相同字母出现的位置。保存在字典中
        dict1 = defaultdict(list)
        for i, val in enumerate(s):
            dict1[val].append(i)
        # 可以从字典的值中得到每个字母出现的开始位置和结束位置，然后从其中找到满足条件2的
        # 所有子串的索引
        substrings = []
        for key in dict1:
            substring = [dict1[key][0], dict1[key][-1]]
            flag = True
            # 子串开始向后遍历，如果遍历到某个字母开始的索引小于该字母的索引
            # 说明前面得到的满足条件2的子串包括该子串,直接跳过
            index = substring[0]
            while index < substring[1]:
                if dict1[s[index]][0] < substring[0]:
                    flag = False
                    break
                # 扩展这个子串，以满足条件2
                substring[1] = max(substring[1], dict1[s[index]][-1])
                index += 1
            if flag:
                substrings.append(substring)
        # 得到的这个substrings数组中的元素只可能出现包含或者不相交的情况
        # 要得到的结果要求包含的子字符串数目最多，那么每个字符串应该尽可能短
        # 对得到的结果按长短排序
        substrings = sorted(substrings, key=lambda x: x[1] -x[0])
        ans = []
        res = []
        for res1 in substrings:
            flag = True
            for value in ans:
                if res1[0] < value[0] and res1[1] > value[1]:
                    flag = False
                    break
            if flag:
                ans.append(res1)
                res.append(s[res1[0] : res1[1] + 1])
        return res