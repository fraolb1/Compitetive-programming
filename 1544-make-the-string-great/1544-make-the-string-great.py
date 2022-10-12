class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and i.isupper() and i.lower() == stack[-1]:
                stack.pop()
            elif stack and stack[-1].isupper() and stack[-1].lower() == i:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)