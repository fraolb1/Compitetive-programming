class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = ['a','e','i','o','u']
        fhalf = s[:len(s)//2]
        shalf = s[len(s)//2:]
        fcount = 0
        scount = 0
        for i in fhalf:
            if i.lower() in vowel:
                fcount += 1
        for i in shalf:
            if i.lower() in vowel:
                scount += 1
        if scount == fcount:
            return True
        return False