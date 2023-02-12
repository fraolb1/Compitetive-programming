class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        length = k
        for i in num:
            while stack and stack[-1] > i and k!=0:
                k -= 1
                stack.pop()
            stack.append(i)
        print(len(stack),len(num)-length)
        while len(stack) > len(num)-length:
            stack.pop()
        if stack:
            res = ''.join(stack)
            res = int(res)
            return str(res)
        else:
            return "0"
