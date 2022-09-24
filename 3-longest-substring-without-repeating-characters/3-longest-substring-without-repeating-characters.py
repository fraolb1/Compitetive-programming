class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        for j in range(len(s)):
            x = 0
            n = []
            for i in range(j,len(s)):
                if s[i] not in n:
                    n.append(s[i])
                    x += 1
                else:
                    break
                if x > l:
                    l = x
        return l        