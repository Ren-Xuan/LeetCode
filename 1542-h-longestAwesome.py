class Solution:
    def longestAwesome(self, s: str) -> int:
        #状态压缩 + dp(固定当前位为末位，往前探)
        prefix_state_idx = defaultdict(int)     #每个状态，第一次出现的index
        prefix_state_idx[0] = -1
        res = 0
        sequence = 0
        for i,c in enumerate(s):
            digit = int(c)
            sequence ^= (1 << digit)
            #每个数字出现的次数，全是偶数次的情况
            if sequence in prefix_state_idx:    #往前探，找第一次出现的位置
                cur_len = i - prefix_state_idx[sequence]
                res = max(res, cur_len)
            else:
                prefix_state_idx[sequence] = i
            #只允许某一个数字，出现次数为奇数
            for j in range(10):
                if (sequence ^ (1 << j)) in prefix_state_idx:
                    cur_len = i - prefix_state_idx[sequence ^ (1 << j)]
                    res = max(res, cur_len)
            
        return res
            

