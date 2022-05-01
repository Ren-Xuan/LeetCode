class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []   # 目标偶数数组
        freq = Counter(digits)   # 整数数组中各数字的出现次数
        # 枚举所有三位偶数，维护整数中各数位的出现次数并比较判断是否为目标偶数
        for i in range(100, 1000, 2):
            freq1 = Counter([int(d) for d in str(i)])
            if all(freq[d] >= freq1[d] for d in freq1.keys()):
                res.append(i)
        return res
