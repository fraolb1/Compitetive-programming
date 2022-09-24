class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        num = n
        while n >= 2:
            num /= 3
            n //= 3
        return True if num == 1 and n > 0 else False