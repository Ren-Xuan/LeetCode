class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans = [deck.pop()]
        for val in deck[::-1]:
            ans.insert(0, ans.pop())
            ans.insert(0, val)
        return ans