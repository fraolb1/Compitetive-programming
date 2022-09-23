class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        j = len(piles)-2
        i = 0
        ans = 0
        while i<j:
            ans += piles[j]
            j -= 2
            i += 1
        return ans
