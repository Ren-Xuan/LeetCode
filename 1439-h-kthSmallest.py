class Solution(object):
    def kthSmallest(self, mat, k):
        candidates = [0]
        for ln in mat:
            candidates = [i + j for i in candidates for j in ln]
            candidates.sort()
            candidates = candidates[:k]
        return candidates[k - 1]