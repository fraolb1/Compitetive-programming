class Solution:
    def reverseWords(self, s: str) -> str:
        curr = s.strip()
        curr = curr.split()
        res = list()
        for i in range(len(curr)-1,-1,-1):
            res.append(curr[i])
        return " ".join(res)