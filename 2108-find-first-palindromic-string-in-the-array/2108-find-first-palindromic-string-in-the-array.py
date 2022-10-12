class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            l,r = 0,len(i)-1
            flag = True
            while l < r:
                if i[l] == i[r]:
                    r -= 1
                    l += 1
                else:
                    flag = False
                    break
            if flag:
                return i
        return ""