from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        record = {0: 1}
        total, ans = 0, 0
        for elem in nums:
            total += elem
            modulus = total % k
            same = record.get(modulus, 0)
            ans += same
            record[modulus] = same + 1
        return ans
