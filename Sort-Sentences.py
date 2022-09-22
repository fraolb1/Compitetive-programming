class Solution:
    def sortSentence(self, s: str) -> str:
        a = s.split(" ")
        b = ""
        for i in range(1, len(a)+1):
            for j in range(len(a)):
                if int(a[j][-1]) == i:
                    b += " " + a[j][:len(a[j])-1]
                    break
                else:
                    continue
        return b.strip()
